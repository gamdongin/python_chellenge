from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

from a12_1 import search_a12_1
from a12_2 import search_a12_2  
from a12_3 import search_a12_3

app = Flask(__name__)
app.jinja_env.globals.update(zip=zip) # html에서 zip 쓸려면 필요함

"""
Do this when scraping a website to avoid getting blocked.
headers = {
      'User-Agent':
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
      'Accept':
      'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Accept-Language': 'en-US,en;q=0.5',
}
response = requests.get(URL, headers=headers)
"""


@app.route("/")
def DohU():
    skill_name = request.args.get("skill_name_serch", None)
    data = []
    if skill_name:
        berlinstartupjobs = search_a12_1(skill_name)
        print(" berlinstartupjobs done ")
        weworkremotely = search_a12_2(skill_name)
        print(" weworkremotely done ")
        web3 = search_a12_3(skill_name)
        print(" web3 done ")
        data = [berlinstartupjobs, weworkremotely, web3]
    return render_template("DohU.html", data=data, skill_name=skill_name)


if __name__ == "__main__":
    app.run(debug=True)