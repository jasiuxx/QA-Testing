from playwright.sync_api import Page,expect
import re


class SearchResultPage:
    def __init__(self, page:Page,phrase):
        self.phrase=re.compile(rf".*{phrase}.*", re.IGNORECASE)
        self.page=page
        self.header=page.locator("header")
        self.movie_link=page.get_by_role("link", name=self.phrase).first
        
    def check_movie_in_list(self):
        expect(self.header).to_contain_text(self.phrase)
        
    def click_movie(self):
        self.movie_link.click()

