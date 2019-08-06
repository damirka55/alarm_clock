import pyglet
import time

def play_song(signal_name):
    ''' Plays signal. '''
    
    song = pyglet.resource.media(signal_name)
    song.play()

    pyglet.app.run()

def take_sleep_time():
    ''' Ask, how many time you want sleep. '''
    
    print("How many time you want sleep?")
    
    hours = input("How many hours you want sleep?")
    minutes = input("How many minutes you want sleep?")
    
    sleep_time = (hours * 60 + minutes) * 60
    
    return sleep_time 
    
