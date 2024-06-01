from PIL import ImageGrab
import os
import datetime


class GameUtilities:

    def __init__(self, boardContext):
        self.boardContext = boardContext

    
    def save_screenshot(self):
        # Se asegura que exista la carpeta
        os.makedirs('history', exist_ok=True)

        x0 = self.boardContext.root.winfo_rootx() + self.boardContext.buttons[0].winfo_x()
        y0 = self.boardContext.root.winfo_rooty() + self.boardContext.buttons[0].winfo_y()
        x1 = x0 + 3 * self.boardContext.buttons[0].winfo_width()
        y1 = y0 + 3 * self.boardContext.buttons[0].winfo_height()

        # toma y guarda la captura
        img = ImageGrab.grab(bbox=(x0, y0, x1, y1))
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        img.save(f'history/game_{timestamp}.png')
        print(f"Saved screenshot as 'history/game_{timestamp}.png'")