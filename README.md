# Moz Domain Checker
CLI tool for checking and reporting Moz domain name statistics. This tool with generate a .csv report with the following information.
- MozRank
- Domain Authority
- Page Authority

**Requirements**
- Python 3
- No external pip packages required.

**Usage**
1. Clone repository (`git clone https://github.com/BrandonClapp/moz-domain-checker`)
2. Navigate to `settings.py` and change the `access_id` and `secret_key` to the appropriate values. To obtain these values, sign up for a free Mozscape account at https://moz.com/products/api
    - Note: Free accounts are limited to 25,000 rows per month and throttled to 1 request (containing a maximum of 10 domains) per 10 seconds.
3. Populate `domains.txt` with a list of desired domain names. i.e.

```
domainname1.com
domainname2.com
domainname3.com
...etc
```

4. From a terminal window (or cmd/PowerShell on Windows) navigate to the root directory of the repository and run `python checker.py`. This will invoke the Mozscape API with batches of 10 domains per request, while pausing 10 seconds between requests to adhere to their throttling terms of service for free accounts.

    Only domains that meet the criteria specified (for moz rank, domain authority, and page authority) will be recorded in the final result file, while others will be ignored.

5. Once all domains from `domains.txt` have been processed, the results raw results will be found inside of `results.jl`. In order to make sense of this information, a .csv file, titled with the appropriate timestamp, will also be created in the `./output` directory.

**Logging**

A verbose log stream is kept in `log.txt`.
