"""
    Scrap file for testing stuff.
"""

import mozscape

chunk = [
    'avatar-mod.com',
    'chi-opendi.com',
    'deshtunes.com',
    'ramaturizm.com',
    'tyroar.com',
    '21stam.com',
    'twyxmotor.com',
    'scdongniao.com',
    'bjzmlaw.com',
    'banitweb.com',
]
metrics = [{'fmrp': 0, 'fmrr': 0.0, 'pda': 1, 'ueid': 0, 'uid': 0, 'ulc': 0, 'umrp': 0, 'umrr': 0, 'upa': 1, 'us': 0, 'ut': '', 'uu': ''}, {'fmrp': 0, 'fmrr': 0, 'pda': 1, 'ueid': 0, 'uid': 0, 'ulc': 0, 'umrp': 0, 'umrr': 0, 'upa': 1, 'us': 0, 'ut': '', 'uu': ''}, {'fmrp': 2.5850879882571416, 'fmrr': 5.000889511601364e-13, 'pda': 21.96990332663498, 'ueid': 2, 'uid': 2, 'ulc': 0, 'umrp': 3.4082645635232236, 'umrr': 5.806642227528035e-14, 'upa': 27.405072024642294, 'us': 0, 'ut': '', 'uu': 'deshtunes.com/'}, {'fmrp': 4.3133010137069965, 'fmrr': 7.86804971135599e-11, 'pda': 28.216462722710848, 'ueid': 0, 'uid': 3545, 'ulc': 0, 'umrp': 5.662642940547774, 'umrr': 3.288893380010822e-10, 'upa': 26.93579180503436, 'us': 0, 'ut': '', 'uu': 'ramaturizm.com/'}, {'fmrp': 0, 'fmrr': 0.0, 'pda': 8.576187545102336, 'ueid': 0, 'uid': 0, 'ulc': 1487791044, 'umrp': 0, 'umrr': 0.0, 'upa': 18.934696367348465, 'us': 301, 'ut': '', 'uu': 'tyroar.com/'}, {'fmrp': 0, 'fmrr': 0.0, 'pda': 3.2103183997534224, 'ueid': 0, 'uid': 2, 'ulc': 1487181330, 'umrp': 0, 'umrr': 0.0, 'upa': 19.15993142836419, 'us': 13, 'ut': '', 'uu': '21stam.com/'}, {'fmrp': 0, 'fmrr': 0.0, 'pda': 30.190900384480184, 'ueid': 0, 'uid': 449, 'ulc': 1483822635, 'umrp': 6.213960177841677, 'umrr': 2.722020794042988e-09, 'upa': 35.5849753349203, 'us': 13, 'ut': '', 'uu': 'twyxmotor.com/'}, {'fmrp': 0, 'fmrr': 0, 'pda': 7.078773951353011, 'ueid': 0, 'uid': 0, 'ulc': 0, 'umrp': 0, 'umrr': 0, 'upa': 1, 'us': 0, 'ut': '', 'uu': ''}, {'fmrp': 0, 'fmrr': 0, 'pda': 1, 'ueid': 0, 'uid': 0, 'ulc': 0, 'umrp': 0, 'umrr': 0, 'upa': 1, 'us': 0, 'ut': '', 'uu': ''}, {'fmrp': 0, 'fmrr': 0, 'pda': 1, 'ueid': 0, 'uid': 0, 'ulc': 0, 'umrp': 0, 'umrr': 0, 'upa': 1, 'us': 0, 'ut': '', 'uu': ''}]

for idx, domain in enumerate(chunk):
    metric = metrics[idx]
    mozrank = round(metric[mozscape.MOZRANK], 2)
    da = round(metric[mozscape.DOMAIN_AUTHORITY], 2)
    pa = round(metric[mozscape.PAGE_AUTHORITY], 2)

    result = {
        "domain": domain,
        "mozrank": mozrank,
        "da": da,
        "pa": pa,
    }

    #print(str(result))


# item = {
#     "domain": "mydomainname.com",
#     "mozrank": 4.3,
#     "da": 2.3,
#     "pa": 2.4,
# }
#
# sql = "INSERT INTO domains VALUES ('%s', %s, %s, %s)" %(item['domain'], item['mozrank'], item['da'], item['pa'])
# print(sql)