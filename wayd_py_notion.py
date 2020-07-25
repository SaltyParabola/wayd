import PySimpleGUI as sg
from datetime import datetime
import schedule
import time
import calendar
from notion.client import NotionClient
from notion_new import *

#package wayd to be a function
def wayd():
	# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
	client = NotionClient(token_v2=TOKEN FROM COOKIES)

	#URL to Notion master page
	wayd_url = YOUR URL
	
	#layout of input box
	wayd_layout = [
	    [sg.Text('What are you doing?')],
	    [sg.InputText()],
	    [sg.Submit(), sg.Cancel()]
	]
	
	#create input box, take input
	window = sg.Window('wayd', wayd_layout)
	event, values = window.read()
	
	
	#time that input was entered
	time = datetime.now().strftime('%H:%M')
	
	#today's date in two formats
	date_dash = datetime.now().strftime('%Y-%m-%d')
	date_dot = datetime.now().strftime('%d.%m.%Y')
	
	#get the day of the week
	day = calendar.day_name[datetime.today().weekday()]

	#close input box
	window.close()
	
	#daily page title
	daily_title = date_dash

	
	#define master page
	master_wayd = client.get_block(wayd_url)
	
	#create list of titles of existing children in master page
	titles = [o.title for o in master_wayd.children]

	#if content has been entered
	if values[0] != '':
		#if page already exists
		if daily_title in titles:
			today_index = titles.index(daily_title)

			#text
			text = '**' + time + '**: ' + values[0]

			new_text(master_wayd.children[today_index], text)

		#if file doesn't exist (aka program hasn't run today)
		else:
			#text
			text = '***' + day + '***\n\n**' + time +':** ' + values[0]
			wayd_new = new_page(wayd_url, daily_title)
			new_text(wayd_new,text)
	#if no content entered
	else:
		exit()

#add wayd function to queue every 20 minutes
schedule.every(20).minutes.do(wayd)

#execute everything to queue as added
while True:
	schedule.run_pending()
