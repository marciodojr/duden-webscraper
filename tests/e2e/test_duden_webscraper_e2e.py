from duden_webscraper.duden_web_scraper import DudenWebScraper
import pytest

@pytest.mark.parametrize("word", [
    ("Pferd"),
    ("Maskotte"),
    ("Kaf"),
    ("Shop"),
])
def test_lemma_must_be_equals_to_word(word):
    scraper = DudenWebScraper()
    result = scraper.get_word_info(word)

    assert result["lemma"] == word
