import pandas as pd
import matplotlib.pyplot as plt

# Read the standings we saved earlier
standings = pd.read_csv("driver_standings_2024.csv")

# Sort so the highest scorer ends up at the TOP of the chart
standings = standings.sort_values("Points", ascending=True)

# Build a horizontal bar chart
plt.figure(figsize=(10, 8))
plt.barh(standings["Driver"], standings["Points"], color="#E10600")  # F1 red
plt.xlabel("Total Points")
plt.title("2024 Formula 1 Driver Standings")

# Write each driver's point total at the end of their bar
for index, value in enumerate(standings["Points"]):
    plt.text(value + 2, index, str(int(value)), va="center")

plt.tight_layout()
plt.savefig("driver_standings_2024.png", dpi=150)  # save the image
print("Chart saved as driver_standings_2024.png")
plt.show()  # also pop it open in a window