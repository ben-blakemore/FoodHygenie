import requests

def main():
    r = requests.get('https://api.ratings.food.gov.uk/Establishments', params={'name':"Picnic Coffee"}, headers={"x-api-version":"2"})
    print(r.url)
    print(r.json())

if __name__ == "__main__":
    main()