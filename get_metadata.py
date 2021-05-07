import fitz

doc = fitz.open(filepath)
metad = doc.metadata
print(metad)
