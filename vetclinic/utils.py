import uuid
import datetime

def str_uuid():
    """
    Returns a uuid4 as a string
    """
    return str(uuid.uuid4())

# Function to convert string to datetime
def converter(dt):
    format = '%b %d %Y %I:%M%p'  # You have to specify the format either statically or dynamically
    datetime_str = datetime.datetime.strptime(dt, format)
    return datetime_str