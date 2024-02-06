from PyPDF2 import PdfFileReader, PdfFileWriter
from os import path
from sys import argv, exit

try:
    watermark = argv[1]
    document = argv[2]
except IndexError:
    exit("Please provide your watermark pdf file followed by your document pdf file...")

with open(document, 'rb') as file:
    reader = PdfFileReader(file)
    writer = PdfFileWriter()

    for page in range(reader.getNumPages()):
        content_page = reader.getPage(page)
        mediabox = content_page.mediaBox

        reader_stamp = PdfFileReader(watermark)
        image_page = reader_stamp.getPage(0)

        image_page.mergePage(content_page)
        image_page.mediaBox = mediabox
        writer.addPage(image_page)

directory, file_name = path.split(document)
with open(path.join(directory, f'wtr-{file_name}'), 'wb') as fp:
    writer.write(fp)

print("Sucessfully watermarked pdf document!")