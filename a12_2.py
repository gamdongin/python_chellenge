import bs4
import requests as requ

# 회사 이름, 직무 제목, 설명 및 직무 링크

def get_data(list_item):
    company_list_get_data = []
    job_title_list_get_data = []
    job_link_list_get_data = []
    #count = 0
    for item in list_item:
        #count += 1
        if item.get("id") == "sponsor_2": # 5번째는 부트캠프 광고라서 패스
            company = "_ADvertisement_"
            job_title = "_ADvertisement_"
            job_link = "_ADvertisement_"
        else:
            data = item.find_all("td")
            
            company_html = data[1]
            company = company_html.find("h3").get_text(strip=True) # 회사 이름
            
            job_title_html = data[0]
            job_title = job_title_html.find("h2").get_text(strip=True) # 직무 제목
            job_link = job_title_html.find("a").get("href") # 직무 링크
        
        company_list_get_data.append(company)
        job_title_list_get_data.append(job_title)
        job_link_list_get_data.append(job_link)
    return company_list_get_data, job_title_list_get_data, job_link_list_get_data

def serch_data(url,url_list):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
    }
    response = requ.get(url,headers=headers)
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    
    page = soup.find("ul",class_="pagination")
    if page:
        li_link = page.find("li",class_="next")
        link = li_link.find("a",class_="page-link")
        page_link = link.get("href")
        if page_link != "#":
            url_list.append(f"https://web3.career{page_link}")
    else:
        pass
    
    data_job_table = soup.find("tbody",class_="tbody")
    list_item = data_job_table.find_all("tr")
    
    company_list, job_title_list, job_link_list = get_data(list_item)
    return company_list, job_title_list, job_link_list, url_list
    
def search_a12_2(skill_name_input):
    url_list = []

    company_list = []
    job_title_list = []
    job_link_list = []

    skill_name = skill_name_input
    url_input = f"https://web3.career/{skill_name}-jobs"
    url_list.append(url_input)
    for url in url_list:

        company_list_cache, job_title_list_cache, job_link_list_cache, url_list = serch_data(url,url_list)
        
        company_list.extend(company_list_cache)
        job_title_list.extend(job_title_list_cache)
        job_link_list.extend(job_link_list_cache)
    #print(company_list)
    doc = {
        "company": company_list,
        "job_title": job_title_list,
        "job_link": job_link_list
    }
    return doc

if __name__ == "__main__":
    search_a12_2()