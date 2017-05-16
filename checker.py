import math
import requests
import json
from domain_importer import content as domains
import result_exporter
from datetime import datetime
import time

def run_request(domain):
    cookies = {
        'mozauth': 'gHiPdyGUi7wAqNLLj0BVAeLmYlLvWFe14k6vP2ee7UovZTiZlcrTDxRdL75WtSij'
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'content-type': 'application/json',
    }
    payload = [domain]

    try:
        resp = requests.post("https://mozbar.moz.com/bartender/url-metrics", data=json.dumps(payload), cookies=cookies,
                         headers=headers, timeout=5)
    except requests.exceptions.Timeout:
        print('Request for domain %s timed out. Trying again.' %(domain))
        resp = run_request(domain)

    if resp.status_code == 429:
        time.sleep(5)
        resp = run_request(domain)

    return resp


for domain in domains:

    resp = run_request(domain)

    response_body = json.loads(resp.text)
    response_body = response_body[0]

    remaining_count = resp.headers.get('X-RateLimit-Remaining')
    reset_time_unix = resp.headers.get('X-RateLimit-Reset')

    reset_time = datetime.fromtimestamp(int(reset_time_unix))
    print('Remaining: %s' %(remaining_count))
    # print('Reset time: %s' %(reset_time))

    reset_seconds = math.floor((reset_time - datetime.now()).seconds)
    print('Seconds until reset: ', reset_seconds)

    pa = round(response_body.get('pda'), 2)
    da = round(response_body.get('upa'), 2)

    rpt = {
        'domain': domain,
        'da': da,
        'pa': pa
    }

    print(rpt)
    result_exporter.write(json.dumps(rpt))

    if int(remaining_count) == 0:
        if reset_seconds > 86000: # 24 hours was returned for some reason.
            print('Not waiting 24 hours. How about 25 seconds instead.')
            reset_seconds = 25
        print('Sleeping for', reset_seconds + 5, 'seconds.')
        time.sleep(reset_seconds + 5)
