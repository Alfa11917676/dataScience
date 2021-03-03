import os
BASE_DIR = 'F:\\dataScience\\crawler\\pepper\\'
baseurl='https://www.pepperfry.com/site_product/search?q='
items = ['king bed', 'queen bed', 'tea table', 'study table']
urls = []
directories = []
for item in items:
    Uurl='+'.join(item.split(" "))
    Udir="-".join(item.split(" "))
    urls.append(baseurl+Uurl)
    directories.append(Udir)

    directoryPath=BASE_DIR+Udir
    if not os.path.exists(directoryPath):
        os.mkdir(directoryPath)
print(urls)
print(directories)