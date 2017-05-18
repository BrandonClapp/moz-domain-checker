try:
    import settings_dev
except:
    print("No development mode settings found.")
    settings_dev = None

# API Authentication Settings
ACCESS_ID = settings_dev.access_id if settings_dev else 'my-access-key'
SECRET_KEY = settings_dev.secret_key if settings_dev else 'my-secret-key'
REQUEST_INTERVAL = 11  # Number of seconds between each Moz request.

# Threshold Settings
MINIMUM_MOZRANK = 3
MINIMUM_DA = 17
MINIMUM_PA = 15

# Database
DB_NAME = 'data.db'

# Reporting
OUT_DIR = './output/'