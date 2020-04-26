from tkinter import *
import smtplib

def enviar():
  if emisor.get()=='' and password=='':
    monitor.set('Por favor, llenar los campos')
  else:
    Email1=str(emisor.get())
    Epass1 = str(password.get())
    Email2 =str(receptor.get())
    subject = str(asunto.get())
    msg = str(mensaje.get(1.0, 'end'))
    msg='Subject: {Subject}\n\n{Asunto}'.format(Subject=subject, Asunto=msg)
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(Email1,Epass1 )
    server.sendmail(Email1,Email2,msg)
    server.quit()
    monitor.set('Enviado correctamente')
    Email1 = emisor.set('')

root = Tk()
root.title("Apliacacion de correo")
root.geometry("700x400")

Color_Bg="#006"
Colol_Fg = "white"
font=('Times new roman', 12)

emisor = StringVar()
password=StringVar()
receptor = StringVar()
asunto = StringVar()
#Cuerpo(Lable, Entry)
Label(root, text="Emisor Email: ", font=font, fg=Colol_Fg, bg=Color_Bg).grid(row=1, column=0, padx=5, pady=5)
emisorEmail=Entry(root, textvar=emisor)
emisorEmail.grid(row=1, column=1, sticky=W + E,padx=5, pady=5)

Label(root, text="Contraseña: ", font=font, fg=Colol_Fg, bg=Color_Bg).grid(row=2, column=0, padx=5, pady=5)
passEmisor=Entry(root, textvar=password, show='*')
passEmisor.grid(row=2, column=1, sticky=W + E,padx=5, pady=5)

Label(root, text="Correo de receptor: ", font=font, fg=Colol_Fg, bg=Color_Bg).grid(row=3, column=0, padx=5, pady=5)
receptorEmail=Entry(root, textvar=receptor)
receptorEmail.grid(row=3, column=1, sticky=W + E,padx=5, pady=5)

Label(root, text="Asunto: ", font=font, fg=Colol_Fg, bg=Color_Bg).grid(row=4, column=0, padx=5, pady=5)
emisorEmail=Entry(root, textvar=asunto)
emisorEmail.grid(row=4, column=1, sticky=W + E,padx=5, pady=5)

mensaje = Text(root)
mensaje.grid(row=5, column=1)
mensaje.config(width=45, height=10, font=font,padx=5, pady=5)

botonEnviar=Button(root, text="Enviar", font=font, command=enviar)
botonEnviar.grid(row=5, column=3,padx=5, pady=5)

monitor = StringVar()
monitor.set("Apliacion para enviar correo")
indicador = Label(root, textvar=monitor, justify='center', pady=5, fg=Colol_Fg, bg=Color_Bg).grid(row=6, column=1)


root.mainloop()
