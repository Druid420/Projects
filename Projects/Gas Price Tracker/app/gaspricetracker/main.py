import requests


#exposed gasbuddy GraphQL endpoint
url = 'https://www.gasbuddy.com/graphql'

#Set headers
headers = {
  "Content-Type": "application/json",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

#JSON payload sent to server
payload = {
    "variables": {
      "search": "21502"
    },
    "query": """
        query locationBySearchTerm($search: String) {
            locationBySearchTerm(search: $search) {
                trends {
                    areaName
                    country
                    today
                    todayLow
                }
            }
        }
    """,

  }

#send POST request with JSON data
response = requests.post(url, json=payload, headers = headers)

print(response.status_code)
print(response.text)