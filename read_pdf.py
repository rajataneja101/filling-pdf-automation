import PyPDF2

import os
from fdfgen import forge_fdf
pr=PyPDF2.PdfFileReader('r1.pdf','rb')
dict=pr.getFields()
print(dict)
r1=list(dict.keys())
print(r1)
print(dict.keys())
fields = [(r1[0],'rajt'),(r1[1],'tneja'),(r1[2],'Rjat'),(dict['Language 1 Check Box'],'On'),(dict['Driving License Check Box'],'<</T(c1)/V(On)>>')]
fdf = forge_fdf("",fields,[],[],[],[])
fdf_file = open("data.fdf","wb")
fdf_file.write(fdf)
fdf_file.close()


os.system('pdftk "r1.pdf" fill_form "data.fdf" output "output.pdf" flatten')
print("done")