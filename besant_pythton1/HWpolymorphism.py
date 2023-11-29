class music:
    def play_music(self):
        print("music is playing")
    def pause_music(self):
        print("music is paused")
    def next_music(self):
        print("playing next song")
class wynk(music):
    def pause_music(self):
        print("music is paused in wynk")
    def next_music(self):
        print("playing next song in wynk")
    def unliked_song(self):
        print("This is unlinked song in wynk")
class spotify(music):
    def pause_music(self):
        print("music is paused in spotify")
    def next_music(self):
        print("playing next song in spotify")
    def liked_song(self):
        print("This is liked song in spotify")
class jio_play(music):
    def pause_music(self):
        print("music is paused in jio_play")
    def next_music(self):
        print("playing next song in jio_play")
    def love_song(self):
        print("This is love song in jio_play")
def player(ref):
    ref.play_music()
    ref.pause_music()
    ref.next_music()
    if type(ref) == wynk:
        ref.unliked_song()
    if type(ref) == spotify:
        ref.liked_song()
    if type(ref) == jio_play:
        ref.love_song()
b = wynk()
c = spotify()
d = jio_play()
player(b)
player(c)
player(d)