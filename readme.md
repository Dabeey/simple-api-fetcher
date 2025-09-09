# Simple API Fetcher

A Python project for fetching, analyzing, and visualizing sports league data from [TheSportsDB API](https://www.thesportsdb.com/). This tool retrieves league information, saves it to CSV files, and generates basic analytics and visualizations.

## Features

- Fetch all sports leagues and save to `All_leagues.csv`
- Fetch details for a specific league and save to `Upcoming-League.csv`
- Analyze league data by sport and country
- Generate bar charts of league counts per sport
- Export summary statistics to `league_summary.csv`

## Requirements

See `requirements.txt` for dependencies. Main packages include:
- `requests`
- `pandas`
- `matplotlib`

Install dependencies with:

```sh
pip install -r requirements.txt
```

## Usage

1. **Fetch All Leagues**

   The script automatically fetches all leagues and saves them to `All_leagues.csv` when run.

2. **Fetch Upcoming Events for a League**

   Call `fetch_upcoming_events(league_id)` in `main.py` with the desired league ID.

3. **Analytics & Visualization**

   The script reads `All_leagues.csv`, analyzes the data, and displays a bar chart of leagues per sport. It also saves a summary to `league_summary.csv`.

## Example

```python
from main import fetch_all_leagues, fetch_upcoming_events

fetch_all_leagues()
fetch_upcoming_events('4328')  # Example league ID
```

## Output Files

- `All_leagues.csv`: All leagues data
- `Upcoming-League.csv`: Details for a specific league
- `league_summary.csv`: Summary statistics
- `my_plot.png`: Bar chart visualization (optional, uncomment in code)

## License

This project is for educational and research purposes.

---

**Author:** Dabeey Mercy 
**API Source:** [TheSportsDB](https://www.thesportsdb.com/)