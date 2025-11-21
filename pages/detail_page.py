from playwright.sync_api import Page,expect
import re

class DetailPage:
    def __init__(self, page:Page,phrase):
        self.phrase=self.phrase=re.compile(rf".*{phrase}.*", re.IGNORECASE)
        self.page=page
        self.h1=page.locator("h1")
        self.play=page.locator("#player-container button").filter(has_text=re.compile(r"^Play$"))

    def check_title_in_h1(self):
        expect(self.h1).to_contain_text(self.phrase)
        
    def check_play_avalible(self):
        expect(self.play).to_contain_text("Play")
        
        
    def wait_for_popup(self):
        self.page.wait_for_timeout(1000  )#czekanie od 1 sekundy po odwtworzeniu playera
        self.page.locator("#popup").get_by_text("Zarejestruj się").click(timeout=120000) #czekanie do 60 sekund na popout
        
        
    def play_movie(self):
        self.play.click(timeout=10000)
        
    def mute_sound(self):
        self.page.get_by_role("button", name="Mute").click()
        
    def get_popup_url(self):
        print('Przekierowanie popup: ' + self.page.url) #sprawdzenie url popupa
        
    