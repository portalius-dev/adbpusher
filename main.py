import subprocess
import time
import sys

print("===================")
print("=== ADB Pusher ===")
print("=== Welcome! ===")
print("===================")

time.sleep(1)
apk = input("APK Path - ")
time.sleep(0.5)
subprocess.run(['adb', 'devices'])
time.sleep(1)

# install logic
here = input("Is your device here? (Y/N) - ")

if here == "y" or here == "Y":
	subprocess.run(['adb', 'install', apk])
	time.sleep(1)
	print("Success!")

else:
	print("Okay. Stopping programm.")
	time.sleep(1)
	sys.exit()
