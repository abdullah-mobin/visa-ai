from datetime import datetime
import pytz

# Optional: set your timezone (Asia/Dhaka for Bangladesh)
TIMEZONE = "Asia/Dhaka"

def get_current_time():
    try:
        now = datetime.now(pytz.timezone(TIMEZONE))
        time_str = now.strftime("Time: %I:%M %p, Date: %A, %d %B %Y")
        return time_str
    except Exception as e:
        return f"Time error: {e}"
