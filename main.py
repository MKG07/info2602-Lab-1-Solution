from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!' 

@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: 
                filtered_students.append(student) 
        return filtered_students
    return data 

@app.get('/students/{id}')
async def get_student(id):
  for student in data: 
    if student['id'] == id: 
        return student 



@app.get('/stats') 
async def get_stats():
    
    chicken_count = 0
    fish_count = 0
    vegetable_count = 0

    cs_major_count = 0
    cs_special_count = 0
    it_major_count = 0
    it_special_count = 0 

    for student in data: 
        if student['pref'] == 'Chicken':
            chicken_count += 1
        elif student['pref'] == 'Fish':
            fish_count += 1
        elif student['pref'] == 'Vegetable':
            vegetable_count += 1 

        if student['programme'] == 'Computer Science (Major)':
            cs_major_count += 1
        elif student['programme'] == 'Computer Science (Special)':
            cs_special_count += 1
        elif student['programme'] == 'Information Technology (Major)':
            it_major_count += 1
        elif student['programme'] == 'Information Technology (Special)':
            it_special_count += 1 

    return {
        "Chicken": chicken_count,
        "Fish": fish_count,   
        "Vegetable": vegetable_count,
        "CS Major": cs_major_count,
        "CS Special": cs_special_count,
        "IT Major": it_major_count,
        "IT Special": it_special_count,
    } 

@app.get('/add/{a}/{b}')
async def add(a: int, b: int): 
    return {"result": a + b}  

@app.get('/subtract/{a}/{b}')
async def subtract(a: int, b: int):
    return {"result": a - b}

@app.get('/multiply/{a}/{b}')
async def multiply(a: int, b: int):
    return {"result": a * b}

@app.get('/divide/{a}/{b}')
async def divide(a: float, b: float):
    if b == 0:
        return {"error": "Division by zero is not allowed."}
    return {"result": a / b}        


