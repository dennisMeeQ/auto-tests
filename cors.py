import requests
import sys

if len(sys.argv) == 1:
    print('No URL given.')
    print('Usage: ' + sys.argv[0] + ' URL [2. URL] [3. URL] ...')
    quit()

urls = sys.argv[1:]

for url in urls:
    print('Testing CORS headers for')
    print(url)
    
    #url = 'https://teamradio-services-stag.herokuapp.com/'
    #payload = {'key1': 'value1', 'key2': 'value2'}
    headers = {'Origin': 'https://testfoo.net'}

    try:
        r = requests.get(url, headers=headers, timeout=2)

    except requests.Timeout:
        print('    Timeout...')
        quit()
    except:
        print("    Unexpected error:", sys.exc_info()[0])
        quit()

    if r.headers.get('Access-Control-Allow-Origin'):
        print('    Access-Control-Allow-Origin: ' + r.headers.get('Access-Control-Allow-Origin'))

    if r.headers.get('Access-Control-Allow-Credentials'):
        print('    Access-Control-Allow-Credentials: ' + r.headers.get('Access-Control-Allow-Credentials'))