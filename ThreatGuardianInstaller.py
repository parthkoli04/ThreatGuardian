# Program to make a simple
# login screen


from tkinter import *
import tkinter as tk
from tkinter import font as tkfont 
import os
from all_paths import username_file_path,password_file_path,email_file_path,purchase_file_path


import webbrowser
def callback(url):
    webbrowser.open_new(url)



from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/assets_installer")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#118BE4")
window.title("ThreatGuardian Installer")

canvas = Canvas(
    window,
    bg = "#118BE4",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    393.9999999999999,
    7.105427357601002e-15,
    861.9999999999999,
    519.0,
    fill="#FCFCFC",
    outline="")

canvas.create_text(
    484.9999999999999,
    371.0,
    anchor="nw",
    text="Email :",
    fill="#000000",
    font=("Roboto Bold", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: vaildate_em_pd(str(entry_3.get()),str(entry_4.get())),
    relief="flat"
)
button_1.place(
    x=555.9999999999999,
    y=432.0,
    width=180.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda : callback("https://github.com/parthkoli04/ThreatGuardian/releases"),
    relief="flat"
)
button_2.place(
    x=8.999999999999886,
    y=432.0,
    width=164.0,
    height=55.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:callback ("https://github.com/parthkoli04/ThreatGuardian/blob/main/LICENSE"),
    relief="flat"
)
button_3.place(
    x=218.9999999999999,
    y=432.0,
    width=164.0,
    height=55.0
)

canvas.create_text(
    26.999999999999886,
    14.000000000000007,
    anchor="nw",
    text="Welcome to \nThreatGuardian Antivirus Installer  ",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    525.9999999999999,
    17.000000000000007,
    anchor="nw",
    text="ThreatGuardian Installer ",
    fill="#505485",
    font=("Ruda Regular", 24 * -1)
)

canvas.create_rectangle(
    26.999999999999886,
    73.0,
    131.9999999999999,
    80.0,
    fill="#DEFF17",
    outline="")

canvas.create_rectangle(
    495.9999999999999,
    52.00000000000001,
    722.9999999999999,
    57.00000000000001,
    fill="#0783F6",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    684.4999999999999,
    110.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_1.place(
    x=568.9999999999999,
    y=80.0,
    width=231.0,
    height=59.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    684.4999999999999,
    199.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_2.place(
    x=568.9999999999999,
    y=169.0,
    width=231.0,
    height=59.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    684.4999999999999,
    297.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_3.place(
    x=568.9999999999999,
    y=267.0,
    width=231.0,
    height=59.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    684.4999999999999,
    384.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_4.place(
    x=568.9999999999999,
    y=354.0,
    width=231.0,
    height=59.0
)

canvas.create_text(
    437.9999999999999,
    186.0,
    anchor="nw",
    text="Password :",
    fill="#000000",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    402.9999999999999,
    287.0,
    anchor="nw",
    text="Purchase date : ",
    fill="#000000",
    font=("Roboto Bold", 22 * -1)
)

canvas.create_text(
    435.9999999999999,
    96.0,
    anchor="nw",
    text="User Name :",
    fill="#000000",
    font=("Roboto Bold", 22 * -1)
)

canvas.create_text(
    23.999999999999886,
    91.0,
    anchor="nw",
    text="About :",
    fill="#FD8585",
    font=("Acme Regular", 23 * -1)
)

canvas.create_text(
    20.999999999999886,
    150.0,
    anchor="nw",
    text="Threat Guardian employs \nstate-of-the-art scanning techniques,\n including signature-based \ndetection and heuristic \nanalysis, to proactively identify \nand neutralize malware.",
    fill="#FCFCFC",
    font=("Acme Regular", 23 * -1)
)

# canvas.create_text(
#     20.999999999999886,
#     310.0,
#     anchor="nw",
#     text="This project is sequel to\nKilo-Antivirus 2\nThis project was renamed because\nit is no longer similar to Kilo-Antivirus.",
#     fill="#00FF84",
#     font=("Acme Regular", 23 * -1)
# )



with open('emails.html', 'r',encoding='utf-8') as f:
    html_string = f.read()

#html_message = html_string.replace('{{usr_email}}',email).replace('{{user}}',user_name).replace('{{password}}',password).replace('{{purchase}}',purchase).replace('{{end_date}}', main_date)  
# declaring string variable
# for storing name and password


# defining a function that will
# get the name and password and
# print them on the screen
def submit():
    
	user_name=entry_1.get()
	password=entry_2.get()
	email=entry_4.get()
	purchase=entry_3.get()

    
	

	import datetime 
	from datetime import date 
	from tkinter import messagebox


    
    
    
	date_time_obj = datetime.datetime.strptime(purchase, '%d-%m-%Y').date()
	main_date = date_time_obj + datetime.timedelta(days=365)
	
	remaining_days = (main_date - date.today()).days
	messagebox.showinfo("showinfo", "Regestraion succesfully. Check your email")
	name = open(username_file_path, "w") #opens file usernames.txt and gets ready to write to it
	

	name.write(user_name) #writes contents in file to usernames.txt
	name.close() #closes file
	open1 = open(username_file_path, "r") #opens file to read it
	print (open1.read()) #prints whatever is in the text file

	#Password
	name = open(password_file_path, "w") #opens file usernames.txt and gets ready to write to it
	

	name.write(password) #writes contents in file to usernames.txt
	name.close() #closes file
	open1 = open(password_file_path, "r") #opens file to read it
	print (open1.read()) #prints whatever is in the text file

	#Email
	name = open(email_file_path, "w") #opens file usernames.txt and gets ready to write to it
	

	name.write(email) #writes contents in file to usernames.txt
	name.close() #closes file
	open1 = open(email_file_path, "r") #opens file to read it
	print (open1.read()) #prints whatever is in the text file

	#purchase
	name = open(purchase_file_path, "w") #opens file usernames.txt and gets ready to write to it
	

	name.write(purchase) #writes contents in file to usernames.txt
	name.close() #closes file
	open1 = open(purchase_file_path, "r") #opens file to read it
	print (open1.read()) #prints whatever is in the text file
    


    
	
	html_message = html_string.replace('{{usr_email}}',email).replace('{{user}}',user_name).replace('{{password}}',password).replace('{{purchase}}',purchase).replace('{{end_date}}', main_date.strftime('%d/%m/%Y'))
	import smtplib, ssl
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart
    
    
    
	sender_email = "bella.thruster@gmail.com"
	receiver_email = email
	password = "qokodpbywvypsgug"

	message = MIMEMultipart("alternative")
	message["Subject"] = "ThreatGuardian antivirus Subscription"
	message["From"] = sender_email
	message["To"] = receiver_email

	# Create the plain-text and HTML version of your message
    
	text = f"""\
	Welcome {receiver_email} to ThreatGuardian Antivirus 1.0
	Your subscription will be of 365 days.
	So from today or {purchase} to this {main_date}."""
      
	html = html_message
	# Turn these into plain/html MIMEText objects
	part1 = MIMEText(text, "plain")
	part2 = MIMEText(html, "html")

	# Add HTML/plain-text parts to MIMEMultipart message
	# The email client will try to render the last part first
	message.attach(part1)
	message.attach(part2)
	
	# Create secure connection with server and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(
			sender_email, receiver_email, message.as_string()
		)


def vaildate_em_pd(pur_date,email):
    # Vaildate Purchase Date
    def check_date(pur_date):
        import datetime
        try:
            datetime.datetime.strptime(pur_date, '%d-%m-%Y')
            print("ok")
            return 0
        except ValueError:
            from tkinter import messagebox
            messagebox.showerror("Error in Date", "Incorrect data format, should be DD-MM-YYYY.")
            return 1

    def email_check(email):
        import re
        from tkinter import messagebox
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        # pass the regular expression
        # and the string into the fullmatch() method
        if(re.fullmatch(regex, email)):
            print("ok")
            return 2
    
        else:
            messagebox.showerror("Error in Email", "Incorrect email format.")
            return 3
    if check_date(pur_date) == 0 and email_check(email) == 2:
        submit()
    
window.resizable(False, False)	
window.mainloop()
