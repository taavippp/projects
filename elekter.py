import requests as rq
import regex as re

amt=10

def multiple_min(iterable=[], amount=1):
    temp=list(iterable)
    results=[]
    num=0
    for a in range(amount):
        num=min(temp)
        results.append(num)
        temp.remove(num)
    return results

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

site=rq.get("http://digigrupp.com/internal/elekter/")
text=site.text.split("\n")
to_del=[]
for i,val in enumerate(text):
    val=remove_html_tags(val)
    if len(val)<=1 or val.find("nbsp")!=-1 or val=="\r" or val.find("(")!=-1 or val.find("[")!=-1:
        to_del.append(i)
    val=val.replace("\r","")
    text[i]=val
for i in range(len(to_del)-1,-1,-1):
    text.pop(to_del[i])

counter=0
price=[]
hour=[]
for val in text:
    if len(hour)==24:
        break
    if val[0].isnumeric():
        counter+=1
        if counter%2==0:
            hour.append(int(val))
        else:
            price.append(float(val))
for i,val in enumerate(price):
    if str(val).find(".0")!=-1:
        price[i]=int(val)

def output():
    lowest=multiple_min(price,amt)
    for val in lowest:
        hour_val=hour[price.index(val)]
        print("Kell {}-{}: \t{} €".format(hour_val,hour_val+1,val))
    return

output()
while True:
    amt=int(input("Mitu madalaimat tundi tahad näha?\n"))
    output()
