from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def viewbooks():
    print("Available books:")
    print("ID     Title                             Author ")
    print("-"*60)
    for x in library_books:
        if x["available"]: #shows the books which are available if it is true
            print(f"{x["id"]:<6} {x["title"]:<30} {x["author"]}")

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def searchbooks():
    want = input("Enter the name of the Auther or the Genre: ")
    for x in library_books:
        if x["author"].lower()==want.lower() or x["genre"].lower()==want.lower():
            print("The books that came up with your response are:")
            print(f"{x["title"]}")


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
def checkout():
    check = input("Input the ID of the Book you want to checkout: ")
    for x in library_books:
        if x["id"] == check: #if the Id matches then it proceeds to checkout
            if x["available"]:
                x["available"] = False
                x["due_date"] = (datetime.today() + timedelta(weeks=2)).strftime("%Y-%m-%d") #Got help from AI for datetime logic
                x["checkouts"] += 1
                print(f"you have successfully checked out {x["title"]}")
        else:
            print("It has already been checked out.")
        return
    print("Book ID not Found")

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def returnbooks():
    check = input("Input the ID of the Book you want to return: ")
    for x in library_books:
        if x["id"] == check: #if the Id matches then it proceeds to return
            if x["available"]:
                print("The book is already available in the library")
            else:
                x["available"] = True
                x["due_date"] = None
                print(f"you have successfully returned {x["title"]}")
            return
    print("Book ID not Found")
# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    viewbooks()
    returnbooks()
    pass

