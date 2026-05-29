import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# LOAD DATASET
# -------------------------

data = pd.read_csv("flight_data.csv")

print("===== AI FLIGHT DELAY PREDICTOR =====")

print("\nDataset Size:", data.shape)

print("\nStatistics")
print(data.describe())

# -------------------------
# BASIC COUNTS
# -------------------------

delay_count = data["Delayed"].value_counts()

on_time = delay_count[0]
delayed = delay_count[1]

# -------------------------
# BAR CHART
# -------------------------

plt.figure(figsize=(6,4))

plt.bar(
    ["On Time","Delayed"],
    [on_time, delayed]
)

plt.title("Flight Delay Count")

plt.show()

# -------------------------
# PIE CHART
# -------------------------

plt.figure(figsize=(6,6))

plt.pie(
    [on_time, delayed],
    labels=["On Time","Delayed"],
    autopct="%1.1f%%"
)

plt.title("Delay Distribution")

plt.show()

# -------------------------
# HISTOGRAM
# -------------------------

plt.figure(figsize=(7,4))

plt.hist(
    data["Distance"],
    bins=10
)

plt.title("Distance Distribution")

plt.xlabel("Distance")

plt.ylabel("Frequency")

plt.show()

# -------------------------
# SCATTER PLOT
# -------------------------

plt.figure(figsize=(7,4))

plt.scatter(
    data["Distance"],
    data["Departure_Hour"]
)

plt.xlabel("Distance")

plt.ylabel("Departure Hour")

plt.title("Distance vs Departure Hour")

plt.show()

# -------------------------
# LINE GRAPH
# -------------------------

delay_day = data.groupby(
    "Day"
)["Delayed"].sum()

plt.figure(figsize=(7,4))

plt.plot(
    delay_day.index,
    delay_day.values,
    marker="o"
)

plt.title("Day Wise Delays")

plt.xlabel("Day")

plt.ylabel("Total Delays")

plt.show()

# -------------------------
# BOX PLOT
# -------------------------

plt.figure(figsize=(6,4))

plt.boxplot(
    data["Distance"]
)

plt.title("Distance Boxplot")

plt.show()

# -------------------------
# AREA CHART
# -------------------------

distance_day = data.groupby(
    "Day"
)["Distance"].mean()

plt.figure(figsize=(7,4))

plt.fill_between(
    distance_day.index,
    distance_day.values
)

plt.title("Average Distance by Day")

plt.xlabel("Day")

plt.ylabel("Average Distance")

plt.show()

# -------------------------
# HORIZONTAL BAR CHART
# -------------------------

airline_delay = data.groupby(
    "Airline"
)["Delayed"].sum()

plt.figure(figsize=(7,4))

plt.barh(
    airline_delay.index.astype(str),
    airline_delay.values
)

plt.title("Airline Delay Comparison")

plt.xlabel("Delays")

plt.ylabel("Airline")

plt.show()

# -------------------------
# AIRLINE ANALYSIS
# -------------------------

plt.figure(figsize=(7,4))

plt.plot(
    airline_delay.index,
    airline_delay.values,
    marker="s"
)

plt.title("Airline Wise Delay Trend")

plt.xlabel("Airline")

plt.ylabel("Delays")

plt.show()

# -------------------------
# PREDICTION SECTION
# -------------------------

print("\n===== Prediction =====")

hour = int(input("Departure Hour: "))
distance = int(input("Distance: "))
day = int(input("Day (1-7): "))
airline = int(input("Airline Code (1-3): "))

score = 0

if hour >= 16:
    score += 1

if distance > 1200:
    score += 1

if day >= 5:
    score += 1

if airline == 3:
    score += 1

probability = (score / 4) * 100

print("\nDelay Probability:",
      round(probability,2),
      "%")

if probability >= 50:
    print("Flight likely DELAYED")
else:
    print("Flight likely ON TIME")
