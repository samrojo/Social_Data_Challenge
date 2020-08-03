from Email_Test import Send_mail
import pandas as pd
import smtplib

df = pd.read_excel ('', sheet_name='')

mail = smtplib.SMTP('smtp.gmail.com', )
mail.ehlo()
mail.starttls()
mail.login('', '')

for index, row in df.iterrows():
    ID = row["ID"]
    gender = row["Sexo"]
    email = row["Correo"]
    print(ID, gender, email)
    Send_mail(email, gender, ID, mail)
    # input("Press Enter to continue...")

mail.quit()  # Cerrar Sesión
