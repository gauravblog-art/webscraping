from autoscraper import AutoScraper

url = 'https://github.com/krishnaik06?tab=repositories'

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ["69","Finding-an-Outlier","12.3k"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
# print(result)
scraper.get_result_similar("https://github.com/krishnaik06?tab=repositories",grouped=True)
