from bs4 import BeautifulSoup
import lxml
import requests

class ppt_parser:
    def __init__(self):
        self.parser_page('https://www.ptt.cc/bbs/MobileComm/index.html')

    def parser_page(self, url):
        self.ppt_request = requests.get(url)
        self.html_parser = BeautifulSoup(self.ppt_request.text, 'lxml')

    def print_current_page_row_news_title(self):
        title_name_tags = self.html_parser.select('div.title a')
        for title_name_tag in title_name_tags:
            print(title_name_tag.text)

    def go_to_next_pate(self):
        next_page_button = self.html_parser.find('a', text='下頁 ›')
        next_page_url = 'https://www.ptt.cc' + next_page_button['href']
        self.parser_page(next_page_url)

    def print_next_page_row_news_title(self):
        self.go_to_next_pate()
        self.print_current_page_row_news_title()

    def go_to_pevious_page(self):
        previous_page_button = self.html_parser.find('a', text='‹ 上頁')
        previous_page_url = 'https://www.ptt.cc' + previous_page_button['href']
        self.parser_page(previous_page_url)

    def print_previous_page_row_news_title(self):
        self.go_to_pevious_page()
        self.print_current_page_row_news_title()

    def print_page_with_iteration(self, print_page_func, times):
        for i in range(times):
            print_page_func()
            print('*********time: %s *********' % (i))
        print('final times')



if __name__=='__main__':
    pt_par = ppt_parser()
    pt_par.print_current_page_row_news_title()
    print('*********previous*********')
    pt_par.print_page_with_iteration(pt_par.print_previous_page_row_news_title, 5)
    # pt_par.print_current_page_row_news_title()
    # print('***********previous**************')
    # pt_par.print_previous_page_row_news_title()
    # print('***********previous**************')
    # pt_par.print_previous_page_row_news_title()
    # print('***********previous**************')
    # pt_par.print_previous_page_row_news_title()
    # print('***********next**************')
    # pt_par.print_next_page_row_news_title()
    # print('***********next**************')
    # pt_par.print_next_page_row_news_title()
