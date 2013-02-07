from flask import Flask, render_template, url_for
import bookdb

app = Flask(__name__)

db = bookdb.BookDB()


@app.route('/')
def books():
    inst = bookdb.BookDB()
    books = inst.titles()
    return render_template('book_list.html', books=books)
    # put code here that provides a list of books to a template named 
    # "book_list.html"
    #pass


@app.route('/book/<book_id>/')
def book(book_id):
    inst = bookdb.BookDB()
    book = inst.title_info(book_id)
    return render_template('book_detail.html', book=book)
    # put code here that provides the details of a single book to a template 
    # named "book_detail.html"
    #pass


if __name__ == '__main__':
    app.run(debug=True)
