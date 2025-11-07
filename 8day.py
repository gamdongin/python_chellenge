import bs4
import requests as requ

def get_data(list_item):
    company_list = []
    job_title_list = []
    description_list = []
    job_link_list = []
    for item in list_item:
        data = item.find("div",class_="bjs-jlid__wrapper")
        company_and_job_title = data.find("div",class_="bjs-jlid__meta")
        
        job_title_html = company_and_job_title.find("h4",class_="bjs-jlid__h")
        job_title = job_title_html.find("a").get_text(strip=True) # 직무 제목
        job_link = job_title_html.find("a").get("href") # 직무 링크
        
        company_html = company_and_job_title.find("a",class_="bjs-jlid__b")
        company = company_html.get_text(strip=True) # 회사 이름
        
        description_html = data.find("div",class_="bjs-jlid__description")
        description = description_html.get_text(strip=True) # 설명
        
        company_list.append(company)
        job_title_list.append(job_title)
        description_list.append(description)
        job_link_list.append(job_link)
    return company_list, job_title_list, description_list, job_link_list

def serch_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
    }
    response = requ.get(url,headers=headers)
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    
    page = soup.find("ul",class_="bsj-nav")
    if page:
        links = page.find_all("a",class_="next")
        for link in links:
            page_link = link.get("href")
            url_list.append(page_link)
    else:
        pass
    ul_list = soup.find("ul",class_="jobs-list-items")
    list_item = soup.find_all("li",class_="bjs-jlid")
    
    company_list, job_title_list, description_list, job_link_list = get_data(list_item)
    return company_list, job_title_list, description_list, job_link_list
    

# 회사 이름, 직무 제목, 설명 및 직무 링크

url_list = [
    "https://berlinstartupjobs.com/engineering/",
    "https://berlinstartupjobs.com/skill-areas/python/",
    "https://berlinstartupjobs.com/skill-areas/typescript/",
    "https://berlinstartupjobs.com/skill-areas/javascript/",
]

next_page = []

company_list = []
job_title_list = []
description_list = []
job_link_list = []

for url in url_list:

    company_list_cache, job_title_list_cache, description_list_cache, job_link_list_cache = serch_data(url)
    company_list.append(company_list_cache)
    job_title_list.append(job_title_list_cache)
    description_list.append(description_list_cache)
    job_link_list.append(job_link_list_cache)

print(company_list)
#print(job_title_list)
#print(description_list)
#print(job_link_list)

#===============================================

skill_name = input("skill : ")
url = f"https://berlinstartupjobs.com/skill-areas/{skill_name}/"
company_list_cache, job_title_list_cache, description_list_cache, job_link_list_cache = serch_data(url)
print(company_list_cache)

    
    