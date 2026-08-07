#project name = crypto_tracker inspired by api integration
#devloper = tilak kumar
#project source level2 intermediate
#project number 3 from level 2 intermediate
#============features======================#
#dynamcaly fetch crypto data  in json using coingecko api#
import requests
def get_crypto_price(crypto_id='bitcoin'):
    """Fetches the current price of a cryptocurrency from CoinGecko API."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"

    try:
        response = requests.get(url)
        response.raise_for_status()  

        data = response.json()

        if crypto_id in data:
            price = data[crypto_id]['usd']
            return f"${price}"
        else:
            return "Crypto ID not found."

    except requests.exceptions.ConnectionError:
        return "Error: No internet connection or API is unreachable."
    except requests.exceptions.HTTPError as err:
        return f"HTTP Error: {err}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def main():
    print("--- Codveda Level 2: Crypto Price Tracker ---")
    print("Available IDs: bitcoin, ethereum, dogecoin, solana")

    while True:
        crypto = input("\nEnter crypto ID (or 'exit' to quit): ").lower().strip()

        if crypto == 'exit':
            print("Exiting tracker. Goodbye!")
            break

        if not crypto:
            continue

        print(f"Fetching price for {crypto}...")
        result = get_crypto_price(crypto)
        print(f"Current Price: {result}")


if __name__ == "__main__":
    main()
