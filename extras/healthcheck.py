import requests

def check_server_status(url):
 try:
 response = requests.get(url)
 if response.status_code == 200:
 return 'Server is up'
 else:
 return 'Server is down'
 except requests.exceptions.RequestException as e:
 return 'Error: ' + str(e)