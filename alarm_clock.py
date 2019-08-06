import pyglet

def play_song(signal_name):
    ''' Plays signal. '''
    
    song = pyglet.resource.media(signal_name)
    song.play()

    pyglet.app.run()
