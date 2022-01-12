from autoscraper import AutoScraper

url = 'https://github.com/krishnaik06?tab=repositories'

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ["85","Car-Price-Prediction","8.4k"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
# print(result)
scraper.get_result_similar("https://github.com/krishnaik06?tab=repositories",grouped=True)

scraper.set_rule_aliases({'rule_iv97': 'Stars', 'rule_t3ca': 'Title','rule_sxsg':'Followers'})
scraper.keep_rules(['rule_iv97', 'rule_t3ca','rule_sxsg'])
scraper.save('github-repository-search')

scraper.load('github-repository-search')

result=scraper.get_result_similar("https://github.com/iNeuronai?tab=repositories",group_by_alias=True)
