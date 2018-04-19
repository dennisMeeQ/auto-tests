import requests
import sys

url = 'https://teamradio-services-stag.herokuapp.com/'
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'Origin': 'https://testfoo.net'}

try:
    r = requests.get(url, headers=headers, timeout=2)

except requests.Timeout:
    print('Timeout...')
    quit()
except:
    print("Unexpected error:", sys.exc_info()[0])
    quit()

if r.headers.get('Access-Control-Allow-Origin'):
    print('Access-Control-Allow-Origin: ' + r.headers.get('Access-Control-Allow-Origin'))

if r.headers.get('Access-Control-Allow-Credentials'):
    print('Access-Control-Allow-Credentials: ' + r.headers.get('Access-Control-Allow-Credentials'))