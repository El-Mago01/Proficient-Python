from PyPDF2 import PdfReader,PdfWriter, Transformation

reader = PdfReader("resume.pdf")
writer = PdfWriter()

page = reader.pages[2]
print(page.extract_text())

page_1 = reader.pages[0]
page_4 = reader.pages[3]



writer.add_page(page_1)
writer.add_page(page_4)
writer.pages[1].rotate(-90)


writer.write("adjusted.pdf")


# Adding a watermark to all pages of the resume
pdf_result="watermarked_resume.pdf"
def watermark():
    page_indices = list(range(0, len(reader.pages)))

    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        # You need to load it again, as the last time it was overwritten
        reader_stamp = PdfReader("watermark.pdf")
        image_page = reader_stamp.pages[0]

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)

watermark()
