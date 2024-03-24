from fastapi import APIRouter
from sqlalchemy import text

from book_type.model import BookTypemodel, BookTypemodel
from book_type.services import BookTypeServices
from db_session import execute_custom_delete_update_query,engine


class BookTypeAPI:
    router=APIRouter()
    
    @router.post('/add_BookType')
    def create_BookType(BookType:BookTypemodel):
        return BookTypeServices.create_BookType(BookType)
        
    @router.get('/get_BookType')
    def get_BookType():
        return BookTypeServices.get_BookType()
            
    @router.delete("/delete_BookType/{id}")
    def delete_BookType(id:str):
        return BookTypeServices.delete_libray(id)
            
    @router.put("/update_BookType")
    def update_BookType(BookType:BookTypemodel):
     return BookTypeServices.update_BookType(BookType)