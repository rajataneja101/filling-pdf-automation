import PyPDF2
import os
from fdfgen import forge_fdf
pr=PyPDF2.PdfFileReader('r1.pdf','rb')
dict=pr.getFields()
r1=list(dict.keys())
print(r1)
print(dict.keys())
fields = [(r1[0],'rajt'),(r1[1],'tneja'),(r1[2],'Rjat'),(r1[9],'checked')]
fdf = forge_fdf("",fields,[],[],[],[])
fdf_file = open("data.fdf","wb")
fdf_file.write(fdf)
fdf_file.close()


os.system('pdftk "r1.pdf" fill_form "data.fdf" output "output.pdf" flatten')
print("done")