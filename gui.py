import multiprocessing
import time
import os

from pygame import mixer
from PyQt5 import QtWidgets, uic, QtGui
from home import get_link, get_audio, get_thumbnail
from Player import AudioPlayer

queue = multiprocessing.Queue()
queue.put([])


class Ui(QtWidgets.QMainWindow):
    """Main class that initiates the gui"""

    def __init__(self):
        # mixer.init()
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi("main.ui", self)  # Load the .ui file

        self.player = AudioPlayer()

        self.play = -1
        self.search.clicked.connect(
            lambda x: print("Please enter a song")
            if self.text_b.text() == ""
            else self.Search(self.text_b.text())
        )
        self.Play.clicked.connect(lambda: self.PlayPause())
        self.show()  # Show the GUI

        # create previously played volume labels
        # with open("last.playlist", "r") as file:
        #     self.

    def PlayPause(self) -> None:
        """Function linked to play pause button"""
        if self.play == 1:
            # mixer.music.pause()
            self.player.pause()
            self.play = 0
        elif self.play == 0:
            # mixer.music.unpause()
            self.player.play()
            self.play = 1

    def Search(self, name) -> None:
        """Function linked to search button"""
        self.p_bar.setValue(50)
        id, NAME = get_link(name)
        URL = "https://music.youtube.com/watch?v=" + id
        print("done")

        if not (os.path.isfile(NAME + ".mp3")):
            # x = multiprocessing.Process(target=get_audio, args=(URL, NAME, self.player, True))
            # y = multiprocessing.Process(target=get_thumbnail, args=(id, NAME))
            # x.start()
            # y.start()
            # for i in range(50, 99, 3):
            #     time.sleep(1)
            #     self.p_bar.setValue(i)
            # x.join()
            # y.join()
            self.p_bar.setValue(100)
            x=get_audio(URL, NAME, True)
            get_thumbnail(id, NAME)
            self.image_label.setPixmap(QtGui.QPixmap(NAME + ".jpg"))

        else:
            self.image_label.setPixmap(QtGui.QPixmap(NAME + ".jpg"))

        # mixer.music.load(NAME + ".mp3")
        # mixer.music.play()
        self.player.set_file(x)
        self.player.play()
        self.current_playing.setText(NAME)
        self.play = 1
        self.p_bar.setValue(0)

        # write the file in history
        with open("played.hist", "a", encoding="UTF-8") as file:
            file.write(NAME + " : " + id + "\n")


app = QtWidgets.QApplication([])
window = Ui()
app.exec_()
