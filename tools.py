
import json


def get_menu() -> str:
    """Retrieve the coffee shop menu.

    Returns:
        A JSON string containing the available menu items.
    """
    try:
        with open("menu.json", "r") as file:
            menu = json.load(file)

        return json.dumps(menu)

    except Exception as e:
        return json.dumps({
            "error": f"Could not retrieve menu: {str(e)}"
        })
"""
Tools for retrieving information from the coffee shop menu.

RAG functionality will be implemented during the development phase.
"""
