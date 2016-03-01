from project import db
from project.models import Blog
from project.models import BlogPost
from project.models import Event
from project.models import Person
from project.models import Organization
from project.models import NewsItem
from project.models import Sponsor

# create the database and the db table
db.create_all()

# insert data
db.session.add(Blog("Foo Blarg of Blag Blog"))
db.session.add(BlogPost("Good", "I\'m good.", author_id=1))
db.session.add(Event("BarCamp"))
db.session.add(Person("Benny Hill"))
db.session.add(Organization("Wanda's Widgets"))
db.session.add(NewsItem("FLASH: News Ticker Acheives Sentience!"))
db.session.add(Sponsor("Good Guy Greg's Gondola Gallery"))

# commit the changes
db.session.commit()
