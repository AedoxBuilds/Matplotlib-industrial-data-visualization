"""
Industrial Data Visualization Using Matplotlib
Manufacturing Production Dashboard - Assignment

Part 1 - Production Trend Analysis
"""

import matplotlib.pyplot as plt
import os

# Ensure outputs folder exists
os.makedirs("outputs", exist_ok=True)

# ===========================================================
# Part 1 - Production Trend Analysis
# ===========================================================

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
production = [1200, 1350, 1280, 1500, 1600, 1550, 1700]

plt.figure(figsize=(9, 5))
plt.plot(
    days,
    production,
    marker="o",          # circular markers at each data point
    linestyle="-",        # solid line
    color="#2E86AB",
    linewidth=2,
)

plt.title("Weekly Production Trend", fontsize=14, fontweight="bold")
plt.xlabel("Day of the Week")
plt.ylabel("Units Produced")
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("outputs/production_trend.png", dpi=150)
plt.show()

# --- Business Question: On which day was production highest? ---
max_index = production.index(max(production))
print(f"Highest production day: {days[max_index]} ({production[max_index]} units)")


# ===========================================================
# Part 2 - Machine Temperature Monitoring
# ===========================================================

hours = [9, 10, 11, 12, 13, 14, 15, 16, 17]
temperature = [65, 68, 72, 75, 79, 82, 85, 81, 76]

plt.figure(figsize=(9, 5))
plt.plot(
    hours,
    temperature,
    marker="o",           # circular markers
    linestyle="-",
    color="#C73E1D",
    linewidth=2,
)

plt.title("Machine Temperature Throughout the Working Day", fontsize=14, fontweight="bold")
plt.xlabel("Hour of the Day")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.6)

# Reference line for the safe operating limit
plt.axhline(y=80, color="black", linestyle=":", linewidth=1.5, label="Safe Limit (80°C)")
plt.legend()

plt.tight_layout()
plt.savefig("outputs/temperature_analysis.png", dpi=150)
plt.show()

# --- Challenge: hours where temperature exceeded 80°C ---
over_limit = [h for h, t in zip(hours, temperature) if t > 80]
print(f"Hours exceeding 80°C: {over_limit}")


# ===========================================================
# Part 3 - Production vs Defective Products
# ===========================================================

total_products = [1200, 1350, 1280, 1500, 1600, 1550, 1700]
defective_products = [35, 42, 30, 55, 48, 60, 45]

plt.figure(figsize=(9, 5))
plt.plot(
    days,
    total_products,
    marker="o",
    linestyle="-",
    color="#2E86AB",
    linewidth=2,
    label="Total Production",
)
plt.plot(
    days,
    defective_products,
    marker="s",            # square markers to distinguish from line 1
    linestyle="--",         # dashed line to distinguish from line 1
    color="#C73E1D",
    linewidth=2,
    label="Defective Products",
)

plt.title("Total Production vs Defective Products", fontsize=14, fontweight="bold")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Units")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("outputs/defect_analysis.png", dpi=150)
plt.show()

# --- Business Question: which day had the most defective products? ---
max_defect_index = defective_products.index(max(defective_products))
print(f"Day with most defects: {days[max_defect_index]} ({defective_products[max_defect_index]} defective units)")


# ===========================================================
# Part 4 - Product Quality Analysis (Defect Percentage)
# ===========================================================

defect_percentage = [(d / t) * 100 for d, t in zip(defective_products, total_products)]

plt.figure(figsize=(9, 5))
plt.plot(
    days,
    defect_percentage,
    marker="D",           # diamond markers
    linestyle="-",
    color="#8E44AD",
    linewidth=2,
)

plt.title("Daily Defect Percentage", fontsize=14, fontweight="bold")
plt.xlabel("Day of the Week")
plt.ylabel("Defect Percentage (%)")
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("outputs/defect_percentage.png", dpi=150)
plt.show()

