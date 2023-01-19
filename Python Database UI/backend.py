from tkinter import *
import datetime
import messagebox
import sqlite3 as sql



current_day = datetime.date.current_day() 
year = current_day.year 
print(year)

with sql.connect("Book_management") as book_management:
    cursor = book_management.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS book_details (
    unique_number INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    yr INTEGER CHECK (year >= 1200 AND year <= CURRENT_YEAR),
    description TEXT,
    pages INTEGER,
    price REAL,
    language TEXT CHECK (language IN ('English', 'Japanese')),
    publisher TEXT,
    genre TEXT
);
""")

def validate_book(book_data):
    """
    Validates book data and saves it to the database if valid.

    Args:
        book_data (dict): Dictionary containing book details.

    Returns:
        str: Success message if saved, error message otherwise.
    """

def save_book():
     time = datetime.date.current_day() 
     time1 = current_day.year
     time1 = str(time1)
     
     unique_number = unique_number.get()
     description  = description.get()
     heading = heading_entry.get()
     pages = pages.get()
     price = price.get()
     yr = yr_entry.get()
     language = language.get()
     publisher = publisher.get()
     genre = genre.get()
     author = author_entry.get()
     

     present = True
     for file in files:
         if file == unique_number:
             present = False
     if present == False:
         messagebox.showerror("Book exists") 
     elif ((int (yr < 1200 or (int(yr) > int(time1))):
         messagebox.showerror("Error: Invalid year. Year must be between 1200 and current year.")
     elif book_data["pages"] > 3000:
         messagebox.showerror("Warning: This book has a very high page count (>3000).") 
     elif isnull(author) or isnull(title) or isnull(genre) or isnull(publisher) or isnull(language) or isnull(heading): 
         messagebox.showerror("Title and Author fields cannot be empty") 
     else: 
         cursor.execute("""INSERT INTO details(unique_number, description,heading, title, author, yr, price, pages, genre, publisher) VALUES (?,?,?,?,?,?,?,?,?,?)""", (
                         unique_number,description, heading, title, author, yr, price, pages,genre, publisher))
                                    
 book_management.commit()
 

def display_books():
    """
    Fetches and displays all book details from the database.
    """

    cursor.execute("SELECT * FROM book_details")
    books = cursor.fetchall()

    if not books:
        print("No books found in the database.")
        return

    # Display books with genre grouping
    genres = set(book[9] for book in books)  # Extract unique genres
    for genre in genres:
        print(f"\n**Genre: {genre}**")
        for book in books:
            if book[9] == genre:
                print(f"\t- Unique Number: {book[0]}\n\t- Title: {book[1]}\n\t- Author: {book[2]}\n\t- Year: {book[3]}\n\t- Description: {book[4]}\n\t- Pages: {book[5]}\n\t- Price: ${book[6]}\n\t- Language: {book[7]}\n\t- Publisher: {book[8]}\n")


def virtual_model(query):
    """
    Simulates a virtual_model by querying the database.

    The code attempts to process the user's query in lowercase 
    and potentially interact with a model retrieved from the enquire.get() function.
    """

    # Extract keywords and split query
    keywords = query.lower().split()
    model = enquire.get()
    if book in model.lower()
        split = model.lower.split
        whitespace = "".join(y[5:])

    #"Recommend me a book by [author name]"
    if "recommend" in keywords and "by" in keywords:
        author = " ".join(keywords[keywords.index("by") + 1:])
        cursor.execute("SELECT title, author FROM book_details WHERE author = ?", (author,))
        results = cursor.fetchall()
        if results:
            return f"Here's a book by {author}: {results[0][0]}"
        else:
            return f"Sorry, I couldn't find a book by {author} in the database."

#Creating the interface

