import requests
import sys
import json


def main():
    print("Enter the name of the country you want stock quotes for: ")
    country_name = input("Country Name: ").strip().title()

    market_status(country_name)


def market_status(name):
    response = requests.get(
        "https://www.alphavantage.co/query?function=MARKET_STATUS&apikey=demo"
    )
    data = response.json()

    valid_countries = ["United States","Canada","United Kingdom","Germany","France",
                       "Spain","Portugal","Japan","India","Mainland China",
                       "Hong Kong","Brazil","Mexico","South Africa"]

    for market in data["markets"]:
        if market["region"] == name:
            if market["current_status"] == "open":
                print("Market is open")
                break
            else:
                print("Market is closed")
                break
        
        elif name not in valid_countries:
            print("Not a Valid Country name")
            break
        
        else:
            continue


if __name__ == "__main__":
    main()
