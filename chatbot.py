from function import *
import pywhatkit
import time
ip = """Which ip you want to show ?

        [1] private
        [2] public
"""
bot.head()
name = bot.Name()
def Main():
    while True:
        query = input(Fore.GREEN +f"{name} :$ "+ Fore.RESET).lower()
        # fun.History(query)
        if bot.update(query) == "yes":
            bot.output("Update your Answer")
            ery = input(Fore.GREEN +f"{bot.name} :$ "+ Fore.RESET).lower()
            q = query.replace("update ","")
            load_json.Update_answer(q,ery)
        elif load_json.json_process_input(query) != None:
            bot.output(load_json.json_process_input(query))
        elif bot.process_input(query,"time") == "yes":
            bot.output(bot.get_time())
        elif bot.process_input(query,"my name") == "yes":
            bot.output("your name is "+name)
        elif bot.process_input(query,"my ip") == "yes":
            bot.output(ip)
            usr = input(Fore.GREEN +f"{name} :$ "+ Fore.RESET).lower()
            if "1" in usr or "private" in usr:
                pri_ip = bot.Ip()
                bot.output("your private is "+pri_ip)
            elif "2" in usr or "public" in usr:
                pub_ip = bot.getIP()
                bot.output("your public is "+pub_ip)
        elif bot.process_input(query,"top news") == "yes":
            bot.get_news()
        elif "/clear" in query or "clear" in query:
            bot.Clear()
            bot.head()
        elif "exit" in query or "/exit" in query:
            exit()
        elif bot.searching(query) == "yes":
            a = query.replace("search","")
            bot.output("searching "+a)
            time.sleep(2)
            pywhatkit.search(a)
        elif bot.opening(query) == "yes":
            a = query.replace("open","")
            if bot.process_input(a,"facebook") == "yes":
                bot.output("opening facebook...")
                time.sleep(2)
                bot.open_facebook()
            elif bot.process_input(a,"google") == "yes":
                bot.output("opening google...")
                time.sleep(2)
                bot.open_google()
            elif bot.process_input(a,"instagram") == "yes":
                bot.output("opening instagram...")
                bot.open_insta()
            elif bot.process_input(a,"linkedin") == "yes":
                bot.output("opening linkedin...")
                bot.open_linkedin()
            elif bot.process_input(a,"telegram") == "yes":
                bot.output("opening telegram...")
                bot.open_telegram()
            elif bot.process_input(a,"github") == "yes":
                bot.output("opening github...")
                bot.open_github()
            else:
                bot.output("Searching "+a)
                time.sleep(2)
                pywhatkit.search(a)
        elif bot.playing(query) == "yes":
            query = query.replace("play","")
            query = query.replace("music","")
            query = query.replace("song","")
            bot.output("playing "+query+"song...")
            time.sleep(2)
            pywhatkit.playonyt(query)   
        elif "what is" in query or "who is" in query or "say something" in query or "do you know" in query:
            bot.check_on_wikipedia(query)
        # elif process_input(query,"write note" or "write a note") == "yes":
        #     output("write here what you want to note down")
        #     note = input(Fore.GREEN +f"{name} :$ "+ Fore.RESET).lower()
        #     Note_write(note)
        # elif process_input(query,"show note" or "see my note" or "show a note") == "yes":
        #     show_note()
        # elif process_input(query,"remove note" or "remove a note" or "delete a note") == "yes":
        #     remove_note()
        elif "me" in query or "about me" in query:
            sn = load_json.json_single_data("me")
            bot.output(sn) 
        elif "see you later" in query or "goodbye" in query or "i am leaving" in query or "have a good day" in query or "bye" in query:
            by = load_json.single_data("bye")
            bot.output(by)
        elif "i am good" in query or "not bad" in query or "I am fantastic" in query or "i am okey" in query or "iam feeling good" in query or "iam great" in query:
            wl = load_json.single_data('doing well')
            bot.output(wl)
        elif "how are you" in query:
            bot.output(load_json.single_data('good'))
        elif "male" in query or "female" in query:
            bot.output(load_json.single_data("gender"))
        elif load_json.json_process_input(query) == None:
                bot.output("I don't know,What it menes")
                bot.Note("if you dont know the answer write (sorry)")
                quer = input(Fore.GREEN +f"{name} :$ "+ Fore.RESET+"it menes ") # jahid
                if "i dont know" in quer or "sorry" in quer:
                    bot.output("ok! sir.")
                else:
                    aa = quer.replace("it menes :$ ","")
                    load_json.Update_answer(query,aa)
                    bot.output("i will remember it next time")
Main()