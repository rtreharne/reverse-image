import requests
import json
from .config import API_TOKEN

def search_images(image_url):
    url = 'https://serpapi.com/search?engine=google_lens'
    params = {
        'engine': 'google_lens',
        'url': image_url,
        'api_key': API_TOKEN
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Error: {response.status_code}')
        return None

if __name__ == '__main__':
    api_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR63kOWBIsQWHv9agSv4r9LAUHYs5frx_4udBxbvV0aSe2w_DVivob5VzWWaJEygJeNyPM&usqp=CAU'  # Replace with your desired search query
    search_results = search_images(api_url)

    # save the results to a file
    with open('search_results.json', 'w') as f:
        f.write(json.dumps(search_results, indent=2))
