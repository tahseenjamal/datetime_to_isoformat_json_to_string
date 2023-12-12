import json
from datetime import datetime
from json import JSONEncoder

employee = [{
    "id": 456,
    "name": "William Smith",
    "salary": 8000,
    "joindate": datetime.now()
},{
    "id": 456,
    "name": "William Smith",
    "salary": 8000,
    "joindate": datetime.now()
}]

# subclass JSONEncoder
class DateTimeEncoder(JSONEncoder):
    #Override the default method
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()

print('JSON with datetime object')
employeeJSONData = json.dumps(employee, indent=2, cls=DateTimeEncoder)
print(employeeJSONData)

