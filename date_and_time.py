
from datetime import datetime

# numer of days that have passed from now to year 12/31/1900
delta = datetime.now() - datetime(1900,12,31)
print(delta.days)