# --- Challenge: highest/lowest defect % and average ---
max_pct_idx = defect_percentage.index(max(defect_percentage))
min_pct_idx = defect_percentage.index(min(defect_percentage))
avg_pct = sum(defect_percentage) / len(defect_percentage)
print(f"Highest defect %: {days[max_pct_idx]} ({defect_percentage[max_pct_idx]:.2f}%)")
print(f"Lowest defect %: {days[min_pct_idx]} ({defect_percentage[min_pct_idx]:.2f}%)")
print(f"Average defect %: {avg_pct:.2f}%")


# ===========================================================
# Part 5 - Industrial Performance Comparison (Machines)
# ===========================================================
# A bar chart is the right choice here (not a line chart) because
# the three machines are separate, unordered categories, not a
# continuous trend over time.

machines = ["Machine A", "Machine B", "Machine C"]
machine_production = [8500, 9200, 7800]

plt.figure(figsize=(9, 5))
bars = plt.bar(machines, machine_production, color=["#2E86AB", "#F5A623", "#C73E1D"])

plt.title("Production Comparison Across Machines", fontsize=14, fontweight="bold")
plt.xlabel("Machine")
plt.ylabel("Units Produced")

# Label each bar with its value for readability
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 50, str(height),
              ha="center", va="bottom", fontsize=10)

plt.tight_layout()
plt.savefig("outputs/machine_performance.png", dpi=150)
plt.show()

# --- Business Question: which machine has the highest output? ---
best_machine_idx = machine_production.index(max(machine_production))
print(f"Best performing machine: {machines[best_machine_idx]} ({machine_production[best_machine_idx]} units)")


# ===========================================================
# Part 6 - Professional Plot Styling
# ===========================================================
# Taking Part 1's production trend and giving it a presentation-ready
# treatment: larger figure, refined colors, an annotation on the peak
# value, and a subtler grid.

plt.figure(figsize=(10, 6))
plt.plot(
    days,
    production,
    marker="o",
    markersize=8,
    linestyle="-",
    linewidth=2.5,
    color="#1B4965",
    label="Weekly Production",
)

peak_day_idx = production.index(max(production))
plt.annotate(
    f"Peak: {production[peak_day_idx]} units",
    xy=(days[peak_day_idx], production[peak_day_idx]),
    xytext=(peak_day_idx - 1.5, production[peak_day_idx] + 60),
    arrowprops=dict(arrowstyle="->", color="black"),
    fontsize=10,
)

plt.title("Weekly Production Trend — Presentation View", fontsize=15, fontweight="bold")
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Units Produced", fontsize=12)
plt.legend(loc="lower right")
plt.grid(True, linestyle="--", alpha=0.4)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

plt.tight_layout()
plt.savefig("outputs/production_trend_professional.png", dpi=150)
plt.show()


# ===========================================================
# Part 7 - Real-World Visualization Problem (Speed vs Temperature)
# ===========================================================
# Speed (40-60) and temperature (60-83) sit in different ranges, so a
# twin y-axis keeps both readable on one chart instead of squashing one.

time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
machine_speed = [40, 45, 48, 52, 55, 58, 60, 59, 55, 50]
temperature_p7 = [60, 62, 65, 68, 72, 76, 80, 83, 81, 78]

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(time, machine_speed, marker="o", linestyle="-", color="#2E86AB", linewidth=2, label="Machine Speed")
ax1.set_xlabel("Time (minutes)")
ax1.set_ylabel("Machine Speed (units/min)", color="#2E86AB")
ax1.tick_params(axis="y", labelcolor="#2E86AB")
ax1.grid(True, linestyle="--", alpha=0.5)

ax2 = ax1.twinx()
ax2.plot(time, temperature_p7, marker="s", linestyle="--", color="#C73E1D", linewidth=2, label="Temperature")
ax2.set_ylabel("Temperature (°C)", color="#C73E1D")
ax2.tick_params(axis="y", labelcolor="#C73E1D")

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

plt.title("Machine Speed vs Temperature Over Time", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/speed_temperature_relationship.png", dpi=150)
plt.show()

# --- Engineering Question: does temperature rise as speed rises? ---
print(
    "Engineering observation: Temperature and machine speed rise together for "
    "most of the run — as speed climbs from 40 to 60 units/min (minutes 1-7), "
    "temperature climbs from 60C to 80C in step. Past minute 7, speed starts "
    "easing off (60 -> 50) and temperature keeps rising slightly before it "
    "peaks at minute 8 (83C) and then falls, suggesting temperature lags "
    "speed by about one interval - consistent with heat build-up/dissipation "
    "taking a moment to catch up with mechanical load."
)


# ===========================================================
# Part 8 - Error Detection Challenge
# ===========================================================
# Original (buggy) code from the assignment:
#
#   import matplotlib.pyplot as plt
#   days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
#   production = [1000, 1200, 1150, 1400, 1350]
#   plt.plot(days production)
#   plt.title("Weekly Production")
#   plt.xlabel("Days")
#   plt.ylabel("Production")
#   plt.show
#
# Errors found:
#   1. `plt.plot(days production)` - missing comma between the two
#      arguments -> SyntaxError. Should be `plt.plot(days, production)`.
#   2. `plt.show` - the function is referenced but never called (missing
#      parentheses) -> no window/figure is actually displayed.
#      Should be `plt.show()`.
#
# Corrected version:

days_p8 = ["Mon", "Tue", "Wed", "Thu", "Fri"]
production_p8 = [1000, 1200, 1150, 1400, 1350]

plt.figure(figsize=(9, 5))
plt.plot(days_p8, production_p8, marker="o", linestyle="-", color="#2E86AB")
plt.title("Weekly Production")
plt.xlabel("Days")
plt.ylabel("Production")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("outputs/part8_corrected.png", dpi=150)
plt.show()


# ===========================================================
# Part 9 - Mini Industrial Project: Machine Production Monitoring Report
# ===========================================================
# Note on the data: the assignment gives `temperature` as 9 hourly
# readings (for hours 9-17), while `days`/`production`/`defects` are
# 7 daily values. These aren't the same axis, so Chart 3 below reuses
# the hourly view (like Part 2) rather than forcing 9 values onto a
# 7-day axis. Charts 1 and 2 are the final, presentation-ready
# versions and are saved under the same filenames as Parts 1 and 3 -
# this matches the assignment's own Output Folder listing, which
# expects exactly one file per chart type.

days_p9 = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
production_p9 = [1200, 1350, 1280, 1500, 1600, 1550, 1700]
defects_p9 = [35, 42, 30, 55, 48, 60, 45]
hours_p9 = [9, 10, 11, 12, 13, 14, 15, 16, 17]
temperature_p9 = [65, 68, 72, 75, 79, 82, 85, 81, 76]

# Chart 1 - Production Trend (final version -> production_trend.png)
plt.figure(figsize=(9, 5))
plt.plot(days_p9, production_p9, marker="o", linestyle="-", color="#2E86AB", linewidth=2)
plt.title("Machine Production Monitoring Report - Weekly Production", fontsize=13, fontweight="bold")
plt.xlabel("Day of the Week")
plt.ylabel("Units Produced")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("outputs/production_trend.png", dpi=150)
plt.show()

# Chart 2 - Defect Analysis (final version -> defect_analysis.png)
plt.figure(figsize=(9, 5))
plt.plot(days_p9, defects_p9, marker="s", linestyle="--", color="#C73E1D", linewidth=2)
plt.title("Machine Production Monitoring Report - Defective Products", fontsize=13, fontweight="bold")
plt.xlabel("Day of the Week")
plt.ylabel("Defective Units")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("outputs/defect_analysis.png", dpi=150)
plt.show()

# Chart 3 - Machine Temperature (final version -> temperature_analysis.png)
plt.figure(figsize=(9, 5))
plt.plot(hours_p9, temperature_p9, marker="o", linestyle="-", color="#8E44AD", linewidth=2)
plt.axhline(y=80, color="black", linestyle=":", linewidth=1.5, label="Safe Limit (80°C)")
plt.title("Machine Production Monitoring Report - Temperature", fontsize=13, fontweight="bold")
plt.xlabel("Hour of the Day")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("outputs/temperature_analysis.png", dpi=150)
plt.show()

print("Mini project complete: production_trend.png, defect_analysis.png, "
      "and temperature_analysis.png regenerated as final report charts.")
