import requests
import json
import re
from lxml import etree

secret = YOUR_TOKEN_HERE
#secret =

def get_prodid_bol(isbn):
    """
    Helper function to get product id from API.
    """

    #REQUESTS
    arguments = {'q': isbn, 'apikey': secret, 'format': 'json'}
    r = requests.get('https://api.bol.com/catalog/v4/search/', params=arguments)

    data = r.json()["products"][0]
    product_id = data["id"]

    return product_id


def get_from_bol(isbn):
    """
    Returns a dict with information of the book.
    """

    product_id = get_prodid_bol(isbn)

    #REQUESTS
    arguments = {'apikey': secret, 'format': 'json'}
    r = requests.get('https://api.bol.com/catalog/v4/products/'  + product_id, params=arguments)

    data = r.json()["products"][0]





    title = data["title"]
    author = data["specsTag"]
    summary = data["summary"]

    years = re.findall("\d{4}", summary)
    if years:
        year = str(years[0])
    else:
        year = ""

    language, print_type  = summary.split("|")[0:2]

    language = language.strip()
    print_type = print_type.strip()

    authors = []
    publishers= []

    entity_data = data["entityGroups"]
    for item in entity_data:

        if item["title"] == "Auteurs":
            for author_entry in item["entities"]:
                author = author_entry["value"]
                authors.append(author)

        if item["title"] == "Uitgever":
            for publisher_entry in item["entities"]:
                publisher = publisher_entry["value"]
                publishers.append(publisher)

    for item in data["attributeGroups"][0]["attributes"]:

        if item["key"] == "DRUK":
            print_n = item["value"]


    for offer in data["offerData"]["offers"]:
        condition = offer["condition"]
        if condition == "Nieuw":
            price = str(offer["price"])
            price = price.replace(".", ",")

    author = ",".join(authors)
    publisher = ",".join(publishers)

    datadict = {
        "ISBN-13": isbn,
        "Title": title,
        "Authors": author,
        "Price": price,
        "Publisher": publisher,
        "Year": year,
        "Print": print_n,
        "Print_type": print_type,
        "Language": language
    }


    return datadict
