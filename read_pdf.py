import PyPDF2
import os
from fdfgen import forge_fdf
import json
import sys
def main():
    pdf_file="input2.pdf"
    j_file="customer.json"
    r2= json.loads(open(j_file).read()) #loading json data into a object basically a dictonary
    print(r2) #for checking the JSON data
    pr = PyPDF2.PdfFileReader(open(pdf_file, 'rb'), strict=False) #reading the pdf file
    dict = pr.getFields()
    print(dict) #for checking the pdf fields
    r1 = list(dict.keys()) #converting pdf fields dictonary to list for easy accessibility
    i = 0
    # for loop to know the specific location of each field
    for r in r1:
        print(str(i) + " " + r)
        i += 1
    fields = [(r1[0], r2['lastName']), (r1[1], r2['firstName']), (r1[2], r2['date']), (r1[4], 'Yes'), (r1[5], 'Yes'),
              (r1[3], 'Yes')] #inserting data into fields
    fdf = forge_fdf("", fields, [], [], [], []) #updating the fields
    fdf_file = open("data.fdf", "wb")
    fdf_file.write(fdf)#writing into a fdf file
    fdf_file.close()
    os.system('pdftk "'+pdf_file+'" fill_form "data.fdf" output "output.pdf" flatten') #system command to update the file and give the output
    print("done")

if __name__ == '__main__':
    sys.exit(main())