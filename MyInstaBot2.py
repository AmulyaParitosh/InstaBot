import random
from instapy import InstaPy


USERNAME = "indibox.in"
PASSWORD = "b0@Rd.B1aCK743"


TAGS = ["digitalart", "redbubble", "tshirtprinting"]
COMMENTS = ["Amazing", "Fablous work!", "Really Cool", "I like your stuff"]
COMMENT_REPLIES = ["Thankuu", "Thanks"]
LANG = ["LATIN"]


def getran(a: int, b: int):
    return random.randrange(a, b)


session = InstaPy(username=USERNAME, password=PASSWORD)

session.set_comments(COMMENTS)
session.set_mandatory_language(enabled=True, character_set=LANG)
session.set_action_delays(enabled=True,
                          randomize=True,
                          random_range_from=25,
                          random_range_to=80)

session.set_quota_supervisor(enabled=True,
                             peak_likes_hourly=getran(18, 20),
                             peak_likes_daily=getran(300, 400),
                             peak_comments_hourly=getran(11, 14),
                             peak_follows_hourly=getran(18, 20),
                             peak_follows_daily=getran(150, 200))

session.set_do_like(enabled=True, percentage=getran(95, 100))
session.set_do_comment(enabled=True, percentage=getran(80, 95))
session.set_do_follow(enabled=True, percentage=getran(50, 60))

session.login()

session.like_by_tags(TAGS, use_random_tags=True, amount=getran(5, 15))
