# PhotoEditor – Batch Image Processing (Python)

A Python script that batch-edits every image in a folder using Pillow and saves the results to an output folder.

## Features

For every image in `./images`, `editor.py`:

- Applies a sharpen filter
- Converts to grayscale
- Rotates by -90°
- Enhances contrast by a factor of 1.5
- Saves the result to `./edited` as `<name>_edited.<ext>`

## Tech Stack

Python · Pillow (PIL) · `os`

## Project Structure

```
editor.py   # batch processing script
```

## Getting Started

```bash
pip install Pillow
mkdir -p images edited     # put your images in ./images
python editor.py
```

### Example

```
images/photo1.jpg  ->  edited/photo1_edited.jpg
```

## Use Cases

- Automating repetitive image edits
- Preparing images for datasets
- Learning image manipulation with Pillow
