import sys
import time
import requests

# Your SerpApi key
API_KEY = "a206e89dadb0b3c6e75c9dd29e485c0ed3200d77e81c7f08dc83e84206eaf688"

# List of queries
queries = [
    'site:{url} filetype:env OR filetype:txt OR filetype:log',
    'site:{url} inurl:admin OR inurl:login OR inurl:dashboard',
    'site:{url} "SQL syntax" OR "database error"',
    'site:{url} "API Key" OR "secret" OR "token"',
    'site:{url} "user" AND ("password" OR "pass" OR "secret")',
    'site:{url} inurl:config OR inurl:configuration OR inurl:settings',
    'site:{url} "Error" OR "Warning" OR "Exception"',
    'site:{url} "backup" OR "dump"',
    'site:{url} inurl:uploads OR inurl:downloads OR inurl:files',
    'site:{url} "deprecated" OR "obsolete" OR "legacy"',
    'site:{url} intitle:index.of',
    'site:{url} filetype:js "password" OR "username"',
    'site:{url} "<!--" OR "<!DOCTYPE"',
    'site:{url} filetype:json OR filetype:xml'
]

def main(url):
    results = []
    
    for query in queries:
        formatted_query = query.format(url=url)
        print(f"Running query: {formatted_query}")
        
        # API request to SerpApi
        params = {
            "engine": "google",
            "q": formatted_query,
            "api_key": API_KEY,
            "num": 10
        }
        response = requests.get("https://serpapi.com/search", params=params)
        
        if response.status_code == 200:
            data = response.json()
            for result in data.get("organic_results", []):
                results.append(result["link"])
        else:
            print(f"Error fetching data: {response.status_code}")
        
        # Wait to avoid triggering limits on SerpApi
        time.sleep(2)
    
    # Write results to an output file
    with open("output.txt", "w") as file:
        for result in results:
            file.write(result + "\n")
    
    print(f"Results saved to output.txt")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <website_url>")
    else:
        website_url = sys.argv[1]
        main(website_url)
