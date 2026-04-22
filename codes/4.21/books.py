from fastapi import FastAPI
app = FastAPI()


Books= [
{'title':'Titleone','author':'Author one','category':'science'},
{'title':'Titletwo','author':'Author two','category':'science'},
{'title':'Titlethree','author':'Author three','category':'history'},
{'title':'Titlefour','author':'Author four','category':'math'},
{'title':'Titlefive','author':'Author five','category':'math'},
{'title':'Titlesix','author':'Author six','category':'math'}
]


@app.get("/books")
async def read_all_books():
    return Books

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in Books:
        if book.get('title').casefold() == book_title.casefold():
            return book
@app.git("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in Books:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in Books:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
           books_to_return.append(book)
    return books_to_return