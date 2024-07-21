from tkinter import *
import pygame
from tkinter import filedialog
root =Tk()
root.title('Shanur Music Player')
root.geometry("600x600")

#initilizing pygame
pygame.mixer.init()

# add songs playlist funstion
def add_songs():
    song = filedialog.askopenfilename(initialdir="F:/", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    print(song)
    songs_list_box.insert(END, song)


def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir="F:/", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    print(songs)
    for song in songs:
        songs_list_box.insert(END, song)


    # song list box
# song list box
songs_list_box = Listbox(bg="white", fg="black", width=60, selectbackground="gray", selectforeground="black")
songs_list_box.pack(pady=20)




def play():
    song = songs_list_box.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    songs_list_box.select_clear(ACTIVE)

# create global variable fot pause
global paused
paused=False
def pause(is_paused):
    global paused
    paused = is_paused
    if paused :
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

# controlls icons
back_btn_icon = PhotoImage(file="icons/back.png")
next_btn_icon = PhotoImage(file="icons/next.png")
play_btn_icon = PhotoImage(file="icons/play.png")
pause_btn_icon = PhotoImage(file="icons/pause.png")
stop_btn_icon = PhotoImage(file="icons/stop.png")



# create contral panel frame
control_panel_frame = Frame(root)
control_panel_frame.pack()

# controll Buttons
back_btn = Button(control_panel_frame, image=back_btn_icon, borderwidth=0)
next_btn = Button(control_panel_frame, image=next_btn_icon, borderwidth=0)
play_btn = Button(control_panel_frame, image=play_btn_icon, borderwidth=0, command=play)
pause_btn = Button(control_panel_frame, image=pause_btn_icon, borderwidth=0, command=lambda: pause(paused))
stop_btn = Button(control_panel_frame, image=stop_btn_icon, borderwidth=0, command=stop)

# grids
back_btn.grid(row=0, column=0, padx=10)
next_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)


# menu
My_Menu = Menu()
root.config(menu=My_Menu)

#Menu->add songs
add_song=Menu(My_Menu)
My_Menu.add_cascade(label="Add Songs", menu=add_song)
add_song.add_command(label="Add one song to playlist", command=add_songs )


# added mutliple songs
add_song.add_command(label="Add Many song to playlist", command=add_many_songs )

# def play():
#     pygame.mixer.music.load("F:/MUSIC/afgaan.mp3")
#     pygame.mixer.music.play(loops=0)
#
#
# play_button = Button(root, text="Play song" ,font=("Helvetica", 32), command=play)
# play_button.pack(pady=20)
#
# stop_button = Button(root, text="Stop" ,font=("Helvetica", 32), command=stop)
# stop_button.pack(pady=20)

root.mainloop()