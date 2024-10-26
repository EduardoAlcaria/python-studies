from pygame import mixer
mixer.init()
mixer.music.load('song.mp3')
mixer.music.play()
input("Press enter to stop ")
mixer.music.stop()
