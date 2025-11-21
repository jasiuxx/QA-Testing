from playwright.sync_api import Page
import re

class HomePage:
    def __init__(self, page:Page,phrase):
        self.phrase=self.phrase=phrase
        self.page=page
        self.cookies_accept=page.get_by_role("button", name="Zgadzam się",exact=True)
        self.search_bar=page.get_by_role("textbox", name="Wyszukuj filmy i seriale...")
        
        
    def accept_cookies(self):
        self.cookies_accept.click()
        
    def search_movie(self):
        self.search_bar.click()
        self.search_bar.fill(self.phrase)