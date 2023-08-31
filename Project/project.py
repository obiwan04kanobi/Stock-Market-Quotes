import requests
import sys
import json

def main():
    print("Do you have an API KEY (Y for Yes & N for NO) ?")
    api_key_bool = input("Enter: ").upper()

    api_key(api_key_bool)

    if api_key(api_key_bool) == None:
        sys.exit("Enter Y for Yes & N for NO ")

    print("Enter Country: ")
    country_name = input("Country Name: ").strip().title()

    valid_country_name(country_name)

    status = market_status(country_name, api_key_bool)
    print(f"Market is {status}")

    print("Enter Stock Ticker Symbol: ")
    company_name = input("Ticker Symbol: ").strip().upper()



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

    for name in valid_countries:
        if name == country_name:
            return True
        else:
            return False


# FUNCTION 2
def market_status(country_name, api_key_bool):
    if api_key(api_key_bool) == False:
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

    elif api_key(api_key_bool) == True:
        api_key_value = input("API Key: ")

        response = requests.get(
            f"https://www.alphavantage.co/query?function=MARKET_STATUS&apikey={api_key_value}"
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


# FUNCTION 4
def api_key(api_key_bool):
    if api_key_bool == "Y":
        print("API Request Limit: 5 API requests per minute and 100 requests per day\n")
        return True

    elif api_key_bool == "N":
        return False

    else:
        return None


if __name__ == "__main__":
    main()
