import fastf1
import pandas as pd

# FastF1 downloads data from the web and caches it locally so it's fast next time.
# We make a folder for that cache.
import os
os.makedirs("cache", exist_ok=True)
fastf1.Cache.enable_cache("cache")

# Get the 2024 season schedule
season = 2024
schedule = fastf1.get_event_schedule(season)

# Print out the races in the 2024 season
print(f"--- {season} F1 Season ---")
print(f"Number of events: {len(schedule)}")
print()
print(schedule[["RoundNumber", "EventName", "Country"]].to_string(index=False))