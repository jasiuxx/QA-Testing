from playwright.sync_api import Page, expect
from pages.detail_page import DetailPage
from pages.home_page import HomePage
from pages.search_result_page import SearchResultPage
import pytest

#dane wejsciowe 
@pytest.mark.parametrize("phrase", [
    "the pickup", 
    "The Iron Heart"
    ])
def test_example(page: Page,phrase):
    page.goto("https://vod.film/") #wejscie na strone glowna 
    home_page=HomePage(page,phrase)
    home_page.accept_cookies() #zatwierzenie zbierania danych 
    home_page.search_movie()  #klik w pole wyszukiwania i wpisanie frazy
    
    search_result_page=SearchResultPage(page,phrase)
    search_result_page.check_movie_in_list() #sprawdzenie film jest na liscie 
    search_result_page.click_movie() # wejscie w szczegoly filmu
    
    detail_page=DetailPage(page,phrase)
    detail_page.check_title_in_h1() #sprawdzenie czy h1 zawiera fraze 
    detail_page.play_movie() #odtworzenie filmu
    #detail_page.mute_sound() #wyciszenie dźwięku
    detail_page.wait_for_popup() #obsługa popup
    detail_page.get_popup_url() #sprawdzenie url popupa