import mysql.connector

import mysql.connector

# Connect to MySQL Database
def connect_to_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="HappinessA1@2020",
        database="library_db"
    )
    return mydb

# Function to create the 'books' table
def create_books_table():
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        ISBN VARCHAR(255)
    )
    """)

    print("Table 'books' created successfully!")
    mycursor.close()
    mydb.close()

# Function to add a new book
def add_book(title, author, ISBN):
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    sql = "INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)"
    values = (title, author, ISBN)

    mycursor.execute(sql, values)
    mydb.commit()

    print(f"Book '{title}' added successfully!")
    mycursor.close()
    mydb.close()

# Function to search for a book by title
def search_books_by_title(search_title):
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    sql = "SELECT * FROM books WHERE title LIKE %s"
    value = ("%"+search_title+"%",)

    mycursor.execute(sql, value)
    results = mycursor.fetchall()

    if results:
        for result in results:
            print(f"ID: {result[0]}, Title: {result[1]}, Author: {result[2]}, ISBN: {result[3]}")
    else:
        print("No books found with that title.")
    
    mycursor.close()
    mydb.close()

# Function to list all books
def list_all_books():
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM books")
    results = mycursor.fetchall()

    for result in results:
        print(f"ID: {result[0]}, Title: {result[1]}, Author: {result[2]}, ISBN: {result[3]}")
    
    mycursor.close()
    mydb.close()

# (Bonus) Function to delete a book by its ID
def delete_book_by_id(book_id):
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    sql = "DELETE FROM books WHERE id = %s"
    value = (book_id,)

    mycursor.execute(sql, value)
    mydb.commit()

    print(f"Book with ID {book_id} deleted successfully!")
    mycursor.close()
    mydb.close()

# Example of how to use the functions
if __name__ == "__main__":
    # Create the books table (run this once)
    create_books_table()

    # Add books
    add_book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "978-0747532699")
    add_book("The Hobbit", "J.R.R. Tolkien", "978-0261102217")

    # Search for a book by title
    search_books_by_title("Harry")

    # List all books
    list_all_books()

    # Delete a book by ID (optional)
    # delete_book_by_id(1)

