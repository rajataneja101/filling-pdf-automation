import PyPDF2
pr=PyPDF2.PdfFileReader('input.pdf','rb')
dict=pr.getFields()
print(dict)
dict['Given Name Text Box']='rajat'
print(dict)
d=pr.getPage(0)
outputstream = open('input.pdf', 'wb+')
pw=PyPDF2.PdfFileWriter()
pw.updatePageFormFieldValues(d,dict['Given Name Text Box'])
pw.write(outputstream)
outputstream.close()