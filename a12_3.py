import bs4
import requests as requ
from playwright.sync_api import sync_playwright

# 동적 웹 페이지임
# 회사 이름, 직무 제목, 설명 및 직무 링크

def get_data(list_item):
    company_list_get_data = []
    job_title_list_get_data = []
    job_link_list_get_data = []
    for item in list_item:
        data = item.find("a", class_="listing-link--unlocked")
            
        company = data.find("p", class_="new-listing__company-name").get_text(strip=True) # 회사 이름

        job_title = data.find("h3").get_text(strip=True) # 직무 제목
        job_link = data.get("href") # 직무 링크

        company_list_get_data.append(company)
        job_title_list_get_data.append(job_title)

        job_link_list_get_data.append(job_link)
    return company_list_get_data, job_title_list_get_data, job_link_list_get_data

def serch_data(url,url_list,page):
    
    page.goto(url)
    content = page.content()
    soup = bs4.BeautifulSoup(content, "html.parser")

    data_job_table = soup.find_all("section",class_="jobs")
    list_item = []
    for data_i in data_job_table:
        list_item.extend(data_i.find_all("li", class_="new-listing-container"))
    
    company_list, job_title_list, job_link_list = get_data(list_item)
    return company_list, job_title_list, job_link_list, url_list
    
def search_a12_3(skill_name_input):
    url_list = []

    company_list = []
    job_title_list = []
    job_link_list = []

    spw = sync_playwright().start()
    browser = spw.chromium.launch(headless=True)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
    }
    page = browser.new_page(user_agent=headers["User-Agent"])

    skill_name = skill_name_input
    url_input = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={skill_name}"
    url_list.append(url_input)
    for url in url_list:
        
        company_list_cache, job_title_list_cache, job_link_list_cache,url_list = serch_data(url,url_list,page)
        
        company_list.extend(company_list_cache)
        job_title_list.extend(job_title_list_cache)
        #description_list.extend(description_list_cache)
        job_link_list.extend(job_link_list_cache)

    browser.close()
    spw.stop()
    #print(company_list)
    doc = {
        "company": company_list,
        "job_title": job_title_list,
        "job_link": job_link_list,
        "description": [""]*len(company_list) 
    }
    return doc

if __name__ == "__main__":
    search_a12_3()