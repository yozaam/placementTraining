import requests
import re
import pandas as pd


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

r = requests.get(f"https://parade.com/947956/parade/riddles/", headers = headers).text

print(r)

riddle = re.findall('Riddle:</b>(.*?)<br><b>' , r, re.S)
answer = re.findall('<b>Answer:</b>(.*?)</p>' , r, re.S)

dic = {'riddle':riddle,'answer':answer}

df = pd.DataFrame(dic)

print(df)