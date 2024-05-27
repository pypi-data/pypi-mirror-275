class CatAdvisor:
   def __init__(self, analyzer):
       self.analyzer = analyzer

   def weight_advice(self, start_date=None, end_date=None):
       avg_weight = self.analyzer.average_weight(start_date, end_date)
       if avg_weight is None:
           return "データが不足しています。"
       elif avg_weight < 3.0:
           return "猫の体重が少し低すぎるようです。食事量を増やすことを検討してください。"
       elif avg_weight > 5.5:
           return "猫の体重が少し高すぎるようです。食事量を減らすことを検討してください。"
       else:
           return "猫の体重は正常範囲内です。"

   def food_intake_advice(self, start_date=None, end_date=None):
       avg_food_intake = self.analyzer.average_food_intake(start_date, end_date)
       if avg_food_intake is None:
           return "データが不足しています。"
       elif avg_food_intake < 150:
           return "猫の食事量が少し少ないようです。食事量を増やすことを検討してください。"
       elif avg_food_intake > 250:
           return "猫の食事量が少し多いようです。食事量を減らすことを検討してください。"
       else:
           return "猫の食事量は適切です。"

   def water_intake_advice(self, start_date=None, end_date=None):
       total_water_intake = self.analyzer.total_water_intake(start_date, end_date)
       days = (end_date - start_date).days + 1
       avg_water_intake = total_water_intake / days
       if avg_water_intake < 50:
           return "猫の水分摂取量が少し少ないようです。新鮮な水をいつでも利用できるようにしてください。"
       else:
           return "猫の水分摂取量は十分です。"

   def activity_level_advice(self, start_date=None, end_date=None):
       avg_activity_level = self.analyzer.average_activity_level(start_date, end_date)
       if avg_activity_level is None:
           return "データが不足しています。"
       elif avg_activity_level < 2:
           return "猫の活動量が少し低いようです。おもちゃを使って遊ぶ時間を増やすことを検討してください。"
       else:
           return "猫の活動量は十分です。"

   def sleep_duration_advice(self, start_date=None, end_date=None):
       min_sleep_duration = self.analyzer.min_sleep_duration(start_date, end_date)
       max_sleep_duration = self.analyzer.max_sleep_duration(start_date, end_date)
       if min_sleep_duration is None or max_sleep_duration is None:
           return "データが不足しています。"
       elif min_sleep_duration < 12 or max_sleep_duration > 20:
           return "猫の睡眠時間が通常の範囲から外れています。獣医師に相談することをお勧めします。"
       else:
           return "猫の睡眠時間は正常範囲内です。"

   def litter_box_advice(self, start_date=None, end_date=None):
       total_visits = self.analyzer.total_litter_box_visits(start_date, end_date)
       days = (end_date - start_date).days + 1
       avg_visits = total_visits / days
       if avg_visits < 1:
           return "猫のトイレ使用回数が少ないようです。健康状態を確認し、必要に応じて獣医師に相談してください。"
       elif avg_visits > 4:
           return "猫のトイレ使用回数が多いようです。健康状態を確認し、必要に応じて獣医師に相談してください。"
       else:
           return "猫のトイレ使用回数は正常範囲内です。"