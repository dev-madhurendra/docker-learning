from typing import Dict, Generator

def get_all_tools() -> Generator[Dict[str, str], None, None]:
    tools_data = [
        {"id": "1", "name": "Slack"}
    ]
    for tool_data in tools_data:
        yield tool_data
