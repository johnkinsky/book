# Script to get and display PyPi.org package data.

# Requires pypistats, matplotlib, and numpy
# https://pypistats.org/api/
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
# https://numpy.org/doc/2.3/reference/generated/numpy.polyfit.html
# https://numpy.org/doc/2.3/reference/generated/numpy.polyval.html
# 
import subprocess
import json
import csv
import base64
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as npy
from datetime import datetime, timedelta
from io import BytesIO

# Define start and end date variable based on current system time. 
# Hardcode valued for past three months. Change this as needed.
start_date = datetime.now() - timedelta(days=91)
# Exclude today since it is always zero.
end_date = datetime.now() - timedelta(days=1)

# Define appended output file names
dataFileName = "download_data.csv"
htmlFileName = "download_data.html"

# Package names: https://pypi.org/search/?q=&o=-created&c=Natural+Language+%3A%3A+English
def get_packages():
    pypiName = input("Enter a valid package name from PyPi.org: ").strip()
    return pypiName
# Use these known package names for testing
# matplotlib - very large activity
# breathe - moderate activity
# openseries - limited activity

# Get packages. Use the .split approach for later expansion when adding more package names.
packages = get_packages().split()

# Define full output file names (fully joined)
package_prefix = packages[0]
dataFileName = f"{package_prefix}_{dataFileName}"
htmlFileName = f"{package_prefix}_{htmlFileName}"

# Get full download stats between start_date and end_date.
# Use JSON because the API doesn't seem to work otherwise.
def get_package_stats(packagename, day):
    day_str = day.strftime('%Y-%m-%d')
    result = subprocess.run([
        'pypistats',
        'overall',
        packagename,
        '-sd', day_str,
        '-ed', day_str,
        '-f', 'json'
    ], capture_output=True, text=True)
    return json.loads(result.stdout)

# Data structure chart
series_data = {pkg: [] for pkg in packages}

# Write data to CSV file
with open(dataFileName, 'w', newline='') as csvfile:
    fieldnames = ['packagename', 'date', 'total']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    current_day = start_date
    while current_day <= end_date:
        for package in packages:
            try:
                stats = get_package_stats(package, current_day)
                total_downloads = sum(item['downloads'] for item in stats.get('data', []))
                writer.writerow({
                    'packagename': package,
                    'date': current_day.strftime('%Y-%m-%d'),
                    'total': total_downloads
                })
                # Save for plotting data.
                series_data[package].append((current_day.strftime('%Y-%m-%d'), total_downloads))
            except Exception as e:
                print(f"Error processing {package} on {current_day}: {e}")
        current_day += timedelta(days=1)

print("Full data saved to " + dataFileName + ".")

# Generate chart using matplotlib.pyplot
package = packages[0]
points = series_data[package]

dates = [datetime.strptime(d, "%Y-%m-%d") for d, _ in points]
values = [v for _, v in points]

# Determine lower and upper boundaries
y_min = min(values)
y_max = max(values)

# Add padding so the chart easier to read
padding = (y_max - y_min) * 0.1  # 10% padding

# Define chart for x-y comparison and pass attributes to chart object
fig, xy = plt.subplots(figsize=(12, 6))
xy.plot(
    dates,
    values,
    marker='o',
    linestyle='solid',
    linewidth='1',
    markersize='3',
    color='blue',
    label=package,
)

# Find trendline using numpy (Using older methods because I understand them.)
x_numeric = npy.arange(len(values))
coeffs = npy.polyfit(x_numeric, values, 1)
trendline = npy.polyval(coeffs, x_numeric)
xy.plot(dates, trendline, color='red', linewidth=1, linestyle='dashed', label='Trendline')

# Use dynamic y-axis range
xy.set_ylim(y_min - padding, y_max + padding)

# Format values for thousands
def format_value(v):
    if v >= 1000:
        return f"{v/1000:,.1f}K"
    return f"{v:,}"

# Find values for minimum and maximum downloads
min_index = values.index(y_min)
max_index = values.index(y_max)
for i, (x, y) in enumerate(zip(dates, values)):
    if i == min_index or i == max_index:
        xy.text(
            x, y,
            format_value(y),
            ha='center',
            va='bottom',
            fontsize=10,
            color='red'
        )

# Format y-axis values using mticker
xy.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, pos: format_value(v)))

# Format chart
xy.set_title("PyPi Downloads")
xy.set_xlabel("Date")
xy.set_ylabel("Downloads")
xy.grid(True, linestyle='--', alpha=0.5)
xy.legend()

# Save to memory buffer as png format
buffer = BytesIO()
plt.savefig(buffer, format="png")
buffer.seek(0)
img_base64 = base64.b64encode(buffer.read()).decode("utf-8")
buffer.close()

# Write HTML content
html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>PyPI Download Statistics for {package} package</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sansation:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap" rel="stylesheet">
<style>body {{margin: 30px;}}h1, h2, p, a {{font-family: 'Sansation', sans-serif;}}</style>
<body>
<h1>PyPi Download Statistics for "{package}" package.</h1>
<p>This chart shows PyPi (pip) download activity for the past three months and shows the activity trend. (Values shown only for the highest and lowest downloads.)</p>
<p><img src="data:image/png;base64,{img_base64}" alt="{package} Download Chart"></p>
<p>Save PNG version of the <a download="{package}_chart.png" href="data:image/png;base64,{img_base64}">chart</a>.</p>
<p>Download the <strong>{package}</strong> data contained in the <a href="{dataFileName}">{dataFileName}</a> file.</p>
</body>
</html>
"""
with open(htmlFileName, "w") as f:
    f.write(html_content)
print("HTML container saved to " + htmlFileName + ".")
