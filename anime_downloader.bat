@echo off
cls
Rem url = "http://www.SOMEWEBSITE.org/path/episode_n_250.mp4"
Rem name = "Anime_folder/episode_n_250.mp4"
Rem "Usage example: anime_downloader.bat 250 260"
Rem "Will download episodes from 250 to 260 included"

set STARTING_EP=%1
set LAST_EP=%2
set CURRENT_EP=%STARTING_EP%


:LOOP
if %CURRENT_EP% gtr %LAST_EP% (
    goto END_SCRIPT
)
python pydown.py -url http://www.SOMEWEBSITE.org/path/episode_n_%CURRENT_EP%.mp4 -o Anime_folder/episode_n_%CURRENT_EP%.mp4
echo -------------------------------------------
set /A CURRENT_EP=CURRENT_EP+1
goto LOOP


:END_SCRIPT
echo Episodes from %STARTING_EP% to %LAST_EP% (included) have been downloaded!
echo Press a key to terminate the script...
pause>nul
exit
