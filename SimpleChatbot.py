try:
    import webbrowser as wb
    import wikipedia as info
    import os
    from datetime import date
    import time
    print("\033[1;32m**********\nChatbot\n**********\n")
except:
	print("ERROR : required modules not downloaded in the system")

user_in=""
result=""
bot_status=True
answer=""

def bot(a):
	global bot_status
	print(f"BOT : {a}")
	bot_status=False
	
def user():
	global user_in
	user_in=input("USER : ")
	
def search(URL):
	wb.open(URL)
	
curr_time = time.localtime()
curr_clock = time.strftime("%H:%M:%S", curr_time)
def time():
	global curr_time,curr_clock	
	bot(f"Current time is {curr_clock}")

def info_result(topic,*args):
	global result
	bot("searching..........")
	try:
		result=info.summary(topic,sentences=250)
		bot(f"{result}")
	except:
		bot("Info can't be found")
	
def calculate(expression):
	global answer
	try:
		answer=eval(expression)
		bot(f"{answer}")
	except:
		bot("Invalid Syntax")

today2 = date.today()		
def date():
	global today2,date2
	date2 = today2.strftime("%B %d, %Y")
	bot(f"Today's date is {date2}")
		
def git():
	wb.open("https://github.com/Omanshu209?tab=repositories")
	
def youtube():
	wb.open("https://youtube.com")
	
def search_youtube(search):
	wb.open(f"https://m.youtube.com/results?sp=mAEA&search_query={search}")

bot("Hello! How can I help you?(Enter \"support\" for more details)")

run=True
while run:
	if bot_status==False:
		user()
	if "browser" in user_in.lower():
		bot("Enter The URL")
		user()
		search(user_in)
	elif "quit" in user_in.lower() or "exit" in user_in.lower():
		bot("Bye")
		run=False
	elif "info" in user_in.lower():
		bot("Enter the topic you want to search about")
		user()
		info_result(user_in)
	elif "date" in user_in.lower():
		date()
	elif "time" in user_in.lower():
		time()
	elif "name" in user_in.lower() and "your" in user_in.lower():
		bot("My name is Omanshu (Developer)")
	elif "calculator" in user_in.lower() or "solve" in user_in.lower():
		bot("Enter the mathematic expression you want to solve")
		user()
		calculate(user_in)
	elif "game" in user_in.lower():
		bot("To play my GUI or CUI games, please visit \"https://github.com/Omanshu209?tab=repositories\" or enter \"Github Profile\"")
	elif "github" in user_in.lower() and "profile" in user_in.lower():
		git()
	elif "open" in user_in.lower() and "youtube" in user_in.lower():
		youtube()
	elif "youtube" in user_in.lower() and "search" in user_in.lower():
		bot("Enter the words to search in youtube")
		user()
		user_in2=user_in.replace(" ","+")
		search_youtube(user_in2)
	elif "support" in user_in.lower():
		bot("The keywords are as follows:\n\t .Open an URL(Surf the internet) -- \"browser\"(Internet Required)\n\t .Search information about a topic -- \"info\"(Internet Required)\n\t .Calculator -- \"calculator\"\n\t .View my(developer) Github Profile and see my projects or play games -- \"github profile\"(Internet Required)\n\t .Open or surf youtube -- \"open  youtube or search youtube\"(Internet Required)\n\t .Today's Date -- \"date\"\n\t .Current Time -- \"time\"")
	else:
		prev_data=user_in
		bot(f"Do want to search about \"{user_in}\" ?")
		user()
		if "yes" in user_in.lower():
			info_result(prev_data)
		else:
		    bot("I didn't understand, pls type again")
