from fastapi import FastAPI, status, Request, Response
from model.user import User
from db.db import get_all_users

app = FastAPI()

@app.get('/api/users', status_code=status.HTTP_200_OK)
async def get_users(request: Request, response:Response):
    users_data = list(get_all_users())
    users = [User(**user_data) for user_data in users_data]
    return users