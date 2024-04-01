# pydub requires simpleaudio, ffmpeg
from pydub import AudioSegment
from pydub.playback import play

class AudioPlayer:
    def __init__(self):
        self.audio=0
        self.playing = False
        self.position = 0  # Track the position where playback was paused

    def set_file(self, file_path):
        """set the audio file to play"""
        self.audio = AudioSegment.from_file(file_path)

    def play(self): 
        if not self.playing and self.audio:
            self.playing = True
            self.audio = self.audio[self.position :]  # Start from the paused position
            play(self.audio)

    def pause(self):
        if self.playing and self.audio:
            self.playing = False
            self.position = (
                len(self.audio) - len(self.audio) % 1000
            )  # Round down to nearest second
            self.audio = self.audio[: self.position]
