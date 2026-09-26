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
    ]
}
schedule["Sunday"] = [
    {"time": "04:47", "subject": "testfgg", "room": "TEST ROOM"}
]

# To locate today's day and time now 
now = datetime.datetime.now()
today = now.strftime("%A")  # monday,tue,wed etc.
timenow = now.strftime("%H:%M")

todays_classes = schedule.get(today, [])

# targeting the upcomming class
for cls in todays_classes:
    if cls["time"] == timenow:
        smtplibObj = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtplibObj.login("SENDERS_Email","Sender_app_pass")

        message = f"Subject:Reminder - {cls['subject']}\n\nClass: {cls['subject']}\nRoom: {cls['room']}\nTime: {cls['time']}"
        smtplibObj.sendmail("SENDERS_Email","Receiver_email",message)
        smtplibObj.quit()
