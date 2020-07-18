# pydown
Basic downloader written in Python.

### NOTE
1. I know it's plenty of python scripts with this name out there already
2. I just needed something to download anime :wink:

## Usage

**NOTE:** You need **Python 3**

1. Run pydown to download a resource form the web:
```
python pydown.py -url resource_url -o output_file
```

2. If you need to automate the download of a large set of media, you can use `anime_downloader.bat` (Windows OS):
```
./anime_downloader.bat STARTING_EPISODE LAST_EPISODE
```
It's a script which calls `pydown` in loop in order to download the media into the specified range all at once.

**NOTE:** You need to specify the resource URL into the batch script:
```batch
:LOOP
if %CURRENT_EP% gtr %LAST_EP% (
    goto END_SCRIPT
)
@Rem !!! The line to modify is below !!!
python pydown.py -url http://www.SOMEWEBSITE.org/path/episode_n_%CURRENT_EP%.mp4 -o Anime_folder/episode_n_%CURRENT_EP%.mp4
echo -------------------------------------------
set /A CURRENT_EP=CURRENT_EP+1
goto LOOP
```
