import mechanicalsoup

def fetch_data_from_website(t):
    url = 'https://tophub.today/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    browser = mechanicalsoup.StatefulBrowser()
    browser.session.headers.update(headers)
    browser.open(url)
    soup = browser.get_current_page()

    result = []  
    div_cc_cd_list = soup.select('div.cc-cd')
    for div_cc_cd in div_cc_cd_list:
        category = div_cc_cd.select_one('.cc-cd-is').text.strip()
        a_tags = div_cc_cd.select('.cc-cd-cb a')
        links = []
        for a_tag in a_tags:
            text = a_tag.text.strip()
            link = a_tag.get('href')
            if link:
                links.append({'text': text, 'link': link})
        result.append({'category': category, 'links': links})

    return result[t]
def Zhihu():
 return fetch_data_from_website(1)