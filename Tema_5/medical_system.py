"""
Sistema de Gestión de Citas Médicas
"""

# ==================== CLASE PACIENTE ====================
class Paciente:
    """Representa un paciente del consultorio médico"""

    contador_pacientes = 0

    def __init__(self, nombre, edad, telefono, email):
        Paciente.contador_pacientes += 1
        self.id = f"PAC{Paciente.contador_pacientes:04d}"
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.email = email
        self.historial_citas = []

    def agregar_cita(self, cita):
        self.historial_citas.append(cita)

    def mostrar_info(self):
        print(f"\n{'='*50}")
        print(f"ID: {self.id} | Nombre: {self.nombre} | Edad: {self.edad} años")
        print(f"Teléfono: {self.telefono} | Email: {self.email}")
        print(f"Total de citas: {len(self.historial_citas)}")
        print(f"{'='*50}")

    def __str__(self):
        return f"{self.id} - {self.nombre} ({self.edad} años)"
    

# ==================== CLASE DOCTOR ====================
class Doctor:
    """Clase base para los doctores del consultorio"""

    contador_doctores = 0

    def __init__(self, nombre, especialidad, telefono):
        Doctor.contador_doctores += 1
        self.id = f"DOC{Doctor.contador_doctores:04d}"
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono
        self.citas_programadas = []

    def agregar_cita(self, cita):
        self.citas_programadas.append(cita)

    def verificar_disponibilidad(self, fecha, hora):
        for cita in self.citas_programadas:
            if cita.fecha == fecha and cita.hora == hora and cita.estado != "Cancelada":
                return False
        return True
    
    def mostrar_info(self):
        citas_activas = len([c for c in self.citas_programadas if c.estado == 'Programada'])
        print(f"\n{'='*50}")
        print(f"ID: {self.id} | Dr(a). {self.nombre}")
        print(f"Especialidad: {self.especialidad} | Teléfono: {self.telefono}")
        print(f"Citas programadas: {citas_activas}")
        print(f"{'='*50}")

    def __str__(self):
        return f"{self.id} - Dr(a). {self.nombre} - {self.especialidad}"
    

# ==================== HERENCIA: ESPECIALIDADES ====================
class Cardiologo(Doctor):
    def __init__(self, nombre, telefono):
        super().__init__(nombre, "Cardiologia", telefono)
        self.costo_consulta = 800

class Pediatra(Doctor):
    def __init__(self, nombre, telefono):
        super().__init__(nombre, "Pediatria", telefono)
        self.coste_consulta = 600

class Dermatologo(Doctor):
    def __init__(self, nombre, telefono):
        super().__init__(nombre, "Dermatologia", telefono)
        self.costo_consulta = 700


# ==================== CLASE CITA ====================
class Cita:
    """Representa una cita medica"""

    contador_citas = 0

    def __init__(self, paciente, doctor, fecha, hora, motivo):
        Cita.contador_citas += 1
        self.id = f"CIT{Cita.contador_citas:04d}"
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = "Programada"
        self.diagnostico = ""

    def cancelar(self):
        self.estado = "Cancelada"

    def completar(self, diagnostico):
        self.estado = "Completada"
        self.diagnostico = diagnostico

    def mostrar_info(self):
        print(f"\n{'='*60}")
        print(f"ID Cita: {self.id} | Estado: {self.estado}")
        print(f"Paciente: {self.paciente.nombre} (ID: {self.paciente.id})")
        print(f"Doctor: {self.doctor.nombre} - {self.doctor.especialidad}")
        print(f"Fecha: {self.fecha} | Hora: {self.hora}")
        print(f"Motivo: {self.motivo}")
        if self.diagnostico:
            print(f"Diagnóstico: {self.diagnostico}")
        print(f"Costo: ${self.doctor.costo_consulta}")
        print(f"{'='*60}")

    def __str__(self):
        return f"{self.id} - {self.paciente.nombre} con {self.doctor.nombre} ({self.fecha} {self.hora}) [{self.estado}]"
    

