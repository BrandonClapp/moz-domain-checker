import requests
import json
from domain_importer import content as domains
import result_exporter

#print(domains)

cookies = {
    'mozauth': 'gHiPdyGUi7wAqNLLj0BVAeLmYlLvWFe14k6vP2ee7UovZTiZlcrTDxRdL75WtSij'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'content-type': 'application/json',
}

for domain in domains:

    payload = [domain]
    resp = requests.post("https://mozbar.moz.com/bartender/url-metrics", data=json.dumps(payload), cookies=cookies, headers=headers)

    response_body = json.loads(resp.text)
    response_body = response_body[0]
    # print(resp.headers)

    pa = round(response_body.get('pda'), 2)
    da = round(response_body.get('upa'), 2)

    rpt = {
        'domain': domain,
        'da': da,
        'pa': pa
    }

     # print('DA = %s, PA = %s' %(da, pa))
    print(rpt)
    result_exporter.write(json.dumps(rpt))