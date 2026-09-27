import smtplib
import datetime
import os

schedule = {
    "Monday": [
        {"time": "07:45", "subject": "MA11003", "room": "NR211"},
        {"time": "08:45", "subject": "MA11003", "room": "NR211"},
        {"time": "09:45", "subject": "MA11003", "room": "NR211"},
        {"time": "10:45", "subject": "EE11003", "room": "NR211"},
        {"time": "16:45", "subject": "CY11003", "room": "NR111"}
    ],

    "Tuesday": [
        {"time": "07:45", "subject": "CS10003", "room": "NR211"},
        {"time": "08:45", "subject": "CS10003", "room": "NR211"},
        {"time": "11:45", "subject": "MA11003", "room": "NR211"},
        {"time": "14:45", "subject": "CY19003", "room": "In the Department"}
    ],

    "Wednesday": [
        {"time": "07:45", "subject": "EE11003", "room": "NR211"},
        {"time": "08:45", "subject": "EE11003", "room": "NR211"},
        {"time": "10:45", "subject": "CY11003", "room": "NR111"}
    ],

    "Thursday": [
        {"time": "11:45", "subject": "CY11003", "room": "NR111"},
        {"time": "14:45", "subject": "ME29201", "room": "In the Department"},
        {"time": "16:45", "subject": "EE11003", "room": "NR211"}
    ],

    "Friday": [
        {"time": "07:45", "subject": "CY11003", "room": "NR111"},
        {"time": "14:45", "subject": "CS19003", "room": "In the PC Labs"},
        {"time": "16:45", "subject": "MA11003", "room": "NR211"}
    # ]
    ],
    "Sunday": [
    {"time": "06:50", "subject": "testfgg", "room": "TEST ROOM"}
    ]
}

# FIX 1: get current time in IST, not the server's UTC time
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
now = datetime.datetime.now(IST)
today = now.strftime("%A")

todays_classes = schedule.get(today, [])

for cls in todays_classes:
    # FIX 2: tolerant time-window match instead of exact match
    reminder_time = datetime.datetime.strptime(cls["time"], "%H:%M").time()
    reminder_dt = now.replace(hour=reminder_time.hour, minute=reminder_time.minute, second=0, microsecond=0)
    diff_minutes = (now - reminder_dt).total_seconds() / 60

    if 0 <= diff_minutes < 10:
        smtplibObj = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        # FIX 3: read credentials from environment (GitHub Secrets)
        smtplibObj.login(os.environ["SENDER_EMAIL"], os.environ["SENDER_PASSWORD"])

        message = f"Subject:Reminder - {cls['subject']}\n\nClass: {cls['subject']}\nRoom: {cls['room']}\nTime: {cls['time']}"
        smtplibObj.sendmail(os.environ["SENDER_EMAIL"], os.environ["RECEIVER_EMAIL"], message)
        smtplibObj.quit()
        print(f"Sent reminder for {cls['subject']} at {cls['time']}")
