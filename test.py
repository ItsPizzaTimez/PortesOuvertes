from http import server
import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465) # variable qui est egale au client

server.login("jpocondorcet@gmail.com","1fR     a$0     w!") # on connecte le client au compte google du "bot"

# creation du mail

user = str(input("choisissez votre destinataire : "))
text = str(input("ecrivez votre mail : "))

server.sendmail("jpocondorcet@gmail.com",user,text)