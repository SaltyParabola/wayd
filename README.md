# what are you doing? (wayd)

![wayd](wayd.png)
This is a python-only version of the original wayd program from spacekaila that works with the website notion.so to store all the files generated.
This version can work on any machine that runs python, and it can interface with notion.


wayd is a python script that uses the schedule library to pop up every 20 minutes (or a custom time period) to ask what you're doing with a text input box. Fill in your current activity and it creates/appends a markdown file named with today's date with the current time and your activity.

If this is the first time wayd has run today, it creates a new file named dd-mm-yyyy.md that looks like this:

> # dd-mm-yyyy
> ***Day of the week***
>**time:** activity

Where "Day of the week" is the weekday.

If wayd has already run or there's already a page named dd-mm-yyyy in the master page, then it just appends '**time:** activity' to the end of the page.

You can keep the notion page open and add your own content to it as well, giving you a daily page with a mix of thoughts and timestamped activities."

## dependencies
* PySimpleGUI
* schedule
* notion

## to use
* download `wayd_py_notion.py`
* download dependencies with
```
pip3 install PySimpleGUI

pip install schedule

pip install notion
```
* open `wayd_py_notion.py` in your text editor and set `token_v2` to the token_v2 value from your browser
  * to find the token, log in to your notion account, then go to developer tools> application and look for 'token_v2'
* set wayd_url to the url of the page you want all of your daily wayd pages to save to
* use the Command Prompt to execute wayd_py_notion.py
```

## tips


* customize how often wayd runs by changing the number in schedule (it's in minutes)
* customize the new file template by changing the string under `#if file doesn't exist` line in `wayd_py_notion.py`


```
*/15 * * * * /path/to/your/python/executable /path/to/wayd.py
```


## future
* [ ] add ability to save settings
* [ ] package as standalone app
* [ ] make it prettier
