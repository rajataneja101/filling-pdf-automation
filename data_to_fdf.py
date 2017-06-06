"""
This file will convert data from the pdf form to fdf file.
"""
import sys
import json
import pprint
from fdfgen import forge_fdf
import PyPDF2


def func2():
    """
    Converts pdf form to fdf data
    """
    pdf_file = input("PDF file")
    j_file = input("JSON file")
    prettyp = pprint.PrettyPrinter(indent=4)
    r_json = json.loads(open(j_file).read())
    prettyp.pprint(r_json)  # for checking the JSON data
    pdfread = PyPDF2.PdfFileReader(open(pdf_file, 'rb'), strict=False)  # reading the pdf file
    dictfields = pdfread.getFields()
    prettyp.pprint(dictfields)  # for checking the pdf fields
    r_list = list(dictfields.keys())  #fields dictonary to list
    i = 0
    # for loop to know the specific location of each field
    for value in r_list:
        print(str(i) + " " + value)
        i += 1
    i=0
    for value in dictfields:
        dictfields[value]=r_list[i]
        i += 1
    print(dictfields)
    fields = [(dictfields['Your_Last_Name'], r_json['lastName']),
              (dictfields['Your_First_Name'], r_json['firstName']),
              (dictfields['Date'], r_json['date']),
              (dictfields['CheckBox1'], 'Yes'),
              (dictfields['CheckBox2'], 'Yes'),
              (dictfields['CheckBox3'], 'Yes'),
              (dictfields['CheckBox4'], 'Yes'),
              (dictfields['CheckBox5'], 'Yes')
              ]  # inserting data into fields
    fdf = forge_fdf("", fields, [])  # updating the fields
    fdf_file = open("data.fdf", "wb")
    fdf_file.write(fdf)  # writing into a fdf file
    fdf_file.close()


def main():
    """
    main function to run the code
    """
    func2()
    prettyp = pprint.PrettyPrinter(indent=4)
    prettyp.pprint("Created fdf file")

if __name__ == '__main__':
    sys.exit(main())
