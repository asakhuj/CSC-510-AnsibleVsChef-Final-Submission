@echo off
call :treeProcess
goto :eof

:treeProcess
rem Do whatever you want here over the files of this subdir, for example:
for %%f in (*.py) do (
	echo %%f
	rem change "C:Users.." to the absolute path of your result folder. Mine is result\pylint_report
	pylint %%f >> "C:\Users\advai\..\result\%%f.txt" 
)
for /D %%d in (*) do (
    cd %%d
    call :treeProcess
    cd ..
)
exit /b
