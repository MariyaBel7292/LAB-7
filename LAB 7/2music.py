'''
here is 4 songs, 
use "Left" for next song;
use " Right" for previous song;
and "Space" for stop/play.
'''


import os, sys, pygame
pygame.init()

s_w = 600
s_h = 600
screen = pygame.display.set_mode((s_w, s_h), pygame.RESIZABLE)
done = False
pygame.display.set_caption("WorldwileMusic")


icon_image = pygame.image.load("C:\\Users\\User\\Desktop\\images.jpeg")
pygame.display.set_icon(icon_image)

music_listen = "ту-туру-ру-ту-ру-ру"
playlist = os.listdir(music_listen)
current_music = 0
is_play = False

def play_music(music):
    pygame.mixer.music.load(os.path.join(music_listen, playlist[music]))
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_music
    current_music = (current_music + 1) % len(playlist)
    play_music(current_music)

def prev_track():
    global current_music
    current_music = (current_music - 1) % len(playlist)
    play_music(current_music)   

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not is_play:
                    play_music(current_music)
                    is_play = True
                else:
                    stop_music()
                    is_play = False
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                prev_track()


pygame.display.flip()

pygame.quit()



