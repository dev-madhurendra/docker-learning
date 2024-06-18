from typing import Dict, Generator

def get_all_employees() -> Generator[Dict[str, str], None, None]:
    employees_data = [
        {"id": "1", "name": "John Doe", "position": "Developer", "company": "Example Inc"},
        {"id": "2", "name": "Jane Smith", "position": "Designer", "company": "Sample Corp"},
    ]
    for employee_data in employees_data:
        yield employee_data
