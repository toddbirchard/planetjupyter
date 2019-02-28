<<<<<<< HEAD:application/currenttime.py
from datetime import datetime
=======
from datetime import datetime, timezone
>>>>>>> 453cbc4c0bbee22fe8e0b53126b94a0411101c41:currenttime.py

def getTime():
    """Get user's current time."""
    rightnow = datetime.today()
    return rightnow

def getPrettyTime():
    """Get user's pretty current time."""
    rightnow = datetime.today()
    prettytime = rightnow.ctime()
    return prettytime

yourtime = getTime()
prettytime = getPrettyTime()
