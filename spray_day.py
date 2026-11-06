# spray_day.py - Sessions 1-2 of the lawn treatment planner
# Checks the next 3 days in Brandon, MS and scores each daylight hour for spraying.
# Standard library only, so it runs on a computer or in an iPhone Python app.
# Weather: Open-Meteo (free, no API key). The product label always wins over this script.
import json, urllib.request

LAT, LON = 32.27, -89.99  # Brandon, MS
URL = ("https://api.open-meteo.com/v1/forecast"
       f"?latitude={LAT}&longitude={LON}"
       "&hourly=temperature_2m,wind_speed_10m,precipitation_probability,precipitation"
       "&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch"
       "&timezone=America%2FChicago&past_days=2&forecast_days=4")

# Rules (general starting points; check your product label)
WIND_MIN, WIND_MAX = 0, 15       # Aaron's field rule: calm is fine, over 15 mph is a no
TEMP_MIN, TEMP_MAX = 50, 85      # cold slows uptake; heat can make some herbicides volatilize
RAIN_CHANCE_MAX = 40             # % chance in the next 24 hours
RAIN_TOTAL_MAX = 0.10            # inches expected in the next 24 hours
PAST_RAIN_MAX = 0.50             # inches in the past 48 hours; soaked ground = runoff

def get_forecast():
    with urllib.request.urlopen(URL, timeout=15) as r:
        return json.load(r)["hourly"]

def check_hour(h, i):
    reasons = []
    wind, temp = h["wind_speed_10m"][i], h["temperature_2m"][i]
    next24 = slice(i, i + 24)
    chance = max(x or 0 for x in h["precipitation_probability"][next24])
    total = sum(x or 0 for x in h["precipitation"][next24])
    past = sum(x or 0 for x in h["precipitation"][max(0, i - 48):i])
    if past > PAST_RAIN_MAX: reasons.append(f"{past:.2f} in rain past 48h, ground soaked")
    if wind < WIND_MIN: reasons.append(f"wind {wind:.0f} mph too calm")
    if wind > WIND_MAX: reasons.append(f"wind {wind:.0f} mph too strong")
    if temp < TEMP_MIN: reasons.append(f"{temp:.0f}F too cold")
    if temp > TEMP_MAX: reasons.append(f"{temp:.0f}F too hot")
    if chance > RAIN_CHANCE_MAX: reasons.append(f"{chance}% rain chance in 24h")
    if total > RAIN_TOTAL_MAX: reasons.append(f"{total:.2f} in rain in 24h")
    return reasons

def main():
    h = get_forecast()
    last = len(h["time"]) - 24  # need 24 hours ahead to judge rain
    for i in range(48, last):
        day, clock = h["time"][i].split("T")
        if not ("07:00" <= clock <= "18:00"):
            continue
        reasons = check_hour(h, i)
        verdict = "GO " if not reasons else "NO "
        print(f"{day} {clock}  {verdict} {'; '.join(reasons)}")
    print("\nGeneral guide only. Always follow the product label.")

if __name__ == "__main__":
    main()
