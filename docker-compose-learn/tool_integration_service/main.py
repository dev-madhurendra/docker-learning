from fastapi import FastAPI, status, Request, Response
from model.tool import Tool
from db.db import get_all_tools

app = FastAPI()

@app.get('/api/tools', status_code=status.HTTP_200_OK)
async def get_users(request: Request, response:Response):
    tools_data = list(get_all_tools())
    tools = [Tool(**tool_data) for tool_data in tools_data]
    return tools