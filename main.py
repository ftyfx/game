import arcade 
SCREEN_WIDTH=960
SCREEN_HEIGHT=720
SCREEN_TITLE="хоррор"
class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
    def on_draw(self):
        self.clear()
window=MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
arcade.run()