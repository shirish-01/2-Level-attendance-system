"""
===========================
ATTENDANCE MARKING IN CSV ||
===========================
"""
import datetime

import pandas as pd


# IF TWO LEVELS ARE SUCESSFULLY AUTHENTICATED ATTENDACE IS MARKED IN CSV FILE


# RECORDING THE ATTENDANCE
def attendance(id, auth_token):
    # IF NOT AUTHENTICATED BELOW MESSAGE IS DISPLAYED
    if not auth_token:
        print('Attendance not marked')

    # USED TO CREATE A CSV FILE ON PRESENT DATE, IF ALREADY CREATED DOSENT CREATE ONE
    # MARKED SUCESSFULLY IF AUTHENTICATED
    else:
        file_name = (str(datetime.datetime.now()).split())[0] + ".csv"
        x = pd.DataFrame([[id, 'P']], columns=['id', 'attendance'])
        with open(file_name, 'a') as f:
            x.to_csv(f, index=False, header=f.tell() == 0)
        print('attendance marked sucessfully')


"""MAIN FUNCTION"""

if __name__ == '__main__':
    attendance('2451-18-733-128', False)
    attendance('251-18-733-136', True)
