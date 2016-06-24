from flask import Flask, render_template, request, redirect, url_for

# Flask - class used to initialize an app
# render_template - render a template
# request - getting form data via POST request
# redirect - respond with location header
# url_for - shorthand for using function name instead of name of route

from flask_modus import Modus

# Modus - allows us to do method override via headers or query string
# with ?_method
from models import Book

# Seed some dummy data...
Book('Gatsby', 'Fitzy')

app = Flask(__name__)
modus = Modus(app)

@app.route('/')
def root():
    return redirect(url_for('index'))

# INDEX
@app.route('/books')
def index():
    return render_template('index.html')#, books = Book.book_list)

# NEW

@app.route('/books/new')
def new():
    return render_template('new.html')

# SHOW
@app.route('/books/<int:id>')
def show(id):
    return render_template('show.html')

# EDIT
@app.route('/books/<int:id>/edit')
def edit(id):
    return render_template('edit.html')
    

# CREATE
@app.route('/books', methods=["POST"])
def create():
    return redirect(url_for('index')) 

# UPDATE
@app.route('/books/<int:id>', methods=["PATCH"])
def update(id):
    return redirect(url_for('index')) 
    
# DELETE
@app.route('/books/<int:id>', methods=["DELETE"])
def destroy(id):
    return redirect(url_for('index')) 
    
if __name__ == '__main__':
    app.run(debug=True, port=3000)
