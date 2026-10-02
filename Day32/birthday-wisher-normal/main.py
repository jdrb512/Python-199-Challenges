import datetime as dt
import random
import smtplib
import pandas as pd

MY_EMAIL = "joserbd512@gmail.com"
MY_PASSWORD = "xjqzvdgbhezrvfra"

# 1. Obtener la fecha de hoy (mes y día)
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# 2. Leer el CSV con pandas
data = pd.read_csv("Day32/birthday-wisher-normal/birthdays.csv")

# 3. Crear un diccionario con la estructura {(month, day): data_row}
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

# 4. Comprobar si la tupla de hoy está en el diccionario
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # Elegir una plantilla aleatoria (letter_1.txt, letter_2.txt, etc.)
    file_path = f"Day32/birthday-wisher-normal/letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        # Reemplazar la marca [NAME] por el nombre real
        contents = contents.replace("[NAME]", birthday_person["name"])

    # 5. Enviar el correo
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}",
        )
    print("¡Correo de cumpleaños enviado con éxito!")