import os
from os import path
import random
import json
import re
from pschatbot import chatbot as bot
from colorama import Fore
class load_json():   
    def learing_data(a):
        try:
            filename = "Data/Learning_data.json"
            with open(filename) as QNA:
                data = json.load(QNA)
                da = data[a]
                if a in data:
                    if type(data[a]) == list:
                        da = random.choice(data[a])
                        return da
                    else:
                        return data[a]
                else:
                    print("sorry , no find data")
        except Exception as e:
            return "No"
        
    def json_process_input(out):
        data_list = []
        file = "Data/Learning_data.json"
        with open(file) as qn:
            data = json.load(qn)
            for i in data:
                data_list.append(i)

        for k in range(len(data_list)):
            t = data_list[k]
            txt = t.lower()
            count = 0
            x = re.split("\s", txt) #how are you
            y = re.split("\s",out) # name
            for i in range(len(y)):
                for j in range(len(x)):
                    if y[i] == x[j]:
                        count +=1
            if count == len(x):
                return load_json.learing_data(txt) 
    def learng_mood(a, b):
        filename = "Data/Learning_data.json"
        dictObj = []
        if path.isfile(filename) is False:
            raise Exception("File not found")
        with open(filename) as fp:
            dictObj = json.load(fp)
            dictObj.update({f"{a}": [f"{b}"]})
        with open(filename, 'w') as json_file:
            json.dump(dictObj, json_file,
                  indent=4,
                  separators=(',', ': '))
        
    def Update_answer(a,b ,filename="Data/Learning_data.json"):
    	with open(filename,'r+') as file:
            data_list = []
            dictObj = []
            tes = 0
            file_data = json.load(file)
            for da in file_data:
                data_list.append(da)
            for i in range(len(data_list)):
                if a == data_list[i]:
                    tes +=1
            if tes == 0:
                load_json.learng_mood(a,b)
            if tes == 1:
                file_data[a].append(b)
                file.seek(0)
                json.dump(file_data, file, indent = 4)
                bot.output("done")

    def single_data(a):
        ans = []
        file ="Data/single.json"
        with open(file) as single:
            data = json.load(single)
            for da in data[f'{a}']:
                ans.append(da)
            daa = random.choice(ans)
            return daa
        
    def json_single_data(a):
        ans = []
        file = "Data/single.json"
        with open(file) as single:
            data = json.load(single)
            for da in data[f'{a}']:
                ans.append(da)
            daa = random.choice(ans)
            return daa
        
# def Note_write(a):
#     output("Here give the file name.")
#     file = input(Fore.GREEN +f"File name:$ "+ Fore.RESET).lower()
#     f = open(f"/Data/Note/{file}.txt", "a")
#     output("OK! I am saving it")
#     f.write(a)
#     f.close()
# def remove_note():
#     output("Here give your file name")
#     nm = input(Fore.GREEN +"File name:$ "+ Fore.RESET).lower()
#     if os.path.exists(f"/Data/Note/{nm}.txt"):
#         os.remove(f"/Data/Note/{nm}.txt")
#         output("Deleted done!")
#     else:
#         output("The file does not exist")
# def show_note():
#     output("Here give your file name")
#     fnm = input(Fore.GREEN +"File name:$ "+ Fore.RESET).lower()
#     f = open(f"/Data/Note/{fnm}.txt", "r")
#     output(f.read())