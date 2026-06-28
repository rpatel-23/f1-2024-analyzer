import fastf1
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set up the cache (same as before)
os.makedirs("cache", exist_ok=True)
fastf1.Cache.enable_cache("cache")

season = 2024
schedule = fastf1.get_event_schedule(season)

# Only keep real races (round number 1 and up — skips pre-season testing)
races = schedule[schedule["RoundNumber"] >= 1]

# We'll tally up each driver's total points across the whole season
driver_points = {}

print(f"Loading {season} season results... (this may take a minute)")

for _, event in races.iterrows():
    round_num = event["RoundNumber"]
    try:
        session = fastf1.get_session(season, round_num, "R")  # "R" = the race
        session.load()
        results = session.results

        for _, row in results.iterrows():
            driver = row["Abbreviation"]   # e.g. "VER", "NOR"
            points = row["Points"]
            if driver not in driver_points:
                driver_points[driver] = 0
            driver_points[driver] += points

        print(f"  Round {round_num}: {event['EventName']} loaded")
    except Exception as e:
        print(f"  Round {round_num}: skipped ({e})")

# Turn the totals into a sorted table (highest points first)
standings = pd.DataFrame(
    list(driver_points.items()), columns=["Driver", "Points"]
).sort_values("Points", ascending=False).reset_index(drop=True)

print()
print(f"--- {season} Final Driver Standings ---")
print(standings.to_string(index=False))
# Save the standings so other scripts can use them without reloading everything
standings.to_csv("driver_standings_2024.csv", index=False)
print()
print("Saved to driver_standings_2024.csv")