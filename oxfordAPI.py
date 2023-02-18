import requests

from pprint import pprint as print

app_id = ""
app_key = ""
language = "en-gb"

word_id = "python"
url = "" + language + "/" + word_id.lower()

r = requests.get(url, headers={"app_id,", "app_key": app_key})
print(r.status_code)
res = r.json()
print(res)
