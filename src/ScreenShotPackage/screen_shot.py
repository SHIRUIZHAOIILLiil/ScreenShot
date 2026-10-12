from PIL import ImageGrab
from pathlib import Path


def grab():
    image = ImageGrab.grab()
    return image


if __name__ == "__main__":
    image = grab()
    path = Path(__file__).resolve().parent / "screenshot.png"
    image.save(path)
