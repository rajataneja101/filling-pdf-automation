import PyPDF2
pdf = open('pdf_out.pdf', 'rb')
flObj = PyPDF2.PdfFileReader(pdf)
dict = flObj.getFields()
print(dict)
