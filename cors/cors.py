import requests
import sys
import string
import random

class ConnectionException(Exception):
    pass

def generateDomain(size=10, chars=string.ascii_lowercase + string.digits):
    dom = ''.join(random.choice(chars) for _ in range(size))
    return dom + '.com'

def scanCors(url):
    # Check arguments
    if not url:
        raise ValueError('Empty URL')
        
    prefixURL = '[CORS] [' + url + '] '

    # Generate random origin
    domain = generateDomain()
    headers = {'Origin': domain}

    # Try getting CORS headers with OPTIONS
    print(prefixURL + 'Testing for CORS headers with OPTIONS')
    try:
        r = requests.options(url, headers=headers, timeout=2)

    except requests.Timeout:
        print(prefixURL + '    Timeout...')
        raise ConnectionException
    except:
        print(prefixURL + '    Unexpected error: ', sys.exc_info()[0])
        raise ConnectionException

    acao = r.headers.get('Access-Control-Allow-Origin')
    if not acao:
        # Try getting CORS headers with GET
        print(prefixURL + 'Testing for CORS headers with GET')
        try:
            r = requests.get(url, headers=headers, timeout=2)

        except requests.Timeout:
            print(prefixURL + '    Timeout...')
            raise ConnectionException
        except:
            print(prefixURL + '    Unexpected error:', sys.exc_info()[0])
            raise ConnectionException

        acao = r.headers.get('Access-Control-Allow-Origin')

    if not acao:
        # No CORS headers to test
        print(prefixURL + '[INFO] No CORS headers found')
        return

    # Print headers for logging
    print(prefixURL + ' [INFO]    Access-Control-Allow-Origin: ' + acao)
    acac = r.headers.get('Access-Control-Allow-Credentials')
    if acac:
        print(prefixURL + ' [INFO]    Access-Control-Allow-Credentials: ' + acac)

    # Check for vulnerable configurations
    # Allow-Credentials invalid value
    if acac and acac != 'true':
        print(prefixURL + ' [ERROR]    Invalid CORS configuration: ACAC set but not true. Actual value: ' + acac)
        return

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
        
    return


def main(argv):
    if len(sys.argv) == 1:
        print('No URL given.')
        print('Usage: ' + sys.argv[0] + ' URL')
        sys.exit(1)
    elif len(sys.argv) > 2:
        print('Too many arguments.')
        print('Usage: ' + sys.argv[0] + ' URL')
        sys.exit(1)

    url = argv[1]

    try:
        scanCors(url)
    except ConnectionException:
        return 1

if __name__ == "__main__":
    main(sys.argv)