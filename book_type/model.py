from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class BookTypemodel(BaseModel):
     
     book_type_id:str
     create_date: Optional[date]=datetime.now()
     update_date:Optional[date]=None
    
