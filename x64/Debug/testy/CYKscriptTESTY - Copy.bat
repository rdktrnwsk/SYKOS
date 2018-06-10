@echo off


SET /A ite=5
SET /A pomiar=6
SET instancyja=rbg323


for /L %%g in (1,1,%ite%) do Call :program7 "%%g"
pause



:program7
	
	start /w CYK.exe grammar7.txt 31 0
	
	echo a
Exit /B
