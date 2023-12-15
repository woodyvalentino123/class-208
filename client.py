#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox = None 
textarea = None 
labelchat = None 
text_message = None 

def connectToServer():
    global SERVER
    global name 
    
    cname = name.get()
    SERVER.send(cname.encode())

def openChatWindow():
    window = Tk()
    window.title("Messenger")
    window.geometry("500x350")

    global name
    global listbox
    global textarea
    global labelchat
    global text_message

    name_label=Label(window,text="enter your name", font=("Calibri",10))
    name_label.place(x=10,y=8)
    
    name=Entry(window,width=30,font=("Calibri",10))
    name.place(x=120,y=8)
    name.focus()

    connectserver = Button(window, text = "Connect to chat server", bd = 1,font=("Calibri",10), command = connectToServer )
    connectserver.place(x = 350, y = 6)

    separator = ttk.Separator(window, orient = 'horizontal')
    separator.place(x = 0, y = 35, relwidth = 1, height = 0.1)

    labelusers = Label(window, text = "Active Users", font = ("Calibri",10))
    labelusers.place(x = 10, y = 70)

    listbox = Listbox(window, height = 5, width = 67, activestyle='dotbox', font = ("Calibri",10))
    listbox.place( x= 10, y = 50)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1, relx = 1)
    scrollbar1.config(command = listbox.yview)

    connectButton = Button(window, text = "Connect", bd = 1,font=("Calibri",10), command = connectToServer )
    connectButton.place(x = 280, y = 160)

    disconnectbutton = Button(window, text = "Disconnect", bd = 1,font=("Calibri",10), command = connectToServer )
    disconnectbutton.place(x = 350, y = 160)

    refresh = Button(window, text = "Refresh", bd = 1,font=("Calibri",10), command = connectToServer )
    refresh.place(x = 435, y = 160)

    labelchat = Label(window, text = "chat Window", font = ("Calibri",10))
    labelchat.place(x = 10, y = 180)

    textarea=Text(window,width=67,height=6,font=("Calibri",10))
    textarea.place(x=10,y=200)

    scrollbar2 = Scrollbar(textarea)
    scrollbar2.place(relheight = 1, relx = 1)
    scrollbar2.config(command = listbox.yview)

    attach = Button(window, text = "attach", bd = 1,font=("Calibri",10) )
    attach.place(x = 10, y = 300)

    text_message=Entry(window,width=40,font=("Calibri",12))
    text_message.place(x=100,y=305)
    text_message.pack()

    send = Button(window, text = "send", bd = 1,font=("Calibri",10) )
    send.place(x = 450, y = 305)

    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    openChatWindow()


setup()


#-----------Bolierplate Code Start -----