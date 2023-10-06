import mysql.connector
import sys


## Connect to MySQL database
connection = mysql.connector.connect(
    host = "localhost",
username = "root",
password = "%TGBnhy6",
database = "bookstore"
)

## Check connection
if (connection!=200) :
    print("Connection failed: ")


## Function to retrieve all books from the database
def getBooks() :
    global connection
    query = "SELECT * FROM books"
    result=connection.cursor()
    result.execute(query)
    books=result.fetchall()
    return books

## Function to add a new book to the database
def addBook(title, author, price) :
    global connection
    result=connection.cursor()
    query = "INSERT INTO books (title, author, price) values (%s,%s)"
    VALUES =('$title', '$author', '$price')
    result.execute(query,VALUES)


## Function to delete a book from the database
def deleteBook(bookId) :
    global connection
    result=connection.cursor()
    query = "DELETE FROM books WHERE id = $bookId"
    result.execute(query)


## Function to update a book in the database
def updateBook(bookId, title, author, price) :
    global connection
    query = "UPDATE books SET title = '$title', author = '$author', price = '$price' WHERE id = $bookId"
    result=connection.cursor()
    result.execute(query)


## Usage Examples
## Fetch all books

books = getBooks()
for book in books:
    print( "Title: " + book['title'])
    print( "Author: " + book['author'] + "<br>")
    print( "Price: $" +book['price'] + "<br><br>")


## Add a book
addBook("New Book", "John Doe", 19.99)

## Delete a book
deleteBook(3)

## Update a book
updateBook(1, "Updated Book", "Jane Smith", 24.99)

## Close database connection
mysqli_close(connection)
