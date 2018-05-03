import requests
import sys
import string
import random

def generateDomain(size=10, chars=string.ascii_lowercase + string.digits):
    dom = ''.join(random.choice(chars) for _ in range(size))
    return dom + '.com'

# Check arguments
if len(sys.argv) == 1:
    print('No URL given.')
    print('Usage: ' + sys.argv[0] + ' URL')
    sys.exit(1)
elif len(sys.argv) > 2:
    print('Too many arguments.')
    print('Usage: ' + sys.argv[0] + ' URL')
    sys.exit(1)

url = sys.argv[1]

prefixURL = '[CORS] [' + url + '] '
print(prefixURL + 'Testing for CORS headers')

# Generate random origin
domain = generateDomain()
headers = {'Origin': domain}

# Try getting CORS headers with OPTIONS
try:
    r = requests.options(url, headers=headers, timeout=2)

except requests.Timeout:
    print(prefixURL + '    Timeout...')
    sys.exit(1)
except:
    print(prefixURL + '    Unexpected error: ', sys.exc_info()[0])
    sys.exit(1)

acao = r.headers.get('Access-Control-Allow-Origin')
if not acao:
    # Try getting CORS headers with GET
    try:
        r = requests.get(url, headers=headers, timeout=2)

    except requests.Timeout:
        print(prefixURL + '    Timeout...')
        sys.exit(1)
    except:
        print(prefixURL + '    Unexpected error:', sys.exc_info()[0])
        sys.exit(1)

    acao = r.headers.get('Access-Control-Allow-Origin')

if not acao:
    # No CORS headers to test
    print(prefixURL + '[INFO] No CORS headers found')
    sys.exit()

# Print headers for logging
print(prefixURL + ' [INFO]    Access-Control-Allow-Origin: ' + acao)
acac = r.headers.get('Access-Control-Allow-Credentials')
if acac:
    print(prefixURL + ' [INFO]    Access-Control-Allow-Credentials: ' + acac)

# Check for vulnerable configurations
# Allow-Credentials invalid value
if acac and acac != 'true':
        print(prefixURL + ' [ERROR]    Invalid CORS configuration: ACAC set but not true. Actual value: ' + acac)
        sys.exit()

acacTrue = acac and acac == 'true'

# Allow-Origin *
if acao == '*':
    if acacTrue:
        print(prefixURL + ' [ERROR]    Invalid CORS configuration: ACAO: * and ACAC: true')
    else:
        print(prefixURL + ' [WARN]    Potentially vulnerable CORS configuration: ACAO: * (ACAC not set)')

# Allow-Origin mirrored
elif acao == domain:
    if acacTrue:
        print(prefixURL + ' [ERROR]    Vulnerable CORS configuration: ACAO mirrored and ACAC: true')
    else:
        print(prefixURL + ' [WARN]    Potentially vulnerable CORS configuration: ACAO mirrored (ACAC not set)')

else:
    print(prefixURL + ' [INFO]    No vulnerability detected')
    
sys.exit()