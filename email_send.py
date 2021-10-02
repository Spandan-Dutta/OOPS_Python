# Code to send email
import smtplib
server = smtplib.SMTP("smtp.gmail.com" , 587)
server.starttls()
login_id = input("Please enter your email id: ")
login_password = input("Please enter your password: ")
server.login(login_id,login_password)
message = "Hello This is Spandan"
server.sendmail("spandan.dutta_cs.ccv19@gla.ac.in" , "bhatnagarujjwal46@gmail.com" ,message)
server.quit()
