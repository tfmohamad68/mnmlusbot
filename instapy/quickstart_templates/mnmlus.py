from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
from instapy import get_workspace
import schedule
import time
from time import clock

# get a session!
insta_username='mnmlus_'
insta_password='hg1dc91h'
set_workspace(path="/Users/tarek/Desktop/mnmlusbot/Path")
competitors = ['sophia_beirut','maatjewelry','sueno.lb','earpartybeirut','mukhisisters','lebelik_com','sarahsbag','bothemians']
users_p = 20

def get_session():
  session = InstaPy(username=insta_username, password=insta_password, headless_browser=False, bypass_suspicious_attempt=True)
  return session
def interact_with_users():
  session = get_session()

  with smart_run(session):
    workspace_in_use = get_workspace()
    print(workspace_in_use["path"])
    session.set_mandatory_language(enabled=True, character_set=['LATIN'])
    session.set_relationship_bounds(enabled=True,
                                    max_followers=5000,
                                    max_following=1200,
                                    min_followers=30,
                                    min_following=30,
                                    min_posts=3)
    session.set_action_delays(enabled=True,
                              like=3,
                              comment=5,
                              follow=4.17,
                              randomize=True,
                              random_range=(70,200))
    session.set_skip_users(skip_private=False,
                          skip_business=True,
                          business_percentage=100,
                          skip_no_profile_pic=True,
                          no_profile_pic_percentage=100)
    session.set_user_interact(amount=3, randomize=False, percentage=100, media='Photo')
    session.set_do_like(enabled=True, percentage=100)
    session.set_comments(['Nice shot! @{}',
                                  'We love your profile! @{}',
                                  'Wonderful :thumbsup:',
                                  'Just incredible :open_mouth:',
                                  'Love your posts @{}',
                                  'Looks awesome @{}',
                                  'Getting inspired by you @{}',
                                  ':raised_hands: Yes!',
                                  'We can feel your passion @{} :muscle:'])
    session.set_do_comment(enabled=True, percentage=30)
    session.set_do_follow(enabled=True, percentage=100, times=1)
    session.follow_likers(competitors, photos_grab_amount = 6, follow_likers_per_photo = 10, randomize=False, sleep_delay=600, interact=True)
    session.end
def follow_users_f():
  session = get_session()

  with smart_run(session):
    session.set_mandatory_language(enabled=True, character_set=['LATIN'])
    session.set_skip_users(skip_private=False,
                          skip_business=True,
                          business_percentage=100,
                          skip_no_profile_pic=True,
                          no_profile_pic_percentage=100)
    session.set_action_delays(enabled=True,
                              like=3,
                              comment=5,
                              follow=4.17,
                              randomize=True,
                              random_range=(70,200))
    session.set_relationship_bounds(enabled=True,
                                    max_followers=5000,
                                    max_following=1200,
                                    min_followers=100,
                                    min_following=100,
                                    min_posts=3)
    session.set_user_interact(amount=3,percentage=100,randomize=True,media='Photo')
    session.follow_commenters(competitors, amount=users_p, daysold=365, max_pic = 6, sleep_delay=600, interact=True)
    session.end
def unfollow_all():
  session = get_session()

  with smart_run(session):
    session.set_action_delays(enabled=True,
                              unfollow=15,
                              randomize=True,
                              random_range=(70,200))
    session.set_dont_unfollow_active_users(enabled=True, posts=5)
    session.unfollow_users(amount=40, nonFollowers=True, style="RANDOM", unfollow_after=48*60*60, sleep_delay=655)
    session.end
def feed_bylike():
  session = get_session()
  with smart_run(session):
    session.set_mandatory_language(enabled=True, character_set=['LATIN'])
    session.like_by_feed(amount=20, randomize=False, unfollow=True, interact=False)
    session.end

schedule.every().day.at("03:00:00").do(unfollow_all)
schedule.every().day.at("08:45:00").do(feed_bylike)
schedule.every().day.at("09:00:00").do(interact_with_users)
schedule.every().day.at("09:00:00").do(follow_users_f)
schedule.every().day.at("11:00:00").do(feed_bylike)
schedule.every().day.at("11:40:00").do(unfollow_all)
schedule.every().day.at("11:59:00").do(follow_users_f)
schedule.every().day.at("11:59:00").do(interact_with_users)
schedule.every().day.at("13:00:00").do(feed_bylike)
schedule.every().day.at("15:00:00").do(unfollow_all)
schedule.every().day.at("15:30:00").do(follow_users_f)
schedule.every().day.at("16:00:00").do(interact_with_users)
schedule.every().day.at("18:40:00").do(unfollow_all)
schedule.every().day.at("19:00:00").do(interact_with_users)
schedule.every().day.at("20:00:00").do(feed_bylike)
schedule.every().day.at("23:40:00").do(unfollow_all)


while True:
  schedule.run_pending()
  time.sleep(10)

