import fitz

doc = fitz.open("D:/programming/project/chuikovaoiu-051.pdf")
mytext = ''
for page in doc:
    mytext += page.get_text("text")
print(mytext) 
