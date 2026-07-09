@echo off

python -m pytest ^
--browser chrome ^
--html=reports/report.html ^
--self-contained-html

pause