#Splash Screen

from customtkinter import *
import os
from PIL import Image, ImageTk


root = CTk()
root.title("Threat Guardian")
# root.resizable(False, False)
root.configure(bg='#252526')
root.overrideredirect(True)

root_wid=600
root_hgt=400

scr_wid=root.winfo_screenwidth()
scr_hgt=root.winfo_screenheight()

x=(scr_wid/2)-(root_wid/2)  
y=(scr_hgt/2)-(root_hgt/2)

root.geometry(f'{root_wid}x{root_hgt}+{int(x)}+{int(y)}')

logo = CTkImage(dark_image=Image.open("./res/0.png"), light_image=Image.open("./res/0.png"),size=(300,300))
spl = CTkLabel(root, image=logo,text="")
spl.place(x=150,y=0)

bar=CTkProgressBar(root,orientation=HORIZONTAL,mode='indeterminate',width=300)
bar.start()
bar.place(x=150,y=350)

text1 = CTkLabel(root, text="Stay Protected, Stay Secure.")
text1.configure(font=('Lobster', 20))
text1.place(x=200,y=300)

root.after(1000, lambda: text1.configure(text="Stay Protected, Stay Secure."))
root.after(2000, lambda: text1.configure(text="Your Shield Against Cyber Threats.."))
root.after(3000, lambda: text1.configure(text="Malware's Worst Nightmare..."))
root.after(4000, lambda: text1.configure(text="Keeping You Safe, Always...."))

def client():
    root.withdraw()
    os.system("python ./main.py")
    root.destroy()


root.after(5000,client)
root.mainloop()
