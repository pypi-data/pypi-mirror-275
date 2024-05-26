import json


class Synthesizer(json.JSONEncoder):
    def default(self, obj):
        # Delegate to a subclass's default method
        if hasattr(obj, 'dehydrate'):
            return obj.dehydrate()
        else:
            return super().default(obj)

