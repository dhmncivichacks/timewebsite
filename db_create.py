from project import db
from project.models import Blog
from project.models import BlogPost
from project.models import Event
from project.models import Person
from project.models import Organization
from project.models import NewsItem
from project.models import Sponsor
from project.models import User

# create the database and the db table
db.create_all()

# insert stub data
db.session.add(User("admin", "ad@min.com", "admin", url_handle="adminy"))
db.session.add(Blog("Foo Blarg of Blag Blog", url_handle="foo_blarg_of_blag_blog"))
db.session.add(BlogPost("A Blog Post Title!", "Post body", author_id=1, url_handle="a_blog_post"))
db.session.add(Event("BarCamp", url_handle="barcamp", description="Unconferences are much more fun and productive than regular be-talked-at conferences."))
db.session.add(Person("Benny Hill", url_handle="bennyhill", biography="Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.", added_by_id=1))
db.session.add(Person("Samurai Jack", url_handle="samuraijack", biography="Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.", added_by_id=1))
db.session.add(Person("Emo Phillips", url_handle="emophillips", biography="Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.", added_by_id=1))
db.session.add(Person("Betty White", url_handle="bettywhite", biography="Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.", added_by_id=1))
db.session.add(Person("Carol Burnett", url_handle="carol_burnett", biography="Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.", added_by_id=1))
db.session.add(Person("Mel Blanc", url_handle="mel_blanc", biography="Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.", added_by_id=1))
db.session.add(Organization("A Makerspace", url_handle="a_makerspace", description="Let's make stuff!"))
db.session.add(NewsItem("FLASH: News Ticker Acheives Sentience!", url_handle="sentient_news_ticker_is_sentient"))
db.session.add(Sponsor("Good Guy Greg's Gondola Gallery", url_handle="good_guy_gregs_gondola_gallery", description="We love N.E. T.I.M.E community -- here have some money!"))


# commit the changes
db.session.commit()
