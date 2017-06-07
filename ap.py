import argparse
parser = argparse.ArgumentParser()
parser.add_argument("pdf_file", help="display a square of a given number",
                    type=str)
parser.add_argument("json_file", help="display a square of a given number",
                    type=str)
args = parser.parse_args()
print("PDF File:"+args.pdf_file)
print("JSON File:"+args.json_file)