from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
root =Tk()
root.title('Shanur Music Player')
root.geometry("600x600")

#initilizing pygame
pygame.mixer.init()

# play status
def play_status():
    current_time=pygame.mixer.music.get_pos()/1000
    current_time = time.strftime('%M:%S', time.gmtime(current_time))
    # get song legth
    # get_song = songs_list_box.curselection()
    song = songs_list_box.get(ACTIVE)

    # song len
    song_mut = MP3(song)
    song_len = song_mut.info.length


    time_conv = time.strftime('%M:%S', time.gmtime(song_len))
    status_bar.config(text=f'Time : {current_time} of {time_conv}')
    status_bar.after(1000, play_status)

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

def remove_songs():
    songs_list_box.delete(ANCHOR)
    pygame.mixer.music.stop()

# remove all songs
def remove_all():
    pygame.mixer.music.stop()
    songs_list_box.delete(0,END)

# next song
def forword():
    next = songs_list_box.curselection()
    print(next)
    next=next[0]+1
    song = songs_list_box.get(next)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #clear selection
    songs_list_box.select_clear(0, END)
    #Active new ong
    songs_list_box.activate(next)
    songs_list_box.select_set(next,last=None)

# previous song
def previous():
    back = songs_list_box.curselection()
    print(back)
    back=back[0]-1
    song = songs_list_box.get(back)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #clear selection
    songs_list_box.select_clear(0, END)
    #Active new ong
    songs_list_box.activate(back)
    songs_list_box.select_set(back,last=None)
def play():
    song = songs_list_box.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    play_status()

def stop():
    pygame.mixer.music.stop()
    songs_list_box.select_clear(ACTIVE)
    status_bar.config(text='')

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
back_btn = Button(control_panel_frame, image=back_btn_icon, borderwidth=0, command=previous)
next_btn = Button(control_panel_frame, image=next_btn_icon, borderwidth=0, command=forword)
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


# remove songs
remove_songs_menu = Menu(My_Menu)
My_Menu.add_cascade(label="remove songs", menu=remove_songs_menu)
remove_songs_menu.add_command(label="Delete songs from playlist", command=remove_songs)
remove_songs_menu.add_command(label="Clear playlist", command=remove_all)


status_bar = Label(text="", bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X,side=TOP, ipady=2)
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