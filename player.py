from tkinter import *
from pygame import mixer
from tkinter import filedialog, PhotoImage, messagebox
from PIL import Image, ImageTk

root = Tk()
mixer.init()

def open_image(name):
    width = 40
    height = 40
    img = Image.open(name)
    img = img.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

def play():
    song = song_box.get(ACTIVE)
    if song == '':
        messagebox.showerror("Exception", "Choose a song to continue")
        return
    mixer.music.load(song)
    mixer.music.play()
    song_state["text"] = "Playing"


def stop():
    mixer.music.stop()
    song_box.select_clear(ACTIVE)
    song_state["text"] = "Stopped"


def openfile():
    song = filedialog.askopenfilename(title='Add a song',
                                      filetypes=(("mp3 Files", "*.mp3"),))
    song_box.insert(END, song)


def openfolder():
    songs = filedialog.askopenfilenames(title='Add songs',
                                        filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        song_box.insert(END, song)


def pause():
    if song_state['text'] == "Paused":
        mixer.music.unpause()
        song_state['text'] = "Playing"
    else:
        mixer.music.pause()
        song_state['text'] = "Paused"


def next_song():
    now_s = song_box.curselection()
    if now_s == ():
        messagebox.showerror("Exception", "You should choose a song to continue")
        return

    next_s = now_s[0] + 1
    song = song_box.get(next_s)

    if song == '':
        messagebox.showerror("Exception", "You don't have enough songs in your playlist")
        return

    mixer.music.load(song)
    mixer.music.play()

    song_box.selection_clear(0, END)
    song_box.activate(next_s)
    song_box.selection_set(next_s, last=None)


def prev_song():
    now_s = song_box.curselection()
    if now_s == ():
        messagebox.showerror("Exception", "You should choose a song to continue")
        return

    prev_s = now_s[0] - 1
    song = song_box.get(prev_s)
    if song == '':
        messagebox.showerror("Exception", "You don't have enough songs in your playlist")
        return

    mixer.music.load(song)
    mixer.music.play()

    song_box.selection_clear(0, END)
    song_box.activate(prev_s)
    song_box.selection_set(prev_s, last=None)

master_frame = Frame(root, bg='#E8F8FD')
master_frame.pack()

info_frame = Frame(master_frame, bg='#E8F8FD')
info_frame.grid(row=0, column=0)

controls_frame = Frame(master_frame, bg='#E8F8FD')
controls_frame.grid(row=1, column=0)

file_frame = Frame(master_frame, bg='#E8F8FD')
file_frame.grid(row=0, column=5)

song_state = Label(info_frame, width=60, text='Stopped', font='Arial 8 bold', bg='#E8F8FD')
song_state.grid(row=0, column=0)

song_box = Listbox(info_frame, width=60, selectbackground="#06BCF5")
song_box.grid(row=1, column=0)

#Create control buttons
pause_img = open_image("img/pause.jpg")
play_img = open_image("img/play.jpg")
stop_img = open_image("img/stop.jpg")
next_img = open_image("img/next.jpg")
prev_img = open_image("img/prev.jpg")

back_button = Button(controls_frame, image=prev_img, width=20, height=20, command=prev_song)
forward_button = Button(controls_frame, image=next_img, width=20, height=20, command=next_song)
play_button = Button(controls_frame, image=play_img, width=20, height=20, command=play)
pause_button = Button(controls_frame, image=pause_img, width=20, height=20, command=pause)
stop_button = Button(controls_frame, image=stop_img, width=20, height=20, command=stop)

back_button.grid(row=0, column=0, padx=10, pady=10)
forward_button.grid(row=0, column=1, padx=10, pady=10)
play_button.grid(row=0, column=2, padx=10, pady=10)
pause_button.grid(row=0, column=3, padx=10, pady=10)
stop_button.grid(row=0, column=4, padx=10, pady=10)

openfile_button = Button(file_frame, width=15, text="Open file", command=openfile, bg="#65D3F6")
openfolder_button = Button(file_frame, width=15, text="Open folder", command=openfolder, bg="#65D3F6")

openfile_button.grid(row=0, column=0, padx=10)
openfolder_button.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()