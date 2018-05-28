@echo off


SET /A ite=1
SET /A pomiar=2
SET instancyja=rbg323


for /L %%g in (1,1,%ite%) do Call :program7 "%%g"

set /a pomiar=2
for /L %%h in (1,1,%ite%) do Call :program8 "%%h"
pause
set /a pomiar=50
for /L %%i in (1,1,%ite%) do Call :program9 "%%i"
set /a pomiar=50
for /L %%j in (1,1,%ite%) do Call :program10 "%%j"
set /a pomiar=25
for /L %%k in (1,1,%ite%) do Call :program11 "%%k"


:program7
	
	echo a
	start /w CYK.exe grammar5.txt cababcabdcffabeedcababcabfffabeeecffabeeebdabfabebeb

	SET error=%errorlevel% 

	if %error% gtr -1  (
	set /a pomiar=%error%
	goto :program7
	) else (
    	echo Function Done %error%
 	 )
Exit /B

:program8
	
	echo a
	start /w CYK.exe grammar6.txt jabejabgababffkfabfkfjabgababffkf

	SET error=%errorlevel% 

	if %error% gtr -1  (
	set /a pomiar=%error%
	goto :program7
	) else (
    	echo Function Done %error%
 	 )
Exit /B

:program9
	
	echo a
	start /w algorytmTSP.exe kro124p 0 %pomiar% 64 dane.txt

	SET error=%errorlevel% 

	if %error% gtr -1  (
	set /a pomiar=%error%
	goto :program9
	) else (
    	echo Function Done %error%
 	 )
Exit /B

:program10
	
	echo a
	start /w algorytmTSP.exe ftv170 0 %pomiar% 64 dane.txt

	SET error=%errorlevel% 

	if %error% gtr -1  (
	set /a pomiar=%error%
	goto :program10
	) else (
    	echo Function Done %error%
 	 )
Exit /B

:program11
	
	echo a
	start /w algorytmTSP.exe rbg323 0 %pomiar% 64 dane.txt

	SET error=%errorlevel% 

	if %error% gtr -1  (
	set /a pomiar=%error%
	goto :program11
	) else (
    	echo Function Done %error%
 	 )
pause
Exit /B




echo %ERRORLEVEL%

pause

Exit /B