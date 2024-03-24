from sqlalchemy import text
from book_type.model import BookTypemodel, BookTypemodelModel
from db_session import execute_custom_delete_update_query,engine


class BookTypeServices:
  
    def create_book_type(book_type:BookTypemodel):
       try:
           query = f'''select book_type_id from dev.tbl_d_book_type where book_type_id ='{book_type.book_type_id}','{book_type.create_date}','{book_type.update_date}');'''
           with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                if len(rows)==0:
                    query=f'''insert into dev.tbl_f_book_type(book_type_id,create_date,update_date) values('{book_type.book_type_id}','{book_type.create_date}','{book_type.update_date}')'''
                    execute_custom_delete_update_query(query)
                    return"user created sucessfully"
                else:
                    return"All ready Created"
       except Exception as e:
            print(e)
           


       
    def get_book_type():
       try:
            query =f'''select book_type,book_id,create_date,update_date  from dev.tbl_d_book_type'''
            with engine.connect() as connection:
                
                 result = connection.execute(text(query))
                 rows = result.fetchall()
                 print(rows)
                 data=[]
                 for row in rows:
                     data.append({'book_type_id':row[0],'create_date':row[2],'update_date':row[3]})
                     return data
       except Exception as e:
                    print(e)


   
    def delete_book_type(id:str):
          try:
            query=f''' select book_type_id from dev.tbl_d_book_type where book_type_id='{id}';'''
            with engine.connect() as connection:
                 result = connection.execute(text(query))
                 rows = result.fetchall()
                 print(rows)
                 if len(rows) is not 0:
                     query=f'''delete from dev.tbl_d_book_type where book_type_id='{id}';'''
                     execute_custom_delete_update_query(query)
                     return "delete"
                 else:
                     return "not exist"
          except Exception as e:
             print(e)


    
    def update_book_type(book_type:BookTypemodel):
          try:
            query=f'''select book_type_id from dev.tbl_d_book_type where book_type_id = '{book_type.book_type_id}';'''
            with engine.connect() as connection:
                 result = connection.execute(text(query))
                 rows = result.fetchall()
                 print(rows)
                 if len(rows)==0:
                    query=f'''update dev.tbl_f_book_type set book_type_id = '{book_type.id}',create_date='{book_type.create_date}',update_date='{book_type.update_date}'where book_type_id='{book_type.book_type_id}' '''
                    execute_custom_delete_update_query(query)
                    return "update query"
                 else:
                     return BookTypeServices.create_book_type(book_type)
          except Exception as e:
              print(e)





