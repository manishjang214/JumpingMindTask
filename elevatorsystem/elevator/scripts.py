import requests

url = 'http://127.0.0.1:8001/api/v1/elevators/'
data = {
    'status': 'Door Open',
    'current_floor': 1
}

response = requests.post(url, json=data)

print(response.status_code)  # Print the response status code
print(response.json())      # Print the response body as JSON
