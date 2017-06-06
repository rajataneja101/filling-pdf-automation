"""
This program dumps fdf data to form
"""
import os
import sys


def final_step():
    """
    function to give the output file
    """
    pdf_file = input("pdf_file")
    fdf_file = input("fdf file")
    os.system('pdftk "' + pdf_file + '" fill_form "' + fdf_file +
              '" output "output.pdf" flatten')  #command give the output


def main():
    """
    calling the function
    """
    final_step()
    print("done")

if __name__ == '__main__':
    sys.exit(main())
