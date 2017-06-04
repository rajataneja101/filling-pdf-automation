import PyPDF2
import os
from fdfgen import forge_fdf
pr=PyPDF2.PdfFileReader('input2.pdf','rb')
dict=pr.getFields()
print(dict)
r1=list(dict.keys())
i=0
print(r1)
for r in r1:
    print(str(i)+" "+r)
    i+=1
fields = [(r1[0],'rajt'),(r1[1],'tneja'),(r1[2],'dads'),(r1[4],'Yes'),(r1[3],'Yes')]
fdf = forge_fdf("",fields,[],[],[],[])
fdf_file = open("data.fdf","wb")
fdf_file.write(fdf)
fdf_file.close()
os.system('pdftk "input2.pdf" fill_form "data.fdf" output "output.pdf" flatten')
print("done")