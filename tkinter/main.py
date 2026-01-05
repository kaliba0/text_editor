import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from pathlib import Path

from PIL import Image, ImageTk

win = tk.Tk()
win.title("TxtEditor")
win.geometry("800x500")
win.resizable(True, True)

current_file_path = ""


# Get the directory where this script is located
script_dir = Path(__file__).parent

new_icon = Image.open(script_dir / 'assets/new_icon.png').convert('RGBA')
new_icon = new_icon.resize((25, 25), Image.Resampling.LANCZOS)
new_icon = ImageTk.PhotoImage(new_icon)

save_icon = Image.open(script_dir / 'assets/save_icon.png').convert('RGBA')
save_icon = save_icon.resize((25, 25), Image.Resampling.LANCZOS)
save_icon = ImageTk.PhotoImage(save_icon)

back_icon = Image.open(script_dir / 'assets/play-back-outline.png').convert('RGBA')
back_icon = back_icon.resize((25, 25), Image.Resampling.LANCZOS)
back_icon = ImageTk.PhotoImage(back_icon)

forward_icon = Image.open(script_dir / 'assets/play-forward-outline.png').convert('RGBA')
forward_icon = forward_icon.resize((25, 25), Image.Resampling.LANCZOS)
forward_icon = ImageTk.PhotoImage(forward_icon)

open_icon = Image.open(script_dir / 'assets/folder-open-outline.png').convert('RGBA')
open_icon = open_icon.resize((25, 25), Image.Resampling.LANCZOS)
open_icon = ImageTk.PhotoImage(open_icon)

separator_icon = Image.open(script_dir / 'assets/line.png').convert('RGBA')
separator_icon = separator_icon.resize((25, 25), Image.Resampling.LANCZOS)
separator_icon = ImageTk.PhotoImage(separator_icon)





def open_file(event = None):
    file_type = [ ( "texte" , ".txt" )]
    file_name = tk.filedialog.askopenfilename(title = "Open", filetypes = file_type)
    global current_file_path 
    current_file_path = file_name
    print(current_file_path)
    if len(file_name) < 1 :
        tk.messagebox.showwarning(title = "Ooops",message = "Please choose another file")
    text_area.delete(1.0, "end")
    with open(file_name) as file :
        text_area.insert("end", file.read())


def new_file(event = None):
    file_name = tk.filedialog.asksaveasfilename(title = "New", confirmoverwrite = True, defaultextension = '.txt')
    global current_file_path
    current_file_path = file_name
    if file_name == None :
        tk.messagebox.showwarning(title = "Ooops",message = "Try again")

    open(file_name, "x")
    print(current_file_path)

def save(event = None):
    current_txt = text_area.get(1.0, "end")
    
    with open(current_file_path, "w") as file :
        file.write(current_txt)

    messagebox.showinfo(title="Your file have been saved", message=current_file_path, icon='info')

def back(event = None) :
    text_area.edit_undo()

def forward(event = None) :
    text_area.edit_redo()

def alert():
    messagebox.showinfo('Alert', 'bouton')
    
    

menubar = tk.Menu(win)

fileMenu = tk.Menu(menubar, tearoff=0)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_separator()
fileMenu.add_command(label="Quit", command=win.quit)
menubar.add_cascade(label="File", menu=fileMenu)

helpMenu = tk.Menu(menubar, tearoff=0)
helpMenu.add_command(label="About", command=alert)
menubar.add_cascade(label="Help", menu=helpMenu)

menuFrame = tk.Frame(win, bg="#D9D9D9", height=40, highlightthickness=5, highlightbackground="#D9D9D9", highlightcolor="#D9D9D9")
menuFrame.pack(side="top", fill="x")

new_btn = tk.Label(menuFrame, image=new_icon, bg="#D9D9D9")
new_btn.pack(side="left", padx=5, pady=2)
new_btn.bind("<Button-1>",new_file)
new_btn.bind("<Control-KeyPress-N>",new_file)

save_btn = tk.Label(menuFrame, image=save_icon, bg="#D9D9D9")
save_btn.pack(side="left", padx=5, pady=2)
save_btn.bind("<Button-1>", save)

open_btn = tk.Label(menuFrame, image=open_icon, bg="#D9D9D9")
open_btn.pack(side="left", padx=5, pady=2)
open_btn.bind("<Button-1>", open_file)

separator = tk.Label(menuFrame, image=separator_icon, bg="#D9D9D9")
separator.pack(side="left", padx=2, pady=2)


back_btn = tk.Label(menuFrame, image=back_icon, bg="#D9D9D9")
back_btn.pack(side="left", padx=5, pady=2)
back_btn.bind("<Button-1>", lambda e: back)

forward_btn = tk.Label(menuFrame, image=forward_icon, bg="#D9D9D9")
forward_btn.pack(side="left", padx=5, pady=2)
forward_btn.bind("<Button-1>", forward)

mainFrame = tk.Frame(win, bg="#D9D9D9")
mainFrame.pack(fill = "both", expand=True)

text_area = tk.scrolledtext.ScrolledText(mainFrame,
                                      font=("Times New Roman",
                                            12), undo=True, )

text_area.pack(fill="both", expand = True, padx=5, pady=0)
win.config(menu=menubar)


win.mainloop()