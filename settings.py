try:
    import settings_dev
except ImportError:
    print("No development mode settings found.")

# API Authentication Settings
access_id = settings_dev.access_id or 'my-access-key'
secret_key = settings_dev.secret_key or 'my-secret-key'
request_interval = 11  # Number of seconds between each Moz request.

# Threshold Settings
minimum_mozrank = 3
minimum_da = 17
minimum_pa = 15