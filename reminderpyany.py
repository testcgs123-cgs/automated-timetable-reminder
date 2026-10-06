import smtplib
import datetime
import os
import time

schedule = {
    "Monday": [
        {"time": "07:45", "start_time": "08:00", "subject": "MA11003", "room": "NR211"},
        {"time": "08:45", "start_time": "09:00", "subject": "MA11003", "room": "NR211"},
        {"time": "09:45", "start_time": "10:00", "subject": "MA11003", "room": "NR211"},
        {"time": "10:45", "start_time": "11:00", "subject": "EE11003", "room": "NR211"},
        {"time": "16:45", "start_time": "17:00", "subject": "CY11003", "room": "NR111"}
    ],

    "Tuesday": [
        {"time": "07:45", "start_time": "08:00", "subject": "CS10003", "room": "NR211"},
        {"time": "08:45", "start_time": "09:00", "subject": "CS10003", "room": "NR211"},
        {"time": "11:45", "start_time": "12:00", "subject": "MA11003", "room": "NR211"},
        {"time": "14:45", "start_time": "15:00", "subject": "CY19003", "room": "In the Department"}
    ],

    "Wednesday": [
        {"time": "07:45", "start_time": "08:00", "subject": "EE11003", "room": "NR211"},
        {"time": "08:45", "start_time": "09:00", "subject": "EE11003", "room": "NR211"},
        {"time": "10:45", "start_time": "11:00", "subject": "CY11003", "room": "NR111"}
    ],

    "Thursday": [
        {"time": "11:45", "start_time": "12:00", "subject": "CY11003", "room": "NR111"},
        {"time": "14:45", "start_time": "15:00", "subject": "ME29201", "room": "In the Department"},
        {"time": "16:45", "start_time": "17:00", "subject": "EE11003", "room": "NR211"}
    ],

    "Friday": [
        {"time": "07:45", "start_time": "08:00", "subject": "CY11003", "room": "NR111"},
        {"time": "14:45", "start_time": "15:00", "subject": "CS19003", "room": "In the PC Labs"},
        {"time": "16:45", "start_time": "17:00", "subject": "MA11003", "room": "NR211"}
    ]
}

# PythonAnywhere also runs on UTC, so set IST here
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))

# remembers which reminders were already sent, so each class is emailed only once
sent = set()

print("Reminder service started")

while True:
    try:
        now = datetime.datetime.now(IST)
        today = now.strftime("%A")
        todays_classes = schedule.get(today, [])

        for cls in todays_classes:
            reminder_time = datetime.datetime.strptime(cls["time"], "%H:%M").time()
            reminder_dt = now.replace(hour=reminder_time.hour, minute=reminder_time.minute, second=0, microsecond=0)
            diff_minutes = (now - reminder_dt).total_seconds() / 60

            key = (now.date(), cls["time"])

            if 0 <= diff_minutes < 10 and key not in sent:
                smtplibObj = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                smtplibObj.login(os.environ["SENDER_EMAIL"], os.environ["SENDER_PASSWORD"])

                message = f"Subject:CLASS REMINDER - {cls['subject']}\n\nSubject   :  {cls['subject']}\nRoom      :  {cls['room']}\nStarts      :  {cls['start_time']}"
                smtplibObj.sendmail(os.environ["SENDER_EMAIL"], os.environ["RECEIVER_EMAIL"], message)
                smtplibObj.quit()

                sent.add(key)   # only marked as sent after the email really went out
                print(f"[{now:%H:%M:%S}] Sent reminder for {cls['subject']}")

    except Exception as e:
        # if the network fails, the loop keeps running and retries in 30 seconds
        print("Error:", e)

    time.sleep(30)