#!/usr/bin/python3

from flask import jsonify, request, Response
from models.book import Book
from models.book_category import BookCategory
from models.member import Member
from api.v1.views import app_views


@app_views.route('/books', methods=['GET'], strict_slashes=False)
def get_all_books():
    """Returns all books"""
    books = [book.to_dict() for book in Book.query.all() if book]
    return jsonify(books)


@app_views.route('/books/', methods=['POST'], strict_slashes=False)
def add_book():
    """Returns newly created book"""
    book: Book = Book(**request.form.to_dict())
    book.save()
    return Response(status=201)


@app_views.route('/books/<int:book_id>', methods=['GET'], strict_slashes=False)
def get_single_book(book_id: int):
    """Returns book with the given id"""
    book: Book = Book.query.get_or_404(book_id, 'Book not found!')
    return jsonify(book)


@app_views.route('/books/<int:book_id>', methods=['PUT'], strict_slashes=False)
def update_book(book_id: int):
    """Returns updated book with new details"""
    book: Book = Book.query.get_or_404(book_id, 'Book not found!')
    book.update(**request.form.to_dict())
    return jsonify(book)


@app_views.route('/books/<int:book_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_book(book_id: int):
    """Deletes book"""
    book: Book = Book.query.get_or_404(book_id, 'Book not found!')
    book.delete()
    return Response(status=204)


@app_views.route('/books/search/', methods=['GET'], strict_slashes=False)
def search_books():
    """Returns book with the given search query"""
    query: str = request.args.get('q')
    books = Book.query.filter(Book.book_author.ilike(
        query) | Book.book_title.ilike(query)).all()
    books = [book.to_dict() for book in books if book]
    return jsonify(books)


@app_views.route('/books/available', methods=['GET'], strict_slashes=False)
def get_available_books():
    """Returns all books available to be rented"""
    books = Book.query.filter_by(Book.book_rent_status == 'Available').all()
    books = [book.to_dict() for book in books if book]
    return jsonify(books)


@app_views.route('/books/rented', methods=['GET'], strict_slashes=False)
def get_rented_books():
    """Returns all books already rented"""
    books = Book.query.filter_by(Book.book_rent_status == 'Rented').all()
    books = [book.to_dict() for book in books if book]
    return jsonify(books)


@app_views.route('/book_categories', methods=['GET'], strict_slashes=False)
def get_all_book_categories():
    """Returns all books with their set categories"""
    book_categories = BookCategory.query.all()
    books: dict = {}
    for book_cat in book_categories:
        books[book_cat.book_category_name] = book_cat.listed_books
    books = dict(
        sorted(
            books,
            key=lambda book_cat: book_cat.book_category_name))
    return jsonify(books)


@app_views.route('/book_categories/<int:book_category_id>',
                 methods=['GET'], strict_slashes=False)
def get_from_book_category(book_category_id: int):
    """Returns only books from the given category"""
    book_category = BookCategory.query.filter_by(
        BookCategory.book_category_id == book_category_id).one()
    books = book_category.listed_books
    return jsonify(books)


@app_views.route('/books/issue/<int:book_id>/to/<int:member_id>',
                 methods=['PUT'], strict_slashes=False)
def issue_book(member_id: int, book_id: int):
    """Returns updated information on member and book details after successful book rent"""
    member: Member = Member.query.filter_by(
        Member.member_id == member_id).one()
    book: Book = Book.query.filter_by(Book.book_id == book_id).one()
    if member and book:
        member.charge_book_fee(book.book_fee)
        book.issue_book_to(
            member_id,
            request.form.get('librarian_id'),
            request.form.get('duration'))
    return jsonify(book, member)


@app_views.route('/books/return/<int:book_id>/from/<int:member_id>',
                 methods=['PUT'], strict_slashes=False)
def return_book(member_id: int, book_id: int):
    """Returns updated information on member and book details after successful book return"""
    member: Member = Member.query.filter_by(member_id=member_id).one()
    book: Book = Book.query.filter_by(book_id=book_id).one()
    if member and book:
        book.return_book_from(member_id, request.form.get('librarian_id'))
    return jsonify(book, member)
