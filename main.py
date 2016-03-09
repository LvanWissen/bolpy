#Use the Bol.com catalogue as a provider for ISBN-data.

import csv
from functions import get_from_bol

# with open("isbn.txt") as infile:
#     data = infile.read()
#     isbnlist = data.split()

def create_csv_from_isbn(isbnlist, outfile="output.csv"):

    with open(outfile, 'w') as csvfile:
        fieldnames = [   "ISBN-13",
                         "Title",
                         "Authors",
                         "Price",
                         "Publisher",
                         "Year",
                         "Print",
                         "Print_type",
                         "Language"
                     ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel', lineterminator='\n', delimiter=';')

        writer.writeheader()

        count = 1

        for isbn in isbnlist:



            try:
                datadict = get_from_bol(isbn)
                writer.writerow(datadict)
            except:
                writer.writerow({"ISBN-13": isbn})











