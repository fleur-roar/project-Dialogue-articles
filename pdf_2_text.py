import pdfminer.high_level

pdfdir = 'D:/programming/project/anastasyevdg-147.pdf'
textpdf = pdfminer.high_level.extract_text(pdfdir)
print(textpdf)

contents = []
for line in textpdf.split('\n'):
    if line.startswith('1.') or line.startswith('2.') or line.startswith('3.') or line.startswith('4.') or line.startswith('5.') or line.startswith('6.') or line.startswith('7.') or line.startswith('8.') or line.startswith('9.'):
        contents.append(line)
print(contents)
