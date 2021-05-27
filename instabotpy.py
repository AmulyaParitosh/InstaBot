import random
from instapy import InstaPy



USERNAME = "indibox.in"
PASSWORD = "b0@Rd.B1aCK743"

TAGS = []
COMMENTS = ["Amazing"]
COMMENT_REPLIES = []



def getran(a : int, b : int):
    return random.randrange(a, b)



session = InstaPy(username=USERNAME, password=PASSWORD)
session.login()

session.set_action_delays(
        enabled= True,
        like= getran(1,4),
        comment= getran(2,5),
        follow= getran(3,6),
        randomize= True,
        random_range_from= getran(1,3),
        random_range_to= getran(3,6)
        )

session.like_by_tags(TAGS, amount= getran(getran(5,11), getran(11,21)))
session.set_dont_like(["naked", "nsfw"])

session.set_do_follow(True, percentage= getran(50,100))

session.set_comments(comments= COMMENTS)
session.set_do_comment(True, percentage= getran(50,80))

session.set_comment_replies(replies= COMMENT_REPLIES )
session.set_do_reply_to_comments(True, percentage= getran(90,101))

session.end()