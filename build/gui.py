import tkinter
from datetime import date, time
from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Toplevel, Canvas, Entry, Label, Button, PhotoImage, messagebox, RIGHT, BOTH
from tkinter import Listbox, Scrollbar
from tkinter.ttk import Treeview
from tkinter import StringVar, IntVar, BooleanVar, DoubleVar
from tkcalendar import DateEntry

import login
import get_link
import webbrowser

# Path Initialize
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Window Initialize
window = Tk()
# window.title = "App"
window.geometry("1440x1024")
window.configure(bg="#FFFFFF")
window.resizable(False, False)

# Variable
login_flag = BooleanVar(value=False)
notification_flag = BooleanVar(value=False)

email_var = StringVar()
password_var = StringVar()
d_start, d_end = "", ""

link_root = 'https://firebasestorage.googleapis.com/v0/b/upload-video-536b1.appspot.com/o/'

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    1440.0,
    100.0,
    fill="#9CD0FA",
    outline="")

canvas.create_rectangle(
    0.0,
    974.0,
    1440.0,
    1024.0,
    fill="#FF6161",
    outline="")

canvas.create_rectangle(
    30.0,
    205.0,
    1410.0,
    955.0,
    fill="#D9D9D9",
    outline="#9CD0FA",
    width=5)

# Date Text
canvas.create_text(
    34.0,
    29.0,
    anchor="nw",
    text=str(date.today().day) + '/' + str(date.today().month) + '/' + str(date.today().year),
    fill="#000000",
    font=("InriaSans Light", 36 * -1)
)

# Filter Area
entry_image_dentry_start = PhotoImage(
    file=relative_to_assets("date_entry.png"))
entry_bg_dentry_start = canvas.create_image(
    935.0,
    160.0,
    image=entry_image_dentry_start
)
entry_dentry_start = DateEntry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 22 * -1)
)
entry_dentry_start.place(
    x=810.0,
    y=135.0,
    width=250.0,
    height=48.0
)

canvas.create_text(
    1075.0,
    145.0,
    anchor="nw",
    text="-",
    fill="#000000",
    font=("Inter", 24 * -1)
)

entry_image_dentry_end = PhotoImage(
    file=relative_to_assets("date_entry.png"))
entry_bg_dentry_end = canvas.create_image(
    1225.0,
    160.0,
    image=entry_image_dentry_end
)
entry_dentry_end = DateEntry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 22 * -1)
)
entry_dentry_end.place(
    x=1100.0,
    y=135.0,
    width=250.0,
    height=48.0
)

# Button OK
button_image_ok = PhotoImage(
    file=relative_to_assets("button_ok.png"))
button_ok = Button(
    image=button_image_ok,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_ok.place(
    x=1360.0,
    y=135.0,
    width=50.0,
    height=50.0
)

# Login Area
# Email
text_em = canvas.create_text(
    935.0,
    18.0,
    anchor="nw",
    text="Email",
    fill="#000000",
    font=("Inter", 16 * -1)
)

entry_image_email = PhotoImage(
    file=relative_to_assets("entry.png"))
entry_bg_email = canvas.create_image(
    1035.0,
    62.0,
    image=entry_image_email
)
entry_email = Entry(
    textvariable=email_var,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 18 * -1)
)
entry_email.place(
    x=935.0,
    y=42.0,
    width=200.0,
    height=38.0
)

# Password
text_pw = canvas.create_text(
    1150.0,
    18.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter", 16 * -1)
)

entry_image_password = PhotoImage(
    file=relative_to_assets("entry.png"))
entry_bg_password = canvas.create_image(
    1250.0,
    62.0,
    image=entry_image_password
)
entry_password = Entry(
    textvariable=password_var,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 18 * -1),
    show='*'
)
entry_password.place(
    x=1150.0,
    y=42.0,
    width=200.0,
    height=38.0
)


# Button submit
def submit_press():
    email = email_var.get()
    password = password_var.get()
    if email == '' or password == '':
        messagebox.showerror("Error", "Email and Password cannot be blank!")
    else:
        new_window = Toplevel(window)
        new_window.title = "Verified Code"
        new_window.geometry("380x60")
        new_window.configure(bg="#FFFFFF")
        new_window.resizable(False, False)

        code_var = IntVar(master=new_window)
        verified_code = StringVar(master=new_window)

        code_var.set(login.send_code(email))
        print(code_var.get())

        def accept_login():
            code = code_var.get()
            v_code = verified_code.get()
            if str(code) == str(v_code):
                login_flag.set(login.login(email, password))
                if login_flag:
                    messagebox.showinfo('Notification', "Login Successfully!")
                    new_window.destroy()
                    button_submit.destroy()
                    canvas.delete(text_em)
                    canvas.delete(text_pw)
                    entry_email.destroy()
                    entry_password.destroy()
                    canvas.delete(entry_email)
                    canvas.delete(entry_password)
                else:
                    messagebox.showerror('Error', "Email or Password is wrong.")
                    new_window.destroy()
            else:
                login_flag.set(value=False)
                messagebox.showerror('Error', "Verified code is not true!")

        label = Label(
            new_window,
            text='Code:',
            font=('calibre', 16, 'normal'),
            bg="#FFFFFF",
            fg="#000716",
        ).grid(row=0, column=0, padx=10, pady=10)
        entry = Entry(
            new_window,
            textvariable=verified_code,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Inter", 18 * -1)
        ).grid(row=0, column=1, padx=0, pady=10)
        button = Button(
            new_window,
            text='submit',
            font=('calibre', 14, 'normal'),
            bg="#FFFFFF",
            fg="#000716",
            command=accept_login
        ).grid(row=0, column=2, pady=10)
        # label_1 = Label(
        #     new_window,
        #     text='if you don\'t have the code.',
        #     font=('calibre', 16, 'normal'),
        #     bg="#FFFFFF",
        #     fg="#000716",
        # ).grid(row=1, column=1)
        # button_send = Button(
        #     new_window,
        #     text='Click here',
        #     font=('calibre', 14, 'normal'),
        #     bg="#FFFFFF",
        #     fg="#FF7716",
        #     command=send_code()
        # ).grid(row=2, column=1, pady=10)


button_image_submit = PhotoImage(
    file=relative_to_assets("button_submit.png"))
button_submit = Button(
    image=button_image_submit,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: submit_press(),
    relief="flat"
)
button_submit.place(
    x=1365.0,
    y=42.0,
    width=40.0,
    height=40.0
)

# Listbox link video    30.0, 205.0, 1410.0, 955.0,
listbox = Listbox(
    window,
    bg="#FFFFFF",
    activestyle='dotbox',
    font=("Inter", 24 * -1),
    fg="#000716"
)

file_name = get_link.get_video_name()
i = 0
# for name in file_name:
#     print(name)
for name in file_name:
    listbox.insert(i, name)
    if i >= 1000:
        i = 0
        break

listbox.place(
    x=32.5,
    y=207.5,
    width=1375,
    height=745
)

scroll_bar = Scrollbar(listbox)
scroll_bar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=listbox.yview)


def select_press():
    for item in listbox.curselection():
        print(listbox.get(item))
        webbrowser.open(link_root + listbox.get(item) + '?alt=media', new=2)


# Button Select
button_image_select = PhotoImage(
    file=relative_to_assets("button_select.png"))
button_select = Button(
    image=button_image_select,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select_press(),
    relief="flat"
)
button_select.place(
    x=30.0,
    y=135.0,
    width=195.0,
    height=50.0
)


# Button show full list video
def show_press():
    listbox.delete(first=0, last=1000)
    f_name = get_link.get_video_name()
    c = 0
    for n in f_name:
        listbox.insert(c, n)
        if c >= 1000:
            c = 0
            break


button_image_show = PhotoImage(
    file=relative_to_assets("button_show.png"))
button_show = Button(
    image=button_image_show,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_press(),
    relief="flat"
)
button_show.place(
    x=600.0,
    y=135.0,
    width=195.0,
    height=50.0
)

# main loop
window.mainloop()
