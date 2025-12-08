import psutil
import smtplib
from email.mime.text import MIMEText

# Email settings
EMAIL_ADDRESS = 'advaith0001@gmail.com'      
EMAIL_PASSWORD = 'zbrd ufrl pera yqsc'       
RECIPIENT_EMAIL = 'advaith0001@gmail.com'   

# Threshold for disk usage (in percentage)
THRESHOLD = 0.1

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    usage = get_disk_usage()

    if usage > THRESHOLD:
        subject = "Disk Usage Alert "
        body = f"""
Warning: Your system's disk usage is high!


Current Usage : {usage}%
Threshold     : {THRESHOLD}%
Path Checked  : /


Please clear unwanted files.
"""
        send_email(subject, body)
    else:
        print(f"Disk usage is OK: {usage}%")

if __name__ == "__main__":
    main()
