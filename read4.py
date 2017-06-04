import PyPDF2
input_file = PyPDF2.PdfFileReader('input.pdf', 'rb')
d = input_file.getFields()
print(d)
d['Given Name Text Box'] = 'xzxz' #as an example
print(d)
output_file = PyPDF2.PdfFileWriter()
output_file.appendPagesFromReader(input_file)
output_file.updatePageFormFieldValues(output_file.getPage(0),d)
with open('pdf_out.pdf', 'wb') as f:
    output_file.write(f)
