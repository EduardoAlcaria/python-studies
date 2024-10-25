from pygame import mixer
mixer.init()
mixer.music.load(r"C:\Users\eduar\OneDrive\Área de Trabalho\PROGRAMING\python studies\song.mp3")
mixer.music.play()
input("Press enter to stop ")
mixer.music.stop()