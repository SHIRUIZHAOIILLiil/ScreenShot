from PIL import Image
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

class ImageCanvas(QLabel):
    def __init__(self, image: Image.Image):
        super().__init__()
        self.image = image

        qt_image = ImageQt(image.convert("RGBA"))
        pixmap = QPixmap.fromImage(qt_image)

        self.setPixmap(pixmap)



