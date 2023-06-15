# Library Management Web Application
A local library is in dire need of a web application to ease their work. The library management system must allow a librarian to track books and their quantity, books issued to members, book fees.

# Steps
1. Models
    - Book object
    - Book Genre/Category object
    - Library object
    - User object
    - Librarian object
    - Member object
2. Views / Routes
    - GET books
    - GET books/genres
    - GET books/genres {id}
    - GET PUT DELETE book {id}
    - POST book
    - GET books/search
    - GET books/issued
    - GET books/available
    - GET books/fees
    - GET libraries
    - GET PUT DELETE library {id}
    - POST library
    - GET librarians
    - GET PUT DELETE librarian {id}
    - POST librarian
    - GET members
    - GET PUT DELETE member {id}
    - POST member
3. Controllers / Operations
    - Create/Read/Update/Delete Book
    - Create/Read/Update/Delete Member
    - Create/Read/Update/Delete Librarian
    - Create/Read/Update/Delete Librarian
    - Issue a book to a member
    - Issue a book return from a member
    - Search for a book by name and author
    - Charge a rent fee on book returns
    - Make sure a member’s outstanding debt is not more than KES.500
4. UI
5. Testing