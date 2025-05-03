# ASCII Art Generator 🎨

***Welcome to the ASCII Art Generator, a Python-based tool that transforms images into detailed ASCII art. This project combines image processing with creative text rendering to produce visually appealing text-based representations of your images, displayed elegantly in a web browser.***

## What You Need 🛠️

- **Python 3.8+** 🐍
- **Pillow** (PIL) library for image processing
- **Tkinter** for file selection (usually comes with Python)
- A modern web browser 🌐
- A terminal or command prompt
- An image file (e.g., .jpg, .png) to convert

## Folder Structure 📂

To keep things organized, structure your project folder like this:

```
ascii-art-generator/
├── main.py          # Main Python script
├── styles.css       # CSS for styling the HTML output
└── README.md        # This file
```

## Step-by-Step Setup & Run 🚀

### 1. Clone the Repository :

```bash
git clone https://github.com/Aryaan-Dev/ascii-art-generator-advanced.git
```

### 2. Create a Virtual Environment :

```bash
python -m venv .venv
```

Activate it:

- **Windows**: `.venv\Scripts\activate`
- **Mac/Linux**: `source venv/bin/activate`

You’ll see `(venv)` in your terminal when it’s active. 🎉

### 3. Install Dependencies 📦

Install the required Pillow library:

```bash
pip install Pillow
```

### 4. Add Your Image 🖼️

Place an image (e.g., `example.jpg`) in the project folder or have one ready on your computer. Supported formats include `.jpg`, `.png`, etc.

### 5. Run the Script 🏃‍♂️

Execute the main script:

```bash
python main.py
```

A file dialog will pop up. Select your image, and the script will:

- Convert the image to ASCII art
- Generate an HTML file (`art-by-aryaan.html`)
- Open the result in your default browser 🌐

### 6. Check the Output 🎨

Your browser will display the ASCII art with a sleek black background and white text, styled by `styles.css`. It’s like digital art in your terminal! 😎

Here’s what it might look like:

## Troubleshooting 🔍

Got issues? No worries, here’s how to fix common problems:

- **Error: "Unable to open image file"** 😕

  - Ensure the image file path is correct and the file isn’t corrupted.
  - Check if the image format is supported (e.g., `.jpg`, `.png`).
  - Try selecting the image again in the file dialog.

- **No file dialog appears** 🖥️

  - Tkinter might not be installed. Verify it by running `python -c "import tkinter"` in your terminal.
  - If it fails, install Tkinter:
    - **Windows/Mac**: Usually included with Python.
    - **Linux**: Run `sudo apt-get install python3-tk` (Ubuntu/Debian).

- **ASCII art looks weird or distorted** 🤔

  - Adjust the `new_width` value in `main.py` (line 33). Smaller values (e.g., 60) reduce width, larger ones (e.g., 100) increase it.
  - The aspect ratio is tuned for monospace fonts. If it’s still off, tweak the `0.65` in the `resize_image` function.

- **Browser doesn’t open or HTML looks plain** 🌐

  - Ensure `styles.css` is in the same folder as `art-by-aryaan.html`.
  - Check if the browser supports CSS (modern browsers like Chrome, Firefox, or Edge work best).
  - Verify the file path in the browser’s address bar starts with `file://`.

- **Pillow not found** 📚

  - Confirm you’re in the virtual environment (`(venv)` in terminal).
  - Reinstall Pillow: `pip install Pillow`.

## Tips for Best Results ✨

- Use high-contrast images for clearer ASCII art.
- Experiment with different `new_width` values in `main.py` to fit your screen.
- Want to customize? Edit `styles.css` to change colors or font sizes!

## License 📜

This project is licensed under the MIT License. See the LICENSE file for details.

## Made By 👨‍💻

Developed with care by **B P ARYAAN \[ARYAAN-DEV\].** Enjoy creating ASCII art and share your creations !
