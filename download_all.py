import urllib.request
import json

repo="ViolaDeRenzis/updowninjections"
url= "https://api.github.com/repos/"+repo+"/releases/latest"

f= urllib.request.urlopen(url)
content = f.read().decode()
f.close()
content = json.loads(content)

for asset in content['assets']:
    urlfile = asset['browser_download_url']
    filename=urlfile.split('/')[-1]
    print(urlfile)
    urllib.request.urlretrieve(urlfile,filename)
