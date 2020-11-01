from models import User, Posts, Tag, PostTag, db
from app import app

db.drop_all()
db.create_all()

u1 = User(first_name="Hunter", last_name="Piggot")
u2 = User(first_name="Apollo", last_name="Piggot")
u3 = User(first_name="Annie", last_name="Oakley")

p1 = Posts(title="Test1", content="Hello World", created_at="10-26-2020", user_id=1)
p2 = Posts(title="Test2", content="World Hello", created_at="10-25-2020", user_id=2)
p3 = Posts(title="Test3", content="Test Commment", created_at="10-24-2020", user_id=3)

t1 = Tag(name="funny")
t2 = Tag(name="NFSW")
t3 = Tag(name="serious")

pt1 = PostTag(post_id=1, tag_id=1)
pt2 = PostTag(post_id=2, tag_id=1)
pt3 = PostTag(post_id=3, tag_id=1)
pt4 = PostTag(post_id=1, tag_id=2)
pt5 = PostTag(post_id=3, tag_id=3)
pt6 = PostTag(post_id=2, tag_id=3)

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.commit()
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.commit()
db.session.add(t1)
db.session.add(t2)
db.session.add(t3)
db.session.commit()
db.session.add(pt1)
db.session.add(pt2)
db.session.add(pt3)
db.session.add(pt4)
db.session.add(pt5)
db.session.add(pt6)
db.session.commit()