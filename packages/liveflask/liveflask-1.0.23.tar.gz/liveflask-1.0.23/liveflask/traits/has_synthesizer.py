import json
from datetime import datetime


def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    else:
        raise TypeError("Type not serializable")


class Synthesizer(json.JSONEncoder):
    def default(self, obj):
        # Delegate to a subclass's default method
        if hasattr(obj, 'dehydrate'):
            return obj.dehydrate()
        else:
            try:
                return super().default(obj)
            except TypeError:
                if isinstance(obj, datetime):
                    return obj.isoformat()

