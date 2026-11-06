# Study hour, Thu Nov 5: Session 2 of the lawn treatment planner
New idea tonight: look backward, not just forward. Forecast rain is a guess. Past rain is what soaked the ground.
1. (10 min) In Safari open this URL (Brandon, MS, last 2 days of hourly rain):
   https://api.open-meteo.com/v1/forecast?latitude=32.27&longitude=-89.99&hourly=precipitation&precipitation_unit=inch&timezone=America%2FChicago&past_days=2&forecast_days=1
   Scroll the JSON. Each hour has precipitation in inches. That is history, not a forecast.
2. (15 min) In spray_day.py, add a rule near the top, for example:
   PAST_RAIN_MAX = 0.50  # inches in the past 48 hours; soaked ground means runoff risk
3. (20 min) Write a helper that sums precipitation for the 48 hours before the hour you are scoring. Use past_days=2 on the Open-Meteo URL (same API as Session 1). If the sum is over PAST_RAIN_MAX, mark that hour NO with a clear reason.
4. (10 min) Run it on your phone. Compare with a yard you know: after a hard rain, would you spray?
5. (5 min) Write one more field rule the script still misses. That becomes Session 3.
