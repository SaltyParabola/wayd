# what are you doing? (wayd)

![wayd](wayd.png)
This is a python-only version of the original wayd program from spacekaila. If you have a mac, the original version is better, but this can work on windows.

From spacekaila:

"Couldn't find a program to do what I wanted, so I built my own. Currently very hacky.

wayd is a python script that uses `launchd` to pop up every 15 minutes to ask what you're doing with a text input box. Fill in your current activity and it creates/appends a markdown file named with today's date with the current time and your activity.

If this is the first time wayd has run today, it creates a new file named dd-mm-yyyy.md that looks like this:

> # dd.mm.yyyy
>## today i will
>>==thrive (`or your own goal`)==
>
>## ideas // thoughts // things i did
>* time: activity

If wayd has already run or there's already a file named dd-mm-yyyy.md in the directory, then it just appends `* time: activity` to the end of the file.

You can keep the file open and add your own content to it as well, giving you a daily file with a mix of thoughts and timestamped activities."

## dependencies
* PySimpleGUI
* schedule

## to use
* download `wayd_py.py`
* download dependencies with
```
pip3 install PySimpleGUI

pip install schedule
```
* open `wayd.py` in your text editor and set `folder_path` to where you want your files saved
* use the Command Prompt to execute wayd_py.py
```

## tips

* find where your python executable is stored by running `where python` in the Command Prompt
* execute the file by typing <\path\to\python\executable\> <\path\to\wayd_py.py>
```

* customize how often wayd runs by changing the number in schedule (it's in minutes)
* customize the new file template by changing the string under `#if file doesn't exist` line in `wayd_py.py`


```
*/15 * * * * /path/to/your/python/executable /path/to/wayd.py
```


## future
* [ ] add ability to save settings
* [ ] package as standalone app
* [ ] make it prettier
