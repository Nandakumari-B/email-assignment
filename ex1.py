import smtplib
import random
def read_data_send_mail():

    try: 

        f=open("student_mail.txt","r")
        student_mail=f.read()

        student_mail=student_mail.split(",")
        print(student_mail)
    except:
        print("file not available")

sender_email="nandu13123@gmail.com"

for i in student_mail:
    otp_number=random.randint(00000,99999)
    print(otp_number)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("nandu13123@gmail.com", "cevu thqw eykz vjra")
    message = f"Hi your otp number is {otp_number}"

try:
    s.sendmail("sender_email", i, message)
    print("mail send successfully")
    s.quit()
except:print("mail not sent")
read_data_send_mail()

