from autoscraper import AutoScraper

url='https://www.flipkart.com/search?q=phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=phone%7CMobiles&requestId=a7afbf04-7b3b-4fc0-b7e0-7747d5b1bf7c&as-searchtext=phone%5D'
add_list=['₹10,499','realme C21Y (Cross Black, 64 GB)']
scrap=AutoScraper()

auto=scrap.build(url,add_list)

# print(auto)

# print(scrap.get_result(url, grouped=True))


print(scrap.get_result_similar(url, grouped=True))


