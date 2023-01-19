Python code for a managing a book system database with the following functionalities and a database to store book information.
Validate book data including year (between 1200 and current year), page count (warning for high page count), and required fields (title, author, genre, publisher, language).
Save book details to the database.
conditions to follow:
If the language is in english and japanese, the system should print the book description and author of the book along with the language.
if the number of pages of the book are more than 3000, the system should display a suitable message.
Display the books from database with same genre. 
The system should ensure that none of the fields are empty. If any of the fields are empty, the system should display a suitable message. 
Allow users to search for books by author using a virtual model (basic implementation using string matching).