from tkinter import *
from api_post import *
APIs = GameAPI()
root = Tk()
root.title('Game Outside Game 3 :: Utility')
root.geometry("480x280")
root.resizable(0,0)
Frames = Frame(root)
def exec_api(*args):
    result = APIs.exec(context.get())
    msg_status.configure(text=f"{result}")
def Screen_obj():
    global context,msg_status
    context = StringVar()
    Label(Frames,text="Please enter answer:",font=("","14")).pack(pady=6)
    texts = Entry(Frames,textvariable=context)
    texts.pack()
    Button(Frames,text='SEND ANSWER!',command=lambda: exec_api(),bg="#7FC700",fg="#fff").pack(pady=9)
    msg_status = Label(Frames,text='',bg="gray",width=30,fg="#fff")
    msg_status.pack(pady=5)

Screen_obj() # Place object
root.bind('<Return>',exec_api)
Frames.pack()
root.mainloop()