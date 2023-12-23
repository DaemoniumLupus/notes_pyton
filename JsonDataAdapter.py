from Notes import Notes
import json
class JsonDataAdapter:
    @staticmethod
    def to_json(o,size:int):
        if isinstance(o,Notes):
            return json.dumps({
                "id": o.id,
                "title": o.title,
                "text": o.text,
                "date": o.date,
                })
        
    