"""
Reads user id, updates user database and saves login information.

User Database :: | User UID | Name | Dept | Major | Year | Num Entry

Login Info :: | Date | Time | UID
"""
import csv
import time
import datetime
import RPi.GPIO as GPIO
import MFRC522


DATABASE = ''
LOGIN_FILE = 'login.csv'
MIFAREReader = MFRC522.MFRC522()


def save_login_info(login_data, csv_file):
    with open(r'%s' % csv_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(login_data)

try:
  while True:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        time_now = datetime.datetime.now()

        # Print UID
        # print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
        print('UID: $i $i $i $i' % *uid)

        # Load login form

        # Read user information

        # If new user add a new entry

        # Old user increase number of visits

        # Save login information
        login_data = [time_now.hour, time_now.minute, time_now.month, time_now.day, time_now.year]
        login_data += uid
        save_login_info(login_data, LOGIN_FILE)

        time.sleep(2)

except KeyboardInterrupt:
  GPIO.cleanup()
