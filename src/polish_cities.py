# Polish cities scraper
(fetch('https://en.wikipedia.org/wiki/List_of_postal_codes_in_Poland'), [open('cities.txt', 'a').write(city + '\n') for city in list(dict.fromkeys(list(filter(None, [text.strip() for text in response.css('li').css('a::text').getall()[:-55]]))).keys())])[-1]
