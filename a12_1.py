import bs4
import requests as requ

def get_data(list_item):
    company_list_get_data = []
    job_title_list_get_data = []
    description_list_get_data = []
    job_link_list_get_data = []
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
        
        company_list_get_data.append(company)
        job_title_list_get_data.append(job_title)
        description_list_get_data.append(description)
        job_link_list_get_data.append(job_link)
    return company_list_get_data, job_title_list_get_data, description_list_get_data, job_link_list_get_data

def serch_data(url,url_list):
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
    return company_list, job_title_list, description_list, job_link_list, url_list
    

# 회사 이름, 직무 제목, 설명 및 직무 링크
def search_a12_1(skill_name_input):
    url_list = []

    company_list = []
    job_title_list = []
    description_list = []
    job_link_list = []

    skill_name = skill_name_input
    url_input = f"https://berlinstartupjobs.com/skill-areas/{skill_name}/"
    url_list.append(url_input)
    for url in url_list:

        company_list_cache, job_title_list_cache, description_list_cache, job_link_list_cache, url_list = serch_data(url,url_list)
        
        company_list.extend(company_list_cache)
        job_title_list.extend(job_title_list_cache)
        description_list.extend(description_list_cache)
        job_link_list.extend(job_link_list_cache)
    #print(company_list)
    doc = {
        "company": company_list,
        "job_title": job_title_list,
        "description": description_list,
        "job_link": job_link_list
    }
    return doc

if __name__ == "__main__":
    search_a12_1()