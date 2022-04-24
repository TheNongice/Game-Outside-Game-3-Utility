from tkinter import *
from api_post import *
from tkinter import messagebox

# Check System
import platform

if platform.system() == 'Darwin':
    from tkmacosx import Button

root = Tk()
root.title('Game Outside Game 3 :: Utility')
root.geometry("480x280")
root.resizable(0, 0)
Frames = Frame(root)


def exec_api(*args):
    APIs = GameAPI()
    result = APIs.exec(context.get())
    msg_status.configure(text=f"{result}")


def Screen_obj():
    global context, msg_status
    context = StringVar()
    Label(Frames, text="Please enter answer:", font=("", "20")).pack(pady=6)
    texts = Entry(Frames, textvariable=context, font=('', '14'))
    texts.pack()
    Button(Frames, text='SEND ANSWER!', command=lambda: exec_api(), bg="#7FC700", fg="#fff", font=('', '14')).pack(
        pady=9)
    msg_status = Label(Frames, text='', bg="gray", width=30, fg="#fff", font=('', '14'))
    msg_status.pack(pady=5)


def CONFIG_GUI():
    global ip, port, gui_ip, msg_gui
    ip = StringVar()
    port = StringVar()
    gui_ip = Toplevel()
    gui_ip.geometry('480x280')
    gui_ip.resizable(0, 0)
    gui_frame = Frame(gui_ip)
    ip_text = Label(gui_frame, text="IP: ", font=('', '14')).grid(row=0, column=0)
    ip_clues = Entry(gui_frame, textvariable=ip, font=('', '14')).grid(row=0, column=1)
    port_text = Label(gui_frame, text="Port ", font=('', '14')).grid(row=1, column=0)
    port_clues = Entry(gui_frame, textvariable=port, font=('', '14')).grid(row=1, column=1)
    gui_frame.pack(pady=20)
    submit = Button(gui_ip, text="SAVE", command=save_ip, bg="#7FC700", fg="#fff", font=('', '14')).pack(anchor=CENTER)
    msg_gui = Label(gui_ip, text='', font=('', '14'))
    msg_gui.pack(pady=13)
    gui_ip.bind('<Return>', save_ip)


def save_ip(*args):
    clues = open('connect.txt', 'w')
    ips = ip.get()
    ports = port.get()
    if (ports == '') and (ips == ''):
        ips = '127.0.0.1'
        ports = '3000'
    else:
        pass
    clues.writelines(f'{ips}\n{ports}')
    clues.close()
    msg_gui.configure(text='DATA HAVE BEEN CHANGED!')
    msg_gui.after(1500,clear_status)

def clear_status():
    msg_gui.configure(text="")

def BF():
    APIs = GameAPI()
    MsgBox = messagebox.askquestion('Warning!', 'Are you sure you want to Bruteforce now?', icon='warning')
    if MsgBox == 'yes':
        APIs.bruteforce()
    else:
        pass


Screen_obj()  # Place object
root.bind('<Return>', exec_api)
Frames.pack()
test = Button(root, text="Bruteforce Choice", command=BF, font=('', '14'), bg="#FFCF40", fg="#000").pack()
config_btn = Button(root, text="Change IP/Port", command=CONFIG_GUI).pack(side=BOTTOM, anchor=W)
msg_os = Label(root, text=f"You're running on {platform.system()}!", bg="gray", fg="#fff", font=('', '10')).pack(
    side=BOTTOM, pady=8)

root.mainloop()
