import requests


response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()
print(all_posts)