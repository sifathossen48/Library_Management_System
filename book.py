import add_books
import view_all_books
import update_books
import remove_books
all_books = []
while True:
    print("Welcome to Library Management System.")
    print("0. Exit")
    print("1. Add Books")
    print("2. Update Your Book")
    print("3. Remove a Select Books")
    print("4. View All Books")

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System.")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        update_books = update_books.update_books(all_books)
    elif menu == "3":
        remove_books = remove_books.remove_books(all_books)
    elif menu == "4":
        view_all_books.view_all_books(all_books)
    else:
        print("Chose a valid number")