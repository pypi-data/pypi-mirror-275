class CatAnalyzer:
   def __init__(self, tracker):
       self.tracker = tracker

   def average_weight(self, start_date=None, end_date=None):
       weights = [r["value"] for r in self.tracker.get_records("weight", start_date, end_date)]
       if len(weights) > 0:
           return sum(weights) / len(weights)
       else:
           return None

   def average_food_intake(self, start_date=None, end_date=None):
       food_intakes = [r["value"] for r in self.tracker.get_records("food", start_date, end_date)]
       if len(food_intakes) > 0:
           return sum(food_intakes) / len(food_intakes)
       else:
           return None

   def total_water_intake(self, start_date=None, end_date=None):
       water_intakes = [r["value"] for r in self.tracker.get_records("water", start_date, end_date)]
       return sum(water_intakes)

   def average_activity_level(self, start_date=None, end_date=None):
       activity_levels = [r["value"] for r in self.tracker.get_records("activity", start_date, end_date)]
       if len(activity_levels) > 0:
           return sum(activity_levels) / len(activity_levels)
       else:
           return None

   def max_sleep_duration(self, start_date=None, end_date=None):
       sleep_durations = [r["value"] for r in self.tracker.get_records("sleep", start_date, end_date)]
       if len(sleep_durations) > 0:
           return max(sleep_durations)
       else:
           return None

   def min_sleep_duration(self, start_date=None, end_date=None):
       sleep_durations = [r["value"] for r in self.tracker.get_records("sleep", start_date, end_date)]
       if len(sleep_durations) > 0:
           return min(sleep_durations)
       else:
           return None

   def total_litter_box_visits(self, start_date=None, end_date=None):
       litter_box_visits = [r["value"] for r in self.tracker.get_records("litter_box", start_date, end_date)]
       return sum(litter_box_visits)