from lib.generate_log import generate_log
from lib.fetch_data import fetch_data

# Entry point script for the automation task

if __name__ == "__main__":
    # Collect initial log entries
    log_entries = ["Automation started", "Fetching API data..."]
    
    # Fetch API data
    data = fetch_data()
    # Add title from API response
    log_entries.append(f"API Title: {data.get('title', 'No title found')}")

    # Generate log
    filename = generate_log(log_entries)
    
    print(f"Automation complete. Log saved to: {filename}")
