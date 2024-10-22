from turtle import done
from typing import Union
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
import sqlite3

class BookItem(BaseModel):
    title: str
    author: str

class Book(BookItem):
    id: int

def create_connection():
    connection = sqlite3.connect("books.db")
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL
    )
    """)
    connection.commit()
    connection.close()
    
def get_book(id:int=None):
    connection = create_connection()
    cursor = connection.cursor()
    if id :
        resp = cursor.execute(f"""
        SELECT * FROM books WHERE id={id}
        """)
    else :
        resp = cursor.execute("""SELECT * FROM books""")
    result = resp.fetchall()
    connection.close()
    return (result if result else None)
    
def create_book(book: BookItem):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (book.title, book.author))
    connection.commit()
    connection.close()
    
def update_book(field:str, id:int,value: str):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"UPDATE books SET {field} = ? WHERE id = ?", (value,id))
    connection.commit()
    connection.close()

def delete_book(id:int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM books WHERE id = {id}")
    connection.commit()
    connection.close()

create_table() # Call this function to create the table

app = FastAPI()
 
@app.get("/")
def read_root():
    return {"message": "Hello, World"}

@app.post("/books")
def create_book_endpoint(book: BookItem):
    book_id = create_book(book)
    return {"id": book_id, **book.dict()}

@app.get("/books")
def getAll_books_endpoint():
    result = []    
    books = get_book()
                
    for book in books :
        for i in range(0,len(book),4) :
            result.append({"id":book[i],"title":book[i+1],"author":book[i+2]})    
    return result

@app.get("/books/{id}")
def get_book_by_id(id:int):
    book = get_book(id)
    
    if book :
        return {"id":book[0][0],"title":book[0][1],"author":book[0][2]} 
    else :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with ID {id} not found")
        
@app.put("/books/{id}")
def update_book_endpoint(id:int, book: BookItem):
    book_found = get_book(id)
    
    if book_found :
        update_book("title",id,book.dict()["title"])
        update_book("author",id,book.dict()["author"])
        return {"message": f"Book with ID {id} successfully updated"}
    else :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with ID {id} not found")
        
@app.delete("/books/{id}")
def delete_book_endpoint(id:int):
    book = get_book(id)
    
    if book :
        delete_book(id)
        return {"message": f"Book with ID {id} successfully deleted"}
    else :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with ID {id} not found")
        
