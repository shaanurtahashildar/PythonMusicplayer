from tkinter import *
import pygame
root =Tk()
root.title('Shanur Music Player')
root.geometry("500x400")

pygame.mixer.init()
def play():
    pygame.mixer.music.load("F:/MUSIC/afgaan.mp3")
    pygame.mixer.music.play(loops=0)


play_button = Button(root, text="Play song" ,font=("Helvetica", 32), command=play)
play_button.pack(pady=20)


root.mainloop()