import requests
from datetime import datetime

pixela_url = "https://pixe.la/v1/users"
pixela_params = {
    "token": "**************",
    "username": "************",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_url, json=pixela_params)
# print(response.text)

graph_endpoint = f"{pixela_url}/{pixela_params['username']}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": pixela_params["token"]
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

add_pixel_endpoint = f"{pixela_url}/{pixela_params['username']}/graphs/{graph_params['id']}"
today = datetime.now()
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.5"
}

response = requests.post(url=add_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)
