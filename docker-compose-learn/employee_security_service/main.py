from fastapi import FastAPI, status, Request, Response
from db.db import get_all_employees
from model.employees import Employee

app = FastAPI()

@app.get('/api/employees', status_code=status.HTTP_200_OK)
async def get_employees(request: Request, response:Response):
    employees_data = list(get_all_employees())
    employees = [Employee(**employee_data) for employee_data in employees_data]
    return employees