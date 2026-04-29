import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.graph_objects as go
import os
from datetime import datetime
from pathlib import Path

# Base URL and page identifiers for NCAA D1 goalkeeper stats
base_url = "https://www.ncaa.com/stats/soccer-men/d1/current/individual/421/"
pages = ["p1", "p2", "p3"]


# =========================
# PROJECT PATH CONFIGURATION
# =========================
# Expected project structure:
#
# project_root/
# ├── scripts/
# │   └── ncaa_d1_soccer_goalkeeper_plot_v3.py
# ├── output/
# │   └── generated CSV files
# └── README.md
#
# This script assumes it lives inside /scripts.
# Output files are written one level up into /output.

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUT_DIR = PROJECT_ROOT / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def scrape_ncaa_soccer_stats(url):
    try:
        print(f"Scraping: {url}")

        response = requests.get(url, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        stats_table = soup.find("table")
        if not stats_table:
            print(f"⚠️ Statistics table not found for URL: {url}")
            return None, None

        headers = [header.text.strip() for header in stats_table.find_all("th")]

        rows = []
        for row in stats_table.find_all("tr")[1:]:
            cols = row.find_all("td")
            cols = [ele.text.strip() for ele in cols]

            if cols:
                rows.append(cols)

        print(f"✅ Collected {len(rows)} rows")
        return headers, rows

    except requests.HTTPError as e:
        print(f"HTTP Error occurred: {e.response.status_code} for URL: {url}")
        return None, None
    except requests.RequestException as e:
        print(f"Request exception for URL {url}: {e}")
        return None, None
    except Exception as e:
        print(f"An error occurred for URL {url}: {e}")
        return None, None


all_rows = []
all_headers = None

for page in pages:
    url = base_url + page
    headers, rows = scrape_ncaa_soccer_stats(url)

    if headers and rows:
        all_headers = headers
        all_rows.extend(rows)
    else:
        print(f"⚠️ Skipped {page} — no rows found")


if all_headers and all_rows:
    df = pd.DataFrame(all_rows, columns=all_headers)

    today_date = datetime.today().strftime("%Y-%m-%d")

    # =========================
    # EXPORT CONFIGURATION
    # =========================
    # Date-stamped file preserves historical scraper runs.
    # Latest file gives downstream tools a stable filename to read.
    #
    # Example outputs:
    # output/ncaa_goalkeeper_stats_2026-04-29.csv
    # output/ncaa_goalkeeper_stats_latest.csv

    dated_file_path = OUTPUT_DIR / f"ncaa_goalkeeper_stats_{today_date}.csv"
    latest_file_path = OUTPUT_DIR / "ncaa_goalkeeper_stats_latest.csv"

    df.to_csv(dated_file_path, index=False)
    df.to_csv(latest_file_path, index=False)

    print(f"✅ Data saved successfully to: {dated_file_path}")
    print(f"✅ Latest file updated at: {latest_file_path}")

    df["Saves"] = pd.to_numeric(df["Saves"], errors="coerce")

    if "Pct." in df.columns:
        df["Pct."] = (
            df["Pct."]
            .astype(str)
            .str.rstrip("%")
        )
        df["Pct."] = pd.to_numeric(df["Pct."], errors="coerce")

        # If NCAA provides decimals like .875, convert to percentage scale.
        if df["Pct."].max(skipna=True) <= 1:
            df["Pct."] = df["Pct."] * 100

    def display_table(df):
        fig = go.Figure(data=[go.Table(
            header=dict(
                values=list(df.columns),
                fill_color="black",
                font=dict(color="white", size=12),
                align="left"
            ),
            cells=dict(
                values=[df[col] for col in df.columns],
                fill_color="darkslategray",
                font=dict(color="white", size=11),
                align="left"
            )
        )])

        fig.update_layout(
            title="Top NCAA Goalkeeper Stats (Dark Mode)",
            title_x=0.5,
            paper_bgcolor="black",
            font=dict(color="white")
        )

        fig.show()

    def display_scatter(df):
        required_cols = ["Name", "Team", "Saves", "GA", "Goalie Min. Plyd", "Pct."]
        missing_cols = [col for col in required_cols if col not in df.columns]

        if missing_cols:
            print(f"⚠️ Skipping scatter plot. Missing columns: {missing_cols}")
            return

        plot_df = df.dropna(subset=["Saves", "Pct."]).copy()

        if plot_df.empty:
            print("⚠️ Skipping scatter plot. No valid Saves / Pct. data found.")
            return

        fig = go.Figure()

        hover_text = [
            f"Name: {row['Name']}<br>"
            f"Team: {row['Team']}<br>"
            f"Saves: {row['Saves']}<br>"
            f"GA: {row['GA']}<br>"
            f"Minutes Played: {row['Goalie Min. Plyd']}<br>"
            f"Save Pct: {row['Pct.']}"
            for _, row in plot_df.iterrows()
        ]

        fig.add_trace(go.Scatter(
            x=plot_df["Saves"],
            y=plot_df["Pct."],
            mode="markers+text",
            marker=dict(
                size=18,
                color="blue",
                opacity=0.7,
                line=dict(width=2, color="white")
            ),
            text=plot_df["Name"],
            textposition="top center",
            textfont=dict(color="white"),
            hovertext=hover_text,
            hoverinfo="text"
        ))

        fig.update_layout(
            title="Goalkeepers: Saves vs. Save Percentage",
            xaxis_title="Saves",
            yaxis_title="Save Percentage (%)",
            plot_bgcolor="black",
            paper_bgcolor="black",
            font=dict(color="white")
        )

        fig.update_xaxes(
            showgrid=True,
            gridwidth=0.5,
            gridcolor="rgba(255,255,255,0.1)",
            zeroline=False,
            color="white"
        )

        fig.update_yaxes(
            showgrid=True,
            gridwidth=0.5,
            gridcolor="rgba(255,255,255,0.1)",
            zeroline=False,
            color="white"
        )

        max_saves = plot_df["Saves"].max()
        max_pct = plot_df["Pct."].max()

        fig.add_annotation(
            x=max_saves - 5,
            y=max_pct - 0.02,
            text="High Impact Goalkeepers",
            showarrow=False,
            font=dict(size=20, color="red"),
            bgcolor="rgba(50, 50, 50, 0.6)",
            bordercolor="white",
            borderwidth=2,
            borderpad=10
        )

        fig.show()

    display_table(df)
    display_scatter(df)

else:
    print("No data to display.")