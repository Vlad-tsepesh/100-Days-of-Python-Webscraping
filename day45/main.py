from scraper.article_scraper import ArticleScraper
from scraper.top_movies_scraper import TopMoviesScraper

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
file_name = "top_movies"
top_movies = TopMoviesScraper(file_name, url)
top_movies.run()

url = "http://news.ycombinator.com/news"
file_name = "articles"
articles = ArticleScraper(file_name, url)
articles.run()