# ==================== CLASE CONSULTORIO ====================
class Consultorio:
    """Gestiona todo el sistema de citas médicas"""

    def __init__(self, nombre):
        self.nombre = nombre
        self.pacientes = []
        self.doctores = []
        self.citas = []

    def registrar_paciente(self, nombre, edad, telefono, email):
        paciente = Paciente(nombre, edad, telefono, email)
        self.pacientes.append(paciente)
        print(f"\n✓ Paciente registrado exitosamente con ID: {paciente.id}")
        return paciente
    
    def registrar_doctor(self, tipo, nombre, telefono):
        if tipo == "1":
            doctor = Cardiologo(nombre, telefono)
        elif tipo == "2":
            doctor = Pediatra(nombre, telefono)
        elif tipo == "3":
            doctor = Dermatologo(nombre, telefono)
        else:
            print("✗ Tipo de especialidad no válido")
            return None
        self.doctores.append(doctor)
        print(f"\n✓ Doctor registrado exitosamente con ID: {doctor.id}")
        return doctor
    
    def agendar_cita(self, id_paciente, id_doctor, fecha, hora, motivo):
        paciente = self.buscar_paciente(id_paciente)
        doctor = self.buscar_doctor(id_doctor)

        if not paciente or not doctor:
            print("✗ Paciente o Doctor no encontrado")
            return None
        
        if not doctor.verificar_disponibilidad(fecha, hora):
            print("✗ El doctor no está disponible en ese horario")
            return None
        
        cita = Cita(paciente, doctor, fecha, hora, motivo)
        self.citas.append(cita)
        paciente.agregar_cita(cita)
        doctor.agregar_cita(cita)
        print(f"\n✓ Cita agendada exitosamente con ID: {cita.id}")
        return cita

    def buscar_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return paciente
        return None

    def buscar_doctor(self, id_doctor):
        for doctor in self.doctores:
            if doctor.id == id_doctor:
                return doctor
        return None
    
    def buscar_cita(self, id_cita):
        for cita in self.citas:
            if cita.id == id_cita:
                return cita
        return None
    
    def mostrar_pacientes(self):
        if not self.pacientes:
            print("\n✗ No hay pacientes registrados")
            return
        print(f"\n{'='*60}\nLISTADO DE PACIENTES ({len(self.pacientes)} total)\n{'='*60}")
        for paciente in self.pacientes:
            print(paciente)
    
    def mostrar_doctores(self):
        if not self.doctores:
            print("\n✗ No hay doctores registrados")
            return
        print(f"\n{'='*60}\nLISTADO DE DOCTORES ({len(self.doctores)} total)\n{'='*60}")
        for doctor in self.doctores:
            print(doctor)

    def mostrar_citas(self, filtro="todas"):
        if not self.citas:
            print("\n✗ No hay citas registradas")
            return
        
        if filtro == "programadas":
            citas_filtradas = [c for c in self.citas if c.estado == "Programada"]
        if filtro == "completadas":
            citas_filtradas = [c for c in self.citas if c.estado == "Completada"]
        if filtro == "canceladas":
            citas_filtradas = [c for c in self.citas if c.estado == "Cancelada"]
        else:
            citas_filtradas = self.citas

        print(f"\n{'='*60}\nCITAS - {filtro.upper()} ({len(citas_filtradas)} total)\n{'='*60}")
        for cita in citas_filtradas:
            print(cita)


def mostrar_menu():
    print("\n" + "="*60)
    print(f"{'🏥 SISTEMA DE GESTIÓN DE CITAS MÉDICAS':^60}")
    print("="*60)
    print("1.  Registrar nuevo paciente")
    print("2.  Registrar nuevo doctor")
    print("3.  Agendar cita")
    print("4.  Ver información de paciente")
    print("5.  Ver información de doctor")
    print("6.  Ver información de cita")
    print("7.  Cancelar cita")
    print("8.  Completar cita (agregar diagnóstico)")
    print("9.  Listar todos los pacientes")
    print("10. Listar todos los doctores")
    print("11. Listar todas las citas")
    print("12. Listar citas programadas")
    print("0.  Salir")
    print("="*60)


