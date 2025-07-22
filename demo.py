import mysql.connector
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class student(BaseModel):
    id:str
    name:str
    age:str
    phno:str
@app.post("/")
def sql_connect(i:student):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student",
        port="3308"
    )
    mypost = mydb.cursor()
    mypost.execute("INSERT INTO details VALUES('" + i.id + "','" + i.name + "','" + i.age+ "','" + i.phno +"')")
    mydb.commit()
    return "data inserted successfully"
@app.get("/{name}")
def sql_connect(name: str):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student",
        port="3308"
    )
    mypost = mydb.cursor()
    mypost.execute("SELECT * FROM details WHERE name = %s", (name,))
    r = mypost.fetchall()
    return r
