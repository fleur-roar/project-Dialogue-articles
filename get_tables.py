import tabula
pdf_path = "D:/programming/project/anastasyevdg-147.pdf"
tables = tabula.read_pdf(pdf_path, pages = "all", multiple_tables = True)
print(tables)
