# Indian movies scraper
import csv; open('movies.csv', 'w').write('Song Heading,Singer,Composer,Lyricist,ActorFilm (Year),Category\n'); [(fetch('https://m.hindigeetmala.net/movie/blockbuster_movies_1.php?page=' + str(page)), [(fetch('https://m.hindigeetmala.net' + url), [csv.writer(open('movies.csv', 'a')).writerow([''.join(col.css(' *::text').getall()) for col in row.css('td')][1:]) for row in response.css('table')[:-1].css('tr') if len(row.css('td'))]) for url in response.css('div[class="col-xs-6 col-md-4 col-lg-3"]').css('a::attr(href)').getall()]) for page in range(1, 6)]
