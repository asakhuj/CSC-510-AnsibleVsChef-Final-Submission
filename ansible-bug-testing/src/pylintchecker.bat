rem for %%f in ("*.py") do pychecker.bat --limit 100 %%f
@echo off
call :treeProcess
goto :eof

set COUNTER = 0
set ADV_FILEPATH = "C:\Users\advai\Desktop\NCSU lec\Fall 18\SE\Ansible\ansible-devel\adv"

:treeProcess
rem Do whatever you want here over the files of this subdir, for example:
for %%f in (*.py) do (
	echo %%f
	pylint %%f >> "C:\Users\advai\Desktop\NCSU lec\Fall 18\SE\Ansible\ansible-devel\adv\%%f.txt" 
)
for /D %%d in (*) do (
    cd %%d
    call :treeProcess
    cd ..
)
exit /b