import requests
jokes=[]
for i,j in enumerate(range(1,500)):
    url=f'https://api.icndb.com/jokes/{j}'
    response=requests.get(url)
    data=response.json()
    try:
        material=data['value']['joke']
        jokes.append(material)
    except:
        print("No jokes found",j)
print("Done")
with open('jokes.csv','w') as jj:
    jokes=str(jokes)
    jj.write(jokes)
jj.close()
