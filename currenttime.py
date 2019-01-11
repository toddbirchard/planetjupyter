from datetime import datetime, timezone

def getTime():
    """Get user's current time"""
    rightnow = datetime.today()
    return rightnow

def getPrettyTime():
    """Get user's pretty current time"""
    rightnow = datetime.today()
    prettytime = rightnow.ctime()
    return prettytime

yourtime = getTime()
prettytime = getPrettyTime()
