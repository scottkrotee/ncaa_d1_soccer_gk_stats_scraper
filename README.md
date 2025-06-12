# NCAA D1 Soccer Goalkeeper Stats Scraper

This Python script scrapes the NCAA’s official website to gather statistics about Division 1 soccer goalkeepers. It processes data from multiple pages, saves it to a CSV file, and displays the data using a dark-themed table and scatter plot with Plotly.

## Functionality

- **Web Scraping**: Fetches the webpage containing the top 50 NCAA D1 goalkeeper stats across multiple pages.
- **Data Extraction**: Parses the HTML content to extract relevant goalkeeper statistics such as `Name`, `Team`, `Saves`, `Goals Against (GA)`, and `Save Percentage (Pct.)`.
- **Data Export**: Saves the extracted data into a CSV file (`ncaa_goalkeeper_stats.csv`) for further analysis or reporting.
- **Data Visualization**:
  - Displays the scraped data in a dark-mode table using Plotly.
  - Generates a scatter plot of `Saves` vs. `Save Percentage (%)`, with goalkeeper names displayed and custom hover information.

## Dependencies

To run this script, you'll need Python installed on your system along with the following libraries:

- `requests` for performing HTTP requests to fetch webpage content.
- `BeautifulSoup` from `bs4` for parsing the HTML content of the webpages.
- `pandas` for data manipulation and exporting the results to a CSV file.
- `plotly` for creating interactive visualizations (dark-mode table and scatter plot).

You can install these dependencies using pip:

```bash
pip install requests beautifulsoup4 pandas plotly
```

## How to Use

1. **Download the Script**: Ensure that you have the Python script on your local system.
2. **Install the Dependencies**: Run the command provided above to install the required Python libraries.
3. **Run the Script**: Run the script in a Python environment. It will:
   - Scrape the top goalkeeper statistics from the NCAA website for multiple pages.
   - Save the data into a CSV file named `ncaa_goalkeeper_stats.csv`.
   - Display the data as a dark-themed table and a scatter plot of goalkeeper performance.

### Example Execution

```bash
python ncaa_d1_soccer_goalkeeper_plot_v3.py
```

The script will print the scraping progress, save the data to a CSV file, and display the visualizations directly.

## Output

### CSV File
The scraped goalkeeper statistics are saved to a CSV file called `ncaa_goalkeeper_stats.csv`. The columns include:

- `Name`: Goalkeeper's name
- `Team`: The team the goalkeeper plays for
- `Saves`: The total number of saves
- `GA`: Goals Against
- `Goalie Min. Plyd`: Minutes played
- `Pct.`: Save percentage (in %)

### Visualizations
1. **Dark-Themed Table**: A Plotly-based interactive table showing all the scraped data in a dark mode for a visually appealing presentation.
   
2. **Scatter Plot**: A scatter plot of goalkeeper performance, plotting `Saves` against `Save Percentage (%)`. High-performing goalkeepers are highlighted with custom hover information and annotations.

## Error Handling

The script includes basic error handling for:

- **HTTP Errors**: Handles failed HTTP requests (e.g., 404 or 500 errors).
- **Request Exceptions**: Handles general request-related exceptions.
- **Data Parsing**: Handles cases where the expected table structure or data is not found.

If an error occurs, an appropriate error message will be printed to the console, helping you diagnose the issue.

## Limitations

- **Pagination**: The script currently handles multiple pages of statistics, but the number of pages is hardcoded. The NCAA website may change its structure, which would require updating the `pages` list.
- **Website Changes**: Any significant changes to the NCAA website’s layout (e.g., table structure or URLs) may require modifications to the script.

## License

This script is provided "as is", without warranty of any kind, express or implied. Feel free to modify and use it as needed.
