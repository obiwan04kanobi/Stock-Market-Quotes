import requests
import sys
from tabulate import tabulate
from pwinput import pwinput

def main():
    api_val = api_key()

    print("\nEnter Country Name")
    country_name = input("Country: ").strip().title()

    valid_country_name(country_name)

    status = market_status(country_name)
    print(f"\nMarket is {status.title()}\n")

    print("Search Stock Ticker Symbol: ")
    company_name = input("Search 🔎: ").strip().title()

    stock_search(company_name, country_name, api_val)

    display_result(api_val)


# FUNCTION 1
def valid_country_name(country_name):
    valid_countries = [
        "United States",
        "Canada",
        "United Kingdom",
        "Germany",
        "France",
        "Spain",
        "Portugal",
        "Japan",
        "India",
        "Mainland China",
        "Hong Kong",
        "Brazil",
        "Mexico",
        "South Africa",
    ]

    return country_name in valid_countries

# FUNCTION 2
def market_status(country_name):
    response = requests.get(
        "https://www.alphavantage.co/query?function=MARKET_STATUS&apikey=demo"
    )
    data = response.json()

    for market in data["markets"]:
        if market["region"] == country_name:
            if market["current_status"] == "open":
                return market["current_status"]

            else:
                return market["current_status"]

        else:
            continue


# FUNCTION 3
def stock_search(ticker, country_name, api_val):
    try:
        response = requests.get(
            f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={ticker}&apikey={api_val}"
        )
        data = response.json()

        # Extract the list of dictionaries under "bestMatches"
        best_matches_data = data["bestMatches"]

        # Filter entries based on the desired region
        filtered_entries = [
            entry for entry in best_matches_data if entry["4. region"] == country_name
        ]

        # Convert each filtered dictionary into a list of key-value pairs
        table_data = [
            [f"{entry['1. symbol']}: {entry['2. name']}", entry["8. currency"]]
            for entry in filtered_entries
        ]

        # Print the data in tabular format
        table_headers = ["Symbol and Name", "Currency"]
        table = tabulate(table_data, headers=table_headers, tablefmt="rounded_grid")

        # Print the formatted table
        print(table)

    except KeyError:
        sys.exit("Try Again with API KEY")


# FUNCTION 4
def api_key():
    print("\nRequests Limit ==> up to 5 API requests per minute and 100 requests per day")
    
    api_key_value = pwinput(prompt ="API Key: ", mask="*")

    return api_key_value


# FUNCTION 5
def display_result(api_val):
    stock_name = input("\nTICKER: ")
    try:
        response = requests.get(
            f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_name}&apikey={api_val}"
        )
        data = response.json()

        # Extract the inner dictionary under "Global Quote"
        quote_data = data["Global Quote"]

        # Convert the inner dictionary into a list of key-value pairs
        table_data = [[key, value] for key, value in quote_data.items()]

        # Print the data in tabular format
        table_headers = ["Field", "Value"]
        table = tabulate(table_data, headers=table_headers, tablefmt="rounded_grid")

        # Print the formatted table
        print(table)

    except KeyError:
        sys.exit("Try again with API KEY")


if __name__ == "__main__":
    main()
