@echo off


SET /A ite=5
SET /A pomiar=0
SET /A algo=0


for /L %%g in (1,1,%ite%) do Call :program7 "%%g"
pause



:program7
	
	for /L %%f in (1,1,5) do (
	set /a pomiar=%%f
		Call :program2 "%%f"
	)
	
	echo a
Exit /B


:program2
	
	for /L %%f in (31,1,36) do (
	set /a algo=%%f
		Call :program1 "%%j"
	)
	
	echo a
Exit /B

:program1
	
	start /w CYK.exe grammar7.txt %algo% %pomiar%
	
	echo a
Exit /B