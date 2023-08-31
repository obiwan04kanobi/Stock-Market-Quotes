# Stock Market Data Retrieval Tool

This is a Python script that interacts with the Alpha Vantage API to retrieve and display stock market data. It allows you to search for stock ticker symbols and display various information about the stocks, including their current values. The script uses the `requests` library for making API calls and the `tabulate` library for formatting and displaying tabular data.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- `tabulate` library (`pip install tabulate`)
- An API key from Alpha Vantage. You can sign up for a free API key on their [website](https://www.alphavantage.co/support/#api-key).

## Getting Started

1. Clone this repository to your local machine or download the `project.py` file directly.
2. Open a terminal or command prompt and navigate to the directory containing `project.py`.

## API Rate Limits

Please note that the Alpha Vantage API has rate limits: up to 5 API requests per minute and 100 requests per day. Make sure to stay within these limits to avoid any disruptions.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/Stock-Market-Quotes.git
```

2. Navigate to the cloned directory:

```bash
cd Stock-Market-Quotes
```

## Usage

1. Open a terminal and navigate to the directory where you cloned the repository.

2. Run the script using Python:

```bash
python project.py
```

3. The script will prompt you for your Alpha Vantage API key, which you can obtain from their website.

4. Enter the name of the country you want to search for. Valid options include: United States, Canada, United Kingdom, Germany, France, Spain, Portugal, Japan, India, Mainland China, Hong Kong, Brazil, Mexico, South Africa.

5. The script will display the current market status for the selected country.

6. You can then search for a stock ticker symbol by entering the company name. The script will display a table of matching symbols and names.

7. After selecting a stock symbol from the table, the script will retrieve and display detailed information about that stock.

## Functionality

### 1. `valid_country_name(country_name)`

This function checks if the entered country name is valid. Valid country names are predefined in the function and include countries like the United States, Canada, United Kingdom, etc.

### 2. `market_status(country_name)`

This function retrieves the market status for a given country using the Alpha Vantage API. It indicates whether the market is open or closed.

### 3. `stock_search(ticker, country_name, api_val)`

This function searches for stock ticker symbols based on the provided keyword. It filters the search results based on the desired region (country name) and displays the results in a tabular format.

### 4. `api_key()`

This function prompts the user to input their Alpha Vantage API key. It also provides information about the API's request limits.

### 5. `display_result(api_val)`

This function displays detailed information about a specific stock based on its ticker symbol. It retrieves data using the Alpha Vantage API and presents it in a tabular format.

## Note

- The Alpha Vantage API key is required for using this script. If you encounter issues related to the API key, please ensure you have a valid key and have entered it correctly.
## Disclaimer

This script is provided for educational and informational purposes only. The accuracy of the stock market data and the availability of the Alpha Vantage API are beyond the control of the script author.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to contribute to the project, report issues, or suggest improvements. Happy investing! 📈
