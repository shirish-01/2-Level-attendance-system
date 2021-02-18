"""
==============
MAIN FUNCTION ||
===============
"""


from QRcodeAuthentication import QRcodeAuthentication
from authenticatePic import authenticate
from attendance import attendance



print("Show your QR code ")

#FIRST LEVEL AUTHENTICATION
validity,roll=QRcodeAuthentication()


# SECOND LEVEL AUTHENTICATION

faceValidity=False

if validity:
	faceValidity=authenticate(roll[-3:])
else:
	print('already marked or wrong qr code')

#  MARKING ATTENDANCE IN .CSV FILE
attendance(roll,faceValidity)





