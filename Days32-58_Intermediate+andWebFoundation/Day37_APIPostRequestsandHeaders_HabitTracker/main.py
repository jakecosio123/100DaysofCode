import requests
from datetime import datetime

USERNAME = "jcosio"
TOKEN = "zcvp38uaoisvhzpx98"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# # Create account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
# # Create the graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
date = str(datetime.now().strftime("%Y%m%d"))

pixel_params = {
    "date": date,
    "quantity": input("How many pages did you read today? "),
}

# Create a pixel on the graph
response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

update_pixel_params = {
    "quantity": "15"
}

# # Update a pixel on the graph with a new value
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

# # Delete a pixel on the graph
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