def main():
    consultorio = Consultorio("Centro Medico Salud Total")

    # Datos de ejemplo
    consultorio.registrar_doctor("1", "Ana García", "555-0101")
    consultorio.registrar_doctor("2", "Carlos Rodríguez", "555-0102")
    consultorio.registrar_doctor("3", "María López", "555-0103")

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\n--- REGISTRAR NUEVO PACIENTE ---")
            nombre = input("Nombre completo: ")
            edad = int(input("Edad: "))
            telefono = input("Teléfono: ")
            email = input("Email: ")
            consultorio.registrar_paciente(nombre, edad, telefono, email)

        elif opcion == "2":
            print("\n--- REGISTRAR NUEVO DOCTOR ---")
            print("Especialidades: 1.Cardiología 2.Pediatría 3.Dermatología")
            tipo = input("Seleccione especialidad: ")
            nombre = input("Nombre completo: ")
            telefono = input("Teléfono: ")
            consultorio.registrar_doctor(tipo, nombre, telefono)

        elif opcion == "3":
            print("\n--- AGENDAR CITA ---")
            consultorio.mostrar_pacientes()
            id_paciente = input("\nID del paciente: ").upper()
            consultorio.mostrar_doctores()
            id_doctor = input("\nID del doctor: ").upper()
            fecha = input("Fecha (YYYY-MM-DD): ")
            hora = input("Hora (HH:00): ")
            motivo = input("Motivo de la consulta: ")
            consultorio.agendar_cita(id_paciente, id_doctor, fecha, hora, motivo)

        elif opcion == "4":
            id_paciente = input("\nID del paciente: ").upper()
            paciente = consultorio.buscar_paciente(id_paciente)
            if paciente:
                paciente.mostrar_info()
            else:
                print("✗ Paciente no encontrado")
        
        elif opcion == "5":
            id_doctor = input("\nID del doctor: ").upper()
            doctor = consultorio.buscar_doctor(id_doctor)
            if doctor:
                doctor.mostrar_info()
            else:
                print("✗ Doctor no encontrado")
        
        elif opcion == "6":
            id_cita = input("\nID de la cita: ").upper()
            cita = consultorio.buscar_cita(id_cita)
            if cita:
                cita.mostrar_info()
            else:
                print("✗ Cita no encontrada")
        
        elif opcion == "7":
            id_cita = input("\nID de la cita a cancelar: ").upper()
            cita = consultorio.buscar_cita(id_cita)
            if cita:
                cita.cancelar()
                print("✓ Cita cancelada exitosamente")
            else:
                print("✗ Cita no encontrada")

        elif opcion == "8":
            id_cita = input("\nID de la cita: ").upper()
            cita = consultorio.buscar_cita(id_cita)
            if cita:
                diagnostico = input("Diagnóstico: ")
                cita.completar(diagnostico)
                print("✓ Cita completada exitosamente")
            else:
                print("✗ Cita no encontrada")

        elif opcion == "9":
            consultorio.mostrar_pacientes()

        elif opcion == "10":
            consultorio.mostrar_doctores()
        
        elif opcion == "11":
            consultorio.mostrar_citas("todas")
        
        elif opcion == "12":
            consultorio.mostrar_citas("programadas")

        elif opcion == "0":
            print("\n¡Gracias por usar el Sistema de Gestión de Citas Médicas!")
            print("¡Hasta pronto! 👋\n")
            break
        
        else:
            print("\n✗ Opción no válida. Por favor, intente de nuevo.")
        
        input("\nPresione ENTER para continuar...")


# ===== EJECUTAR EL PROGRAMA =====
# Llamar a la función principal
main()