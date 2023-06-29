#!/usr/bin/python3

from flask import render_template, jsonify, request, redirect, session
from models.book import Book
from models.book_category import BookCategory
from models.member import Member
from api.v1.views import app_views
from werkzeug.exceptions import HTTPException, NotFound


@app_views.route('/books', methods=['GET'], strict_slashes=False)
def get_all_books():
    """Returns all books"""
    try:
        books = Book.query.all()
        return jsonify(books)
    except HTTPException:
        return render_template('error.html')


@app_views.route('/books/', methods=['POST'], strict_slashes=False)
def add_book():
    """Returns newly created book"""
    book: Book = Book(request.form)
    book.save()
    return jsonify(book)


@app_views.route('/books/{book_id:int}', methods=['GET'], strict_slashes=False)
def get_single_book(book_id: int):
    """Returns book with the given id"""
    book: Book = Book.query(book_id=book_id).one()
    return jsonify(book)


@app_views.route('/books/{book_id:int}', methods=['PUT'], strict_slashes=False)
def update_book(book_id: int):
    """Returns updated book with new details"""
    book: Book = Book.query(book_id=book_id).one()
    book.update(request.form)
    return jsonify(book)


@app_views.route('/books/{book_id:int}',
                 methods=['DELETE'], strict_slashes=False)
def delete_book(book_id: int):
    """Deletes book"""
    book: Book = Book.query(book_id=book_id).one()
    book.delete()
    return redirect('/', 301)


@app_views.route('/books/search', methods=['GET'], strict_slashes=False)
def search_books():
    """Returns book with the given search query"""
    books = Book.query(filter_by=request.data).all()
    return jsonify(books)


@app_views.route('/books/', methods=['GET'], strict_slashes=False)
def get_available_books():
    """Returns all books available to be rented"""
    books = Book.query(filter_by={'book_rent_status': 'Available'}).all()
    return jsonify(books)


@app_views.route('/books/', methods=['GET'], strict_slashes=False)
def get_rented_books():
    """Returns all books already rented"""
    books = Book.query(filter_by={'book_rent_status': 'Rented'}).all()
    return jsonify(books)


@app_views.route('/books/', methods=['GET'], strict_slashes=False)
def get_book_fees():
    """Returns all books with their set fees"""
    books: list = list(Book.query().all())
    books.sort(key=lambda book: book.book_fee)
    return jsonify(books)


@app_views.route('/books/', methods=['GET'], strict_slashes=False)
def get_all_book_categories():
    """Returns all books with their set categories"""
    book_categories = BookCategory.query().all()
    books: dict = {}
    for book_cat in book_categories:
        books[book_cat.book_category_name] = book_cat.listed_books
    books = dict(
        sorted(
            books,
            key=lambda book_cat: book_cat.book_category_name))
    return jsonify(books)


@app_views.route('/books/{book_category_id:int}',
                 methods=['GET'], strict_slashes=False)
def get_from_book_category(book_category_id: int):
    """Returns only books from the given category"""
    book_category = BookCategory.query().filter_by(
        book_category_id=book_category_id).one()
    books = book_category.listed_books
    return jsonify(books)


@app_views.route('/books/issue/{member_id:int}/{book_id:int}',
                 methods=['PUT'], strict_slashes=False)
def issue_book(member_id: int, book_id: int):
    """Returns updated information on member and book details after successful book rent"""
    member: Member = Member.query.filter_by(member_id=member_id).one()
    book: Book = Book.query.filter_by(book_id=book_id).one()
    if member and book:
        member.charge_book_fee(book.book_fee)
        book.issue_book_to(
            member_id,
            request.form.get('librarian_id'),
            request.form.get('duration'))
    return jsonify(book, member)


@app_views.route('/books/return/{member_id:int}/{book_id:int}',
                 methods=['PUT'], strict_slashes=False)
def return_book(member_id: int, book_id: int):
    """Returns updated information on member and book details after successful book return"""
    member: Member = Member.query.filter_by(member_id=member_id).one()
    book: Book = Book.query.filter_by(book_id=book_id).one()
    if member and book:
        book.return_book_from(member_id, request.form.get('librarian_id'))
    return jsonify(book, member)
