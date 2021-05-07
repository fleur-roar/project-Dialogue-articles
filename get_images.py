import fitz

doc = fitz.open(filepath)
for page in doc:
    images = page.get_images()
    if images:
        counter = 0
        for im in images:
            counter += 1
            pix = fitz.Pixmap(doc, im[0])
            pix.writeImage('image' + str(counter) + '.png', output=None)

