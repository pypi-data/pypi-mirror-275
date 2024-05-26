#By Python_Fucker On 2024/5/25
import mechanicalsoup
class TopHubFetcher:
    def __init__(self):
        self.url = 'https://tophub.today/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.browser = mechanicalsoup.StatefulBrowser()
        self.browser.session.headers.update(self.headers)
    def fetch_data_from_website(self, t):
        self.browser.open(self.url)
        soup = self.browser.get_current_page()
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
    def weibo(self):
        return self.fetch_data_from_website(4)
    def zhihu(self):
        return self.fetch_data_from_website(5)
    def weixin(self):
        return self.fetch_data_from_website(6)
    def baidu(self):
        return self.fetch_data_from_website(7)
    def bilibili(self):
        return self.fetch_data_from_website(12)
    def douyin(self):
        return self.fetch_data_from_website(13)
    def aiwu(self):
        return self.fetch_data_from_website(16)
    def tieba(self):
        return self.fetch_data_from_website(17)
    def tengxun(self):
        return self.fetch_data_from_website(18)
