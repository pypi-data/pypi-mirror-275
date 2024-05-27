import matplotlib.pyplot as plt

class CatVisualizer:
   def __init__(self, tracker):
       self.tracker = tracker
   
   def plot_weight(self, start_date=None, end_date=None):
       weights = self.tracker.get_records("weight", start_date, end_date)
       dates = [r["date"] for r in weights]
       values = [r["value"] for r in weights]
       
       plt.figure(figsize=(10, 6))
       plt.plot(dates, values, marker='o')
       plt.xlabel("Date")
       plt.ylabel("Weight (kg)")
       plt.title(f"Weight of {self.tracker.name}")
       plt.grid()
       plt.show()
   
   def plot_food_intake(self, start_date=None, end_date=None):
       food_intakes = self.tracker.get_records("food", start_date, end_date)
       dates = [r["date"] for r in food_intakes]
       values = [r["value"] for r in food_intakes]
       
       plt.figure(figsize=(10, 6))
       plt.bar(dates, values)
       plt.xlabel("Date")
       plt.ylabel("Food Intake (g)")
       plt.title(f"Food Intake of {self.tracker.name}")
       plt.grid()
       plt.show()
   
   def plot_water_intake(self, start_date=None, end_date=None):
       water_intakes = self.tracker.get_records("water", start_date, end_date)
       dates = [r["date"] for r in water_intakes]
       values = [r["value"] for r in water_intakes]
       
       plt.figure(figsize=(10, 6))
       plt.bar(dates, values)
       plt.xlabel("Date")
       plt.ylabel("Water Intake (ml)")
       plt.title(f"Water Intake of {self.tracker.name}")
       plt.grid()
       plt.show()
   
   def plot_activity_level(self, start_date=None, end_date=None):
       activity_levels = self.tracker.get_records("activity", start_date, end_date)
       dates = [r["date"] for r in activity_levels]
       values = [r["value"] for r in activity_levels]
       
       plt.figure(figsize=(10, 6))
       plt.plot(dates, values, marker='o')
       plt.xlabel("Date")
       plt.ylabel("Activity Level")
       plt.title(f"Activity Level of {self.tracker.name}")
       plt.grid()
       plt.show()
   
   def plot_sleep_duration(self, start_date=None, end_date=None):
       sleep_durations = self.tracker.get_records("sleep", start_date, end_date)
       dates = [r["date"] for r in sleep_durations]
       values = [r["value"] for r in sleep_durations]
       
       plt.figure(figsize=(10, 6))
       plt.plot(dates, values, marker='o')
       plt.xlabel("Date")
       plt.ylabel("Sleep Duration (hours)")
       plt.title(f"Sleep Duration of {self.tracker.name}")
       plt.grid()
       plt.show()