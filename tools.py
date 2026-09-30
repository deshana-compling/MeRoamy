import json
from database import search_packages

#Function schema

package_function = {
    "name": "search_packages",
    "description": "Get information about the travel packages to the destination place",
    "parameters": {
        "type": "object",
        "properties": {
            "place": {
                "type" : "string",
                "description": "The place the user wants to travel to"
            },
        },
        "required" : ["place"],
        "additionalProperties" : False
    }
}
tools = [
    {
        "type": "function",
        "function": package_function
    }
]   

def toolcalls(message):
    responses = []
    for tool_call in message.tool_calls:
        if tool_call.function.name == 'search_packages':
            arguments = json.loads(tool_call.function.arguments)
            place = arguments.get('place')
            package_info = search_packages(place)
            responses.append({
                'role':'tool',
                'content': str(package_info),
                'tool_call_id': tool_call.id
            })
    return responses