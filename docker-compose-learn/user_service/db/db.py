from typing import Dict, Generator

def get_all_users() -> Generator[Dict[str, str], None, None]:
    users_data = [
        {"id": "1", "name": "John Doe", "position": "Developer", "company": "Example Inc"},
        {"id": "2", "name": "Jane Smith", "position": "Designer", "company": "Sample Corp"},
    ]
    for user_data in users_data:
        yield user_data
