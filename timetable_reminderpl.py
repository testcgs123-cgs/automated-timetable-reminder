
import smtplib
import datetime

schedule = {
    "Monday": [
        {"time": "08:00", "subject": "MA11003", "room": "NR211"},
        {"time": "09:00", "subject": "MA11003", "room": "NR211"},
        {"time": "10:00", "subject": "MA11003", "room": "NR211"},
        {"time": "11:00", "subject": "EE11003", "room": "NR211"},
        {"time": "17:00", "subject": "CY11003", "room": "NR111"}
    ],

    "Tuesday": [
        {"time": "08:00", "subject": "CS10003", "room": "NR211"},
        {"time": "09:00", "subject": "CS10003", "room": "NR211"},
        {"time": "12:00", "subject": "MA11003", "room": "NR211"},
        {"time": "15:00", "subject": "CY19003", "room": "In the Department"}
    ],

    "Wednesday": [
        {"time": "08:00", "subject": "EE11003", "room": "NR211"},
        {"time": "09:00", "subject": "EE11003", "room": "NR211"},
        {"time": "11:00", "subject": "CY11003", "room": "NR111"}
    ],

    "Thursday": [
        {"time": "12:00", "subject": "CY11003", "room": "NR111"},
        {"time": "15:00", "subject": "ME29201", "room": "In the Department"},
        {"time": "17:00", "subject": "EE11003", "room": "NR211"}
    ],

    "Friday": [
        {"time": "08:00", "subject": "CY11003", "room": "NR111"},
        {"time": "15:00", "subject": "CS19003", "room": "In the PC Labs"},
        {"time": "17:00", "subject": "MA11003", "room": "NR211"}
    ]
}

# PythonAnywhere's server runs in UTC, so convert to IST 
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
now = datetime.datetime.now(IST)
today = now.strftime("%A")
current_time = now.strftime("%H:%M")

todays_classes = schedule.get(today, [])

# Only send if current IST time is between 05:55 and 06:05
if todays_classes and "05:55" <= current_time <= "06:05":
    body = f"Timetable for {today}:\n\n"
    for cls in todays_classes:
        body += f"{cls['time']} - {cls['subject']} ({cls['room']})\n"

    smtplibObj = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtplibObj.login("testcgs123@gmail.com", "xdwz vmzi gqef hhyw")
    smtplibObj.sendmail("testcgs123@gmail.com", "testcgs123@gmail.com", f"Subject: Today's Timetable - {today}\n\n{body}")
    smtplibObj.quit()
# now = datetime.datetime.now()
# today = now.strftime("%A")
# current_time = now.strftime("%H:%M")

# todays_classes = schedule.get(today, [])

# # Only send if current time is between 05:55 and 06:05
# if todays_classes and "05:55" <= current_time <= "06:05":
#     body = f"Timetable for {today}:\n\n"
#     for cls in todays_classes:
#         body += f"{cls['time']} - {cls['subject']} ({cls['room']})\n"

