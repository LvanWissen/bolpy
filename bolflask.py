#!/usr/bin/python

import random
from main import create_csv_from_isbn
from flask import Flask,render_template,request, make_response
app_bolpy = Flask(__name__)

app_bolpy.vars={}
app_bolpy.config["CACHE_TYPE"] = "null"

@app_bolpy.route('/',methods=['GET','POST'])
def index_bolpy():
    nquestions=5
    if request.method == 'GET':
        return render_template('bolpy.html',num=nquestions)
    else:
        #request was a POST
        app_bolpy.vars['isbn_list'] = request.form['isbn_list']


        isbnlist = app_bolpy.vars["isbn_list"].split()

        if isbnlist:
            create_csv_from_isbn(isbnlist, outfile="static/output.csv")
        else:
            return "No input."

        n_random = random.randint(1,99999999)

        return render_template('output.html', n_isbn=len(isbnlist), n_random=n_random)


@app_bolpy.route('/download', methods=['POST'])
def download():
    csv = open("static/output.csv").read()

    response = make_response(csv)
    response.headers["Content-Disposition"] = "attachment; filename=books.csv"
    return response

if __name__ == "__main__":
    app_bolpy.run(debug=True)
