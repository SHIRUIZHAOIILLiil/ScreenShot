from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

type ColorValue = (str | tuple[int, int, int] | tuple[int, int, int, int])


def save_image(image: Image.Image, filename: str = "screenshot.png") -> None:
    path = Path(__file__).parent / filename
    image.save(path)
    print(f"Screenshot saved to {path}")


def resize(image: Image.Image, width: int, height: int) -> Image.Image:
    image = image.resize((width, height))
    return image


def crop(image: Image.Image, start_x: int, start_y: int, end_x: int, end_y: int) -> Image.Image:
    left = min(start_x, end_x)
    right = max(start_x, end_x)

    top = min(start_y, end_y)
    bottom = max(start_y, end_y)

    left = max(0, min(image.width, left))
    right = max(0, min(image.width, right))

    top = max(0, min(image.height, top))
    bottom = max(0, min(image.height, bottom))

    image = image.crop((left, top, right, bottom))
    return image

def mosaic(image: Image.Image, box:tuple[int, int, int, int], tile_size: int) -> Image.Image:
    result = image.copy()
    region = result.crop(box)
    original_size = region.size

    small_width = max(1, region.width // tile_size)
    small_height = max(1, region.height // tile_size)

    region = region.resize((small_width, small_height))

    region = region.resize(
        original_size,
        Image.Resampling.NEAREST
    )

    result.paste(region, box)
    return result

def blur(image: Image.Image,box: tuple[int, int, int, int], radius: int) -> Image.Image:
    result = image.copy()

    region = result.crop(box)

    region = region.filter(ImageFilter.GaussianBlur(radius))

    result.paste(region, box)
    return result

def solid_cover(image: Image.Image, box:tuple[int, int, int, int], color: ColorValue) -> Image.Image:
    result = image.copy()
    region = result.crop(box)
    overlay = Image.new("RGBA", region.size, color)
    result.paste(overlay, box)
    return result

if __name__ == "__main__":
    image = Image.open("./screenshot.png")
    im = mosaic(image, (10, 10, 500, 500), 10)
    save_image(im, "mosaic.png")
    im = blur(image, (10, 10, 500, 500), 5)
    save_image(im, "blurred.png")
    im = solid_cover(image, (10, 10, 500, 500), (255, 0, 0, 10))
    save_image(im, "solid_cover.png")