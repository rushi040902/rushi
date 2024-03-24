from sqlalchemy import text
from fastapi import APIRouter

from user.model import UserModel
from utils.db_session import engine, execute_custom_delete_update_query, execute_custom_query
from utils.db_session import execute_custom_delete_update_query

class UserAPI:
    router=APIRouter()

    @router.post('/add_user')
    def create_user(user:UserModel):
        try:
            query = f'''insert into dev.tbl_d_user(user_id,first_name,last_name,mobile_number,email_id,branch_id,city,state,zip_code,address,password,type,create_date,update_date) values('{user.user_id}','{user.first_name}','{user.last_name}','{user.mobile_number}','{user.email_id}','{user.branch_id}','{user.city}','{user.state}',{user.zip_code},'{user.address}','{user.password}','{user.type}','{user.create_date}','{user.update_date}');'''
            execute_custom_delete_update_query(query)
        except Exception as e:
            print(e)
    
        
    @router.get('/get_users')
    def get_user():
        try:
            query=f'''select user_id,first_name,last_name,mobile_number,email_id,branch_id,city,state,zip_code,address,password,type,create_date,update_date from dev.tbl_d_user'''
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                print(rows)
                data=[]
                for row in rows:
                    data.append({'user_id':row[0],'first_name':row[1],'last_name':row[2],'mobile_number':row[3],'email_id':row[4],'branch_id':row[5],'city':row[6],'state':row[7],'zip_code':row[8],'address':row[9],'password':row[10],'type':row[11],'create_date':row[12],'update_date':row[13]})
                return data
        except Exception as e:
            print(e)
    
        
    @router.delete("/delete_user/{id}")
    def delete_user(id:str):
        try:
            query=f''' select user_id from dev.tbl_d_user where user_id='{id}';'''
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                print(rows)
                if len(rows) is not 0:
                    query=f'''delete from dev.tbl_d_user where user_id='{id}';'''
                    execute_custom_delete_update_query(query)
                    return "delete"
                else:
                    return "not exist"
        except Exception as e:
            print(e)

    @router.put("/update/user/{id}")
    def update_user(user:UserModel):
        try:
            query=f'''update dev.tbl_d_user set first_name ='none' ,last_name ='none',mobile_number ='none',email_id ='none',branch_id = 'none',city = 'none',state = 'none',zip_code = 'none',address = 'none',password = 'none',type = 'none',create_date = 'none',update_date = data where user_id = "{user.user_id}" ;'''
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                print(rows)
                if len(rows)==0:
                    query=f'''update dev.tbl_d_user set first_name = '{user.first_name}',last_name = '{user.last_name}' where user_id='{user.user_id}';'''
                    execute_custom_delete_update_query(query)
                    return "update query"
                else:
                    return "query is exist"
        except Exception as e:
            print(e)
