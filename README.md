# Moz Domain Checker
Script for bulk checking and reporting Moz domain name statistics. This tool with generate a .csv report with the following information.
- MozRank
- Domain Authority
- Page Authority

**Why?**

Useful for finding expired domain names that have already been previously promoted, and have built reputations and search engine results. I find the existing free tools online lacking, limited, and requiring too much manual intervention. Also, paid tools are absurdly expensive.

**Requirements**
- Python 3
- No external pip packages required.

**Usage**
1. Clone repository (`git clone https://github.com/BrandonClapp/moz-domain-checker`)

2. Navigate to `settings.py` and change the `access_id` and `secret_key` to the appropriate values. To obtain these values, sign up for a free Mozscape account at https://moz.com/products/api
    - Note: Free accounts are limited to 25,000 rows per month and throttled to 1 request (containing a maximum of 10 domains) per 10 seconds.
    
```python
# API Authentication Settings
ACCESS_ID = settings_dev.ACCESS_ID if settings_dev else 'put-your-access-id-here'
SECRET_KEY = settings_dev.SECRET_KEY if settings_dev else 'put-your-secret-key-here'
```
    
3. Populate `domains.txt` with a list of desired domain names. i.e.

```
domainname1.com
domainname2.com
domainname3.com
...etc
```

4. From a terminal window (or cmd/PowerShell on Windows) navigate to the root directory of the repository and run `python checker.py`. This will invoke the Mozscape API with batches of 10 domains per request, while pausing 10 seconds between requests to adhere to their throttling terms of service for free accounts.

   All domain results will be populated in a SQLite database, even if they do not meet the minimum specified criteria in `settings.py` to ensure that they are not checked multiple times if the process is restarted.

5. At any time, you may run `python report.py` to generate a .csv file containing only the domains which meet the minimum criteria specified in `settings.py`. The file will be placed in the `./output` directory by default, but can be customized via the settings.

6. Analyze the results and do further research on the domains that were filtered. Just because it has high metrics, doesn't mean that it's good. Do your research!

**Logging**

A verbose log stream is kept in `log.txt`.
