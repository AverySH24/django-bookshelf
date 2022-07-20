# Bookshelf - Django Review    
Similar to Cars and Brands, this project is creating a directory that separates books into a few genres.
Books should be able to display their specific information including title, author, and description. Meanwhile, genres will contain their name.

Books and genres will be saved in the SQL database.
There must be a functionality where a book can be added to a specified genre.
Editing books must also be possible where the input fields are already filled out by the old information, ready to be edited by the user.

The following urls should lead to:
1. `genres/`- shows a list of the genres (links to click to their respective books)
2. `genres/<int:genre_id>/` - show list of respective books (link to their specific info)
3. `genres/<int:genre_id>/books/<int:book_id>/` - display information of a single book
4. `genres/<int:genre_id>/books/<int:book_id>/edit/` - edit information of the book
5. `genres/<int:genre_id>/books/new/` - add a new book to a specified category
