try:
    import settings_dev
except:
    print("No development mode settings found.")
    settings_dev = None

# API Authentication Settings
access_id = settings_dev.access_id if settings_dev else 'my-access-key'
secret_key = settings_dev.secret_key if settings_dev else 'my-secret-key'
request_interval = 11  # Number of seconds between each Moz request.

# Threshold Settings
minimum_mozrank = 3
minimum_da = 17
minimum_pa = 15

# Data
db_name = 'data.db'