# ExifScraper 🛡️

A Python-based utility to strip forensic metadata (EXIF) from images. 

## The "McAfee" Problem
In 2012, John McAfee was located by authorities because a VICE photo contained embedded GPS coordinates. This project was built to demonstrate how simple it is to mitigate such "metadata leaks" by reconstructing images from raw pixel data.

## Features
- **True Stripping:** Unlike tools that simply "hide" tags, this script rebuilds the image from raw pixels, ensuring no "ghost data" remains.
- **Privacy by Design:** Focuses on Level 1 (EXIF/GPS) and Level 2 (Software Fingerprinting) data removal.
- **Lightweight:** Minimal dependencies using the Pillow library.

## How to Run
1. Clone the repo:
   `git clone https://github.com/YOUR_USERNAME/ExifScraper.git`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the tool:
   `python3 cleaner.py`

## Future Roadmap
- Integration with `ffmpeg` for video metadata scrubbing.
- Batch processing for entire folders.
- Adding Gaussian noise to disrupt Sensor Fingerprinting (PRNU).

## Disclaimer
Educational purposes only. Created as part of my portfolio for NHL Stenden University.
