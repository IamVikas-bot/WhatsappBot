@echo off
set message=Installing the Python Packages Keep Calm
echo %message%
pip install -r requirements.txt %*
set message1=Running the Join Group Script
echo %message1%
python JoinGroup.py %*
set message2=Group Joined Successfully Take a Deep Breath
echo %message2%
pause