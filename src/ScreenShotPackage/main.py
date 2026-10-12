from PySide6.QtWidgets import QApplication

from ScreenShotPackage.image_canvas import ImageCanvas
from ScreenShotPackage.screen_shot import grab

def main():
    app = QApplication([])

    image = grab()
    canvas = ImageCanvas(image)
    canvas.show()

    app.exec()



if __name__ == "__main__":
    main()