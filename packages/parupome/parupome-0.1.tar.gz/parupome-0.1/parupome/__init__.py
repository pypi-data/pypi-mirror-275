from datetime import datetime
import pytz

def convert_timezone(dt_str, from_tz, to_tz, dt_format='%Y-%m-%d %H:%M:%S'):
    """
    Convert datetime string from one timezone to another.

    Parameters:
    - dt_str (str): The datetime string to convert.
    - from_tz (str): The timezone of the input datetime string.
    - to_tz (str): The timezone to convert the datetime string to.
    - dt_format (str, optional): The format of the datetime string. Default is '%Y-%m-%d %H:%M:%S'.

    Returns:
    - str: The converted datetime string in the target timezone.
    """
    # Get the from and to timezone objects
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    
    # Parse the datetime string
    dt = datetime.strptime(dt_str, dt_format)
    
    # Set the original timezone
    dt = from_zone.localize(dt)
    
    # Convert to target timezone
    converted_dt = dt.astimezone(to_zone)
    
    # Return the converted datetime string
    return converted_dt.strftime(dt_format)
