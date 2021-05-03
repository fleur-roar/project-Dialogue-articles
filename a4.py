import camelot

tables = camelot.read_pdf('D:/programming/project/anastasyevdg-147.pdf')
tables.export('foo.csv', f='json', compress=True)
