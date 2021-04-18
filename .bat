@echo off
echo Which file do you want to run?
echo (1) UUID generator
set /P file="> "
if %file%==1 python "uuid/uuid.py"
pause