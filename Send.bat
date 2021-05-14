@echo off
set message=Installing the Python Packages Keep Calm
echo %message%
pip install -r requirements.txt %*
set message1=Running the Send Message Script
echo %message1%
python SendMessage.py %*
set message2=Messages Sent Take a Deep Breath
echo %message2%
pause