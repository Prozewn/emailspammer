import smtplib, ssl, threading

my_mail = "forspamretard@seznam.cz"
my_pass = "f0r$pamretard12"
server = "smtp.seznam.cz"
port = 465
reciever = " RECIEVER EMAIL HERE"
message = " MESSAGE HERE "
threads_no = 10

def spammer():
    while True:
        sslcontext = ssl.create_default_context()
        connection = smtplib.SMTP_SSL(server, port, sslcontext)
        connection.login(my_mail, my_pass)
        connection.sendmail(my_mail, reciever, message)
        print("email sent")

threads = []

for i in range(threads_no):
    t = threading.Thread(target=spammer)
    t.daemon = True
    threads.append(t)

for i in range (threads_no):
    threads[i].start()

for i in range(threads_no):
    threads[i].join()