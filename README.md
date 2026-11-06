# lawn-planner

A small Python tool from a working landscaper in Brandon, MS, learning Python in public.

`spray_day.py` is a spray-day weather checker. It reads a free forecast and scores each daylight hour as **GO** or **NO** for spraying. It is a planning aid, not a substitute for the product label.

## What it does

The script asks the free [Open-Meteo](https://open-meteo.com/) API for Brandon, MS (latitude 32.27, longitude -89.99). No API key and no account. It uses only the Python standard library.

For each hour from 7 AM to 6 PM, local time, over the next three days, it prints **GO** or **NO**. A **NO** line says which rule failed: wind, temperature, rain ahead, or rain that already fell.

## Field rules

These live at the top of `spray_day.py`. Change the numbers there if your label or your own practice is different. They are general starting points from field experience, not agronomic advice.

| Rule | Setting | Why |
|---|---|---|
| Wind | 0 to 15 mph | From field experience: calm air is fine. Over 15 mph, do not spray (drift). |
| Temperature | 50 to 85 °F | Cold slows uptake. Heat can make some herbicides volatilize. |
| Rain chance | 40% max in the next 24 hours | Rain can wash product off before it works. |
| Rain amount | 0.10 in max in the next 24 hours | Same reason. |
| Past rain (Session 2) | More than 0.50 in in the past 48 hours is **NO** | Soaked ground causes runoff. |

## Run it

On a computer:

```bash
python3 spray_day.py
```

Nothing to install. It needs Python 3 and a network connection so it can reach Open-Meteo.

On an iPhone (Python Code Pad or a similar app):

1. Copy all of `spray_day.py` into the app.
2. If you get an SSL certificate error, add this line near the top, under the imports:

   ```python
   import ssl; ssl._create_default_https_context = ssl._create_unverified_context
   ```

   This skips certificate checking. It is fine for reading a public weather forecast. Do not use it for anything with passwords or payments.
3. Tap Run.

To check a different town, change `LAT, LON` at the top of the script.

## Sample output

This is a shortened run from November 6, 2026. The forecast changes, so your output will not match these lines. Temperatures on a **NO** line are rounded to the nearest degree, so a value just under 50 °F can print as `50F too cold`.

```text
2026-11-06 07:00  GO  
2026-11-06 08:00  GO  
2026-11-07 07:00  NO  48F too cold
2026-11-07 08:00  NO  50F too cold
2026-11-07 09:00  GO  

General guide only. Always follow the product label.
```

Other failures use the same shape, for example `wind 18 mph too strong` or `0.72 in rain past 48h, ground soaked`. This run did not hit those rules.

## Build log

Study notes for each session are in the repo: `LESSON_1.md`, `LESSON_2.md`, and `NEXT_SESSION_3.md`.

- **Session 1.** Forecast GO/NO checker. Hourly wind, temperature, rain chance, and expected rain for Brandon, scored for daylight hours.
- **Session 2.** Past 48-hour rain check. If more than 0.50 in fell in the previous 48 hours, that hour is **NO** because soaked ground causes runoff.

## Next up

**Session 3.** After a GO hour, check a spray drying window of 15 to 30 minutes (hotter dries faster) and look for the best watering time, 6 to 8 AM, within the next 24 hours. The products this is aimed at are water-activated, so they need water after they dry, and not during the hottest part of the day.

## The label always wins

This script is a general guide only. **The product label always wins.** Follow its wind, temperature, rain, and application instructions, and your local regulations, over anything this script prints.
