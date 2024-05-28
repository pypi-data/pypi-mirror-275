import json
from decimal import Decimal

class RawDynamodbEncoder(json.JSONEncoder):
    def default(self, obj):
        match obj:
            case Decimal():
                return str(obj)
        return super().default(obj)