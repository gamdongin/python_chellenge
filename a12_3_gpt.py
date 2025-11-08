import bs4
import asyncio
from playwright.async_api import async_playwright

# 동적 웹 페이지
# 회사 이름, 직무 제목, 설명 및 직무 링크

async def get_data(list_item):
    company_list_get_data = []
    job_title_list_get_data = []
    job_link_list_get_data = []
    for item in list_item:
        data = item.find("a", class_="listing-link--unlocked")
        if not data:
            continue  # 안전하게 None 처리

        company = data.find("p", class_="new-listing__company-name")
        company = company.get_text(strip=True) if company else ""

        job_title = data.find("h3")
        job_title = job_title.get_text(strip=True) if job_title else ""

        job_link = data.get("href") if data else ""

        company_list_get_data.append(company)
        job_title_list_get_data.append(job_title)
        job_link_list_get_data.append(job_link)
    return company_list_get_data, job_title_list_get_data, job_link_list_get_data


async def search_data(url, url_list, page):
    await page.goto(url)
    content = await page.content()
    soup = bs4.BeautifulSoup(content, "html.parser")

    data_job_table = soup.find_all("section", class_="jobs")
    list_item = []
    for data_i in data_job_table:
        list_item.extend(data_i.find_all("li", class_="new-listing-container"))

    company_list, job_title_list, job_link_list = await get_data(list_item)
    return company_list, job_title_list, job_link_list, url_list


async def search_a12_3(skill_name_input):
    url_list = []
    company_list = []
    job_title_list = []
    job_link_list = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

        skill_name = skill_name_input.strip()
        if not skill_name:
            await browser.close()
            return {"company": [], "job_title": [], "job_link": [], "description": []}

        url_input = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={skill_name}"
        url_list.append(url_input)

        for url in url_list:
            company_cache, job_title_cache, job_link_cache, url_list = await search_data(url, url_list, page)
            company_list.extend(company_cache)
            job_title_list.extend(job_title_cache)
            job_link_list.extend(job_link_cache)

        await browser.close()

    return {
        "company": company_list,
        "job_title": job_title_list,
        "job_link": job_link_list,
        "description": [""] * len(company_list)
    }

# 테스트용
if __name__ == "__main__":
    result = asyncio.run(search_a12_3("python"))
    print(result)