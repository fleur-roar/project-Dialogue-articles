import fitz

doc = fitz.open('D:/programming/project/anastasyevdg-147.pdf')
metad = doc.metadata
print(metad)
