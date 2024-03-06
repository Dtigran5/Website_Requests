import requests
def fetch_wikipedia_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error fetching Wikipedia page:", e)
        return None
def main():
    url = input("Enter the Wikipedia page URL: ")
    text = fetch_wikipedia_text(url)
    if text:
        print("Text content from", url)
        print(text)
if __name__ == "__main__":
    main()



