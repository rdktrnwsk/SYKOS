@echo off


SET /A ite=20
SET /A pomiar=25
SET instancyja=rbg323


for /L %%g in (1,1,%ite%) do Call :program7 "%%g"
pause



:program7
	
	start /w CYK.exe example1.txt 31 1
	echo a
Exit /B
