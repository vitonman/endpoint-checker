import sys
import time
import requests

"""
endpoint_checker.py

Script to check the URL availabiolity

Inputs:
- URL Link
Outputs:
- HTTP response code
- Result (OK - NOK)
- Response time in ms

! Required library:
- request (Install with: python -m pip install requests)

"""


def check_endpoint(url): #def function link
    start = time.perf_counter() #start counter
    code = None #initializing answer
    try: #sending get request
        resp = requests.get(url, timeout=10)
        code = resp.status_code
    except Exception as e: # catch exeptions
        print(f"Error: {e}", file=sys.stderr)
    elapsed = int((time.perf_counter() - start) * 1000) # time to ms and counter perfortm
    result = "OK" if code == 200 else "NOK"
    return code, result, elapsed #returning answer

if __name__ == "__main__":
    #Ensure the script is being run derectly

    if len(sys.argv) < 2:
        #If no URL then print instructions how to run
        print("Usage: python endpoint_checker.py <URL>")
        sys.exit(1)

    #Get url from cmd
    url = sys.argv[1]

    # code - HTTP status code, result - OK or NOK, elapsed - response time in ms
    code, result, elapsed = check_endpoint(url)

    #output the check results
    print(f"Response code: {code}")
    print(f"Result: {result}")
    print(f"Response time (ms): {elapsed}")
