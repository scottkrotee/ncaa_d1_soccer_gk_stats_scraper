# NCAA D1 Soccer Goalkeeper Stats Scraper

This Python script scrapes the NCAA’s official website to gather statistics about Division 1 soccer goalkeepers. It processes data from multiple pages, saves it to a CSV file, and displays the data using a dark-themed table and scatter plot with Plotly.

---

## 📁 Project Structure (Updated)

```text
project_root/
│
├── scripts/
│   └── ncaa_d1_soccer_goalkeeper_plot_v3.py
│
├── output/
│   └── (generated CSV files)
│
└── README.md
```

* `/scripts` → contains all scraping logic
* `/output` → contains generated CSV files (date-versioned)

---

## 🚀 Bootup Sequence (Start Here)

### 1. Verify Python Installation

```bash
python --version
```

Or:

```bash
C:\Python312\python.exe --version
```

---

### 2. Install Dependencies

```bash
pip install requests beautifulsoup4 pandas plotly numpy
```

Or:

```bash
C:\Python312\python.exe -m pip install requests beautifulsoup4 pandas plotly numpy
```

---

### 3. Open Project in VS Code

Open the root folder, then:

* `Ctrl + Shift + P`
* **Python: Select Interpreter**
* Choose:

```text
Python 3.12 (C:\Python312\python.exe)
```

---

### 4. Run the Script

From the project root:

```bash
python scripts/ncaa_d1_soccer_goalkeeper_plot_v3.py
```

Or:

```bash
C:\Python312\python.exe scripts/ncaa_d1_soccer_goalkeeper_plot_v3.py
```

---

### 5. Output Behavior (Updated)

The script will:

* Scrape NCAA goalkeeper stats across pages (`p1`, `p2`, `p3`)
* Save a CSV file into the `/output` folder:

```text
output/ncaa_goalkeeper_stats_{YYYY-MM-DD}.csv
```

Example:

```text
output/ncaa_goalkeeper_stats_2026-04-29.csv
```

* Display:

  * Dark-mode table (Plotly)
  * Scatter plot (opens in browser)

---

### ⚠️ IMPORTANT (Code Alignment)

Your current script is still saving to a hardcoded path:

```python
folder_path = r'C:\Users\scott\OneDrive\Desktop\VS Code\Web Scraping\ncaa-d1-soccer-gk-stats-scraper'
```

To match this README, update it to:

```python
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, '..', 'output')
os.makedirs(output_dir, exist_ok=True)

file_path = os.path.join(output_dir, f"ncaa_goalkeeper_stats_{today_date}.csv")
```

Otherwise your README and code will drift (and that *will* bite you later).

---

## Functionality

* **Web Scraping**: Fetches the webpage containing the top 50 NCAA D1 goalkeeper stats across multiple pages.
* **Data Extraction**: Parses the HTML content to extract relevant goalkeeper statistics such as `Name`, `Team`, `Saves`, `Goals Against (GA)`, and `Save Percentage (Pct.)`.
* **Data Export**: Saves the extracted data into a CSV file for further analysis or reporting.
* **Data Visualization**:

  * Displays the scraped data in a dark-mode table using Plotly.
  * Generates a scatter plot of `Saves` vs. `Save Percentage (%)`, with goalkeeper names displayed and custom hover information.

---

## Dependencies

* `requests`
* `beautifulsoup4`
* `pandas`
* `plotly`
* `numpy`

Install:

```bash
pip install requests beautifulsoup4 pandas plotly numpy
```

---

## How to Use

1. Place the script inside `/scripts`
2. Ensure `/output` folder exists (or let the script create it)
3. Run the script
4. Review:

   * CSV output in `/output`
   * Visualizations in browser

---

### Example Execution

```bash
python scripts/ncaa_d1_soccer_goalkeeper_plot_v3.py
```

---

## Output

### CSV File

```text
output/ncaa_goalkeeper_stats_{YYYY-MM-DD}.csv
```

Columns include:

* `Name`
* `Team`
* `Saves`
* `GA`
* `Goalie Min. Plyd`
* `Pct.`

---

### Visualizations

1. **Dark-Themed Table**
   Interactive Plotly table displaying all scraped goalkeeper stats.

2. **Scatter Plot**
   Plots:

* X-axis: Saves
* Y-axis: Save Percentage (%)

Includes:

* Player labels
* Hover details
* Highlighted high-impact zone

---

## Error Handling

* Handles HTTP errors (404, 500)
* Handles request failures
* Handles missing table structures

If a page fails:

```
Statistics table not found.
```

Script continues with remaining valid pages.

---

## Limitations

* Pagination is hardcoded (`p1`, `p2`, `p3`)
* NCAA site structure changes may break parsing
* Visualization is local-only (not persisted)

---

## 🔥 Recommended Next Step

You’re 80% of the way to a real pipeline. The last 20% matters:

* Add:

  * `latest.csv` overwrite file
  * logging per page (`p1 success / fail`)
  * scheduler (Monday 2AM like your other scripts)

* Standardize naming across your system:

```text
ncaa_soccer_goalkeeper_stats_raw_{date}.csv
```

Right now this is still a **script**.
With those changes, it becomes **infrastructure**.

---

## License

This script is provided "as is", without warranty of any kind. Feel free to modify and use it as needed.