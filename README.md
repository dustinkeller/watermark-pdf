# watermark-pdf
## Purpose
This Python script makes it quick and easy to add a watermark to all pages on a pdf file. This can be useful for specifying that a document's contents are private, not final, etc.

## Usage
Open the terminal, navigate to the directory containing this script, and run
```
python3 watermark.py /your/watermark/YOUR-FILENAME1-HERE.pdf/ /your/document/YOUR-FILENAME2-HERE.pdf/
```
Note that the watermarked pdf file will be named `wtr-YOUR-FILENAME2-HERE.pdf` and will be saved to the same directory as the document pdf file.  

## Dependencies
- [PyPDF2](https://pypdf2.readthedocs.io/en/latest/)