import PyPDF2
import os
from fdfgen import forge_fdf
fields = [('Given Name Text Box','rajat'),('Family Name Text Box','taneja'),('House nr Text Box','Rajat')]
fdf = forge_fdf("",fields,[],[],[],[])
fdf_file = open("data.fdf","wb")
fdf_file.write(fdf)
fdf_file.close()
pr=PyPDF2.PdfFileReader('r1.pdf','rb')
print(pr.isEncrypted)
print(pr.getDocumentInfo())
print(pr.getFields())
print(pr.getFormTextFields())
os.system('pdftk "r1.pdf" fill_form "data.fdf" output "output.pdf" flatten')
print("done")