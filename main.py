import os, webbrowser
from tkinter import filedialog
from PIL import Image

# Expanded ASCII characters for different intensity levels
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """Resize the image while maintaining aspect ratio."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.65)  # Adjust for font aspect ratio
    return image.resize((new_width, new_height))

def grayify(image):
    """Convert the image to grayscale."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Convert each pixel to an ASCII character."""
    pixels = image.getdata()
    # Map pixel intensity (0-255) to ASCII_CHARS
    ascii_str = "".join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    return ascii_str

def image_to_ascii(image_path, new_width=80):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {e}")
        return None

    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)
    ascii_width = image.width
    ascii_art = "\n".join(ascii_str[i:i + ascii_width] for i in range(0, len(ascii_str), ascii_width))
    return ascii_art

file_path = filedialog.askopenfilename()

# Reduce the width of the ASCII art
ascii_art = image_to_ascii(file_path, new_width=80)

if ascii_art:
    # Link to external CSS file
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles.css">
        <title>ASCII Art</title>
    </head>
    <body>
        <pre>{}</pre>
    </body>
    </html>
    """.format(ascii_art)

    with open("art-by-aryaan.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    webbrowser.open(f'file://{os.path.abspath("art-by-aryaan.html")}')