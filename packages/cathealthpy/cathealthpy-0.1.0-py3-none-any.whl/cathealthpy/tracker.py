import datetime

class CatTracker:
    def __init__(self, name):
        self.name = name
        self.records = []
    
    def record_weight(self, weight, date=None):
        if date is None:
            date = datetime.date.today()
        self.records.append({"type": "weight", "value": weight, "date": date})
    
    def record_food_intake(self, amount, date=None):
        if date is None:
            date = datetime.date.today()
        self.records.append({"type": "food", "value": amount, "date": date})
    
    def record_water_intake(self, amount, date=None):
        if date is None:
            date = datetime.date.today()
        self.records.append({"type": "water", "value": amount, "date": date})
    
    def get_records(self, record_type=None, start_date=None, end_date=None):
        if record_type:
            records = [r for r in self.records if r["type"] == record_type]
        else:
            records = self.records
        
        if start_date:
            records = [r for r in records if r["date"] >= start_date]
        
        if end_date:
            records = [r for r in records if r["date"] <= end_date]
        
        return records