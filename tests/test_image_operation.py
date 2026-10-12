"""Tests for the image manipulation functions."""

from PIL import Image

from ScreenShotPackage import crop, resize, solid_cover


def test_resize_changes_size_without_changing_original():
    """resize returns the requested size and leaves its input unchanged."""
    image = Image.new("RGB", (4, 3), "white")

    result = resize(image, 2, 6)

    assert result.size == (2, 6)
    assert image.size == (4, 3)


def test_crop_accepts_coordinates_in_reverse_order():
    """crop normalises the start and end coordinates."""
    image = Image.new("RGB", (5, 4), "white")

    result = crop(image, 4, 3, 1, 1)

    assert result.size == (3, 2)


def test_crop_clamps_coordinates_to_image_edges():
    """crop keeps coordinates within the image bounds."""
    image = Image.new("RGB", (5, 4), "white")

    result = crop(image, -10, -10, 20, 20)

    assert result.size == image.size


def test_solid_cover_changes_only_the_selected_region():
    """solid_cover covers its box without modifying the input image."""
    image = Image.new("RGB", (4, 4), "white")

    result = solid_cover(image, (1, 1, 3, 3), "red")

    assert result.getpixel((1, 1)) == (255, 0, 0)
    assert result.getpixel((2, 2)) == (255, 0, 0)
    assert result.getpixel((0, 0)) == (255, 255, 255)
    assert image.getpixel((1, 1)) == (255, 255, 255)
