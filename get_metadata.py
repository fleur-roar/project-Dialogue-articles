import fitz

doc = fitz.open('D:/programming/project/anastasyevdg-147.pdf')
x = doc.metadata
print(x)
