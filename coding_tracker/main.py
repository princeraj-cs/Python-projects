import requests
from datetime import datetime

USERNAME = "princeraj07"
TOKEN = "dfnifjbsdflknsd8943y"
GRAPH = "graph07"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
today = datetime.now()


want_to = input("""1. POST
2. UPDATE
3. DELETE

Enter [POST/UPDATE/DELETE]: """)

if want_to.lower() == "post":
    quantity = input("How many commits to post?: ")
    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": quantity,
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    print(response.text)
elif want_to.lower() == "update":
    quantity = input("How many commits to update?: ")
    pixel_update_ep = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime("%Y%m%d")}"
    new_pixel_data = {
        "quantity": quantity
    }
    response = requests.put(url=pixel_update_ep, json=new_pixel_data, headers=headers)
    print(response.text)
elif want_to.lower() == "delete":
    pixel_delete_ep = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime("%Y%m%d")}"
    response = requests.put(url=pixel_delete_ep, headers=headers)
    print(response.text)