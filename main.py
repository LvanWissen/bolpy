"""Use Bol.com catalogue as a provider for ISBN-data. """

import csv
from functions import *

with open("isbn.txt") as infile:
    data = infile.read()
    isbnlist = data.split()

with open('output.csv', 'w', ) as csvfile:
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

    for isbn in isbnlist:
        datadict = get_from_bol(isbn)
        writer.writerow(datadict)



# # First try the isbnlib service (Google Books and WCat)

# meta_data = isbnlib.meta(isbn2)

# if meta_data == None:
#     meta_data = get_from_bol(isbn)









