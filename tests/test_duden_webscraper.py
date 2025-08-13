from duden_webscraper.duden_web_scraper import DudenWebScraper
import pytest

@pytest.mark.parametrize("word, expected_lemma",[
    ("Pferd", "Pferd"),
    ("Maskotte", "Mas­kot­te"),
    ("Kaf", "Kaf"),
    ("Shop", "Shop")
])
def test_lemma_must_be_equals_to_word(word, expected_lemma):
    scraper = DudenWebScraper()
    result = scraper.get_word_info(word)

    assert result["lemma"] == expected_lemma
