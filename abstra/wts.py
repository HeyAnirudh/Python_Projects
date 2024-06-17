import pywhatkit as kit
import datetime


# Send a simple message
kit.sendwhatmsg("+919989858071", "Hello, this is an automated message!",12, 35)

# Schedule a message for a specific time
hour = 12
minute = 35
kit.sendwhatmsg("+919989858071", "This message is scheduled!", hour, minute)