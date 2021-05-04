import tabula
pdf_path = "D:/programming/project/anastasyevdg-147.pdf"
x = tabula.read_pdf(pdf_path, pages = "all", multiple_tables = True)
print(x)
