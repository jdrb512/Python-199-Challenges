import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='torchvision')

import streamlit as st
from gfpgan import GFPGANer
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer
from config import CONFIG
from zeroscratches import EraseScratches
from PIL import Image
import cv2
import numpy as np


class ImageEnhancer:
    """Clase para manejar el modelo GFPGAN y el procesamiento de imágenes."""
    
    def __init__(self):
        self.model = None
        self.model_with_bg = None
        self._scratch_eraser = None  # Caché interno
    
    @property
    def scratch_eraser(self):
        """Lazy loading del EraseScratches con caché."""
        if self._scratch_eraser is None:
            self._scratch_eraser = EraseScratches()
        return self._scratch_eraser
    
    @st.cache_resource
    def load_model_simple(_self):
        """Carga GFPGAN sin RealESRGAN (solo mejora caras)."""
        with st.spinner("Cargando GFPGAN..."):
            model = GFPGANer(
                model_path=CONFIG['model_url'],
                upscale=CONFIG['upscale'],
                arch=CONFIG['arch'],
                channel_multiplier=CONFIG['channel_multiplier'],
                bg_upsampler=None
            )
        return model
    
    @st.cache_resource
    def load_model_with_background(_self):
        """Carga GFPGAN con RealESRGAN (mejora caras + fondo)."""
        with st.spinner("Cargando GFPGAN + RealESRGAN..."):
            model_bg = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, 
                               num_block=23, num_grow_ch=32, scale=2)
            bg_upsampler = RealESRGANer(
                scale=2,
                model_path='https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth',
                model=model_bg,
                tile=400,
                tile_pad=10,
                pre_pad=0,
                half=False
            )
            
            model = GFPGANer(
                model_path=CONFIG['model_url'],
                upscale=CONFIG['upscale'],
                arch=CONFIG['arch'],
                channel_multiplier=CONFIG['channel_multiplier'],
                bg_upsampler=bg_upsampler
            )
        return model

    def _remove_scratches(self, image_bgr: np.ndarray) -> np.ndarray:
        """Elimina rayas/grietas antes de pasar a GFPGAN."""
        img_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)
        
        restored_rgb = self.scratch_eraser.erase(pil_img)
        
        restored_rgb = np.array(restored_rgb, dtype=np.uint8)
        restored_bgr = cv2.cvtColor(restored_rgb, cv2.COLOR_RGB2BGR)
        return restored_bgr
    
    def enhance(self, image_bgr, repair_scratches=False, enhance_background=False):
        """
        Mejora una imagen con opciones configurables.
        
        Args:
            image_bgr: Imagen en formato BGR
            repair_scratches: Si True, repara grietas primero
            enhance_background: Si True, usa RealESRGAN para el fondo
        """
        # Paso 1: Reparar grietas (opcional)
        if repair_scratches:
            st.info("🔧 Reparando grietas y arañazos...")
            image_bgr = self._remove_scratches(image_bgr)
        
        # Paso 2: Seleccionar modelo según opciones
        if enhance_background:
            st.info("✨ Mejorando caras y fondo...")
            if self.model_with_bg is None:
                self.model_with_bg = self.load_model_with_background()
            model = self.model_with_bg
        else:
            st.info("✨ Mejorando caras...")
            if self.model is None:
                self.model = self.load_model_simple()
            model = self.model
        
        # Paso 3: Aplicar mejora
        _, _, restored_img = model.enhance(
            image_bgr,
            has_aligned=False,
            only_center_face=False,
            paste_back=True,
            weight=CONFIG['enhancement_weight']
        )
        
        return restored_img