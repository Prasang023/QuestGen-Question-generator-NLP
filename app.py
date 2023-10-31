from flask import Flask, redirect, url_for, render_template, request, session, flash
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/saveData', methods=['POST'])
def saveData():
    output_string = StringIO()
    print(request.files)
    if 'testReport' in request.files:
        in_file= request.files['testReport']
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        print(output_string.getvalue())
        return f'<h1>File saved {in_file.filename}</h1>'
    else:
        return 'Not done'

if __name__=='__main__':
    app.run(debug=True)