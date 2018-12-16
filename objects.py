"""
Basic data structure plans for all relevant vllgrs objects
"""

import datetime


post_dict = dict(
        post_id = "",
        post_type = "", # textlet, text, blog, picture (picture is an extension of text?)
        post_emoji = "", # any individual emoji
        content = "",
        len_char = 0,
        len_word = 0,
        post_user = "",
        post_campfire = "", # campfire id
        comments = [],
        upvotes = [],
        privacy = "vllg", # campfire, vlly, hut
        post_date = datetime.today(),
        edited = False,
        edited_dates = [],
        edited_history = [], # list of old content
        has_picture = True,
        pictures = [], # picture_ids
        is_subpost = False,
        has_subpost = False,
        subpost = "", # the subpost's post_id
        subpost_of = [], # tracks where it has been shared
)

user_dict = dict(
    user_id = "",
    name = dict(first="",middle="",last=""),
    email = "",
    password = "",
    birthday = "",
    phone = "",
    contact_email = "",
    connections = [], # user_ids
    following = [], # user_ids
    followers = [], # user_ids
    campfires = [],
    viewed = dict(), # supposed to track what you've seen and when, etc. Don't know how to implement this right now to serve only new content
    active_interactions = [], # tracks all posts you've interacted with in some way
    inactive_interactions = [], # tracks all posts with which you've interacted but on which you don't want to see updates anymore
    posts = [],
    comments = [], # comment IDs
    upvotes = [], # user_ids who have upvoted
    user_picture = "", # picture_id
    user_picture_small = [], # picture_ids
    user_picture_all = [], # picture_ids
    settings = dict(
        defaults = dict(
            textlet_privacy = "vlly", # hut, vllg
            text_privacy = 'vllg', # hut, vllg
            blog_privacy = "vllg", # hut, vlly
            picture_privacy = "vllg", # hut, vlly
            comments = "parent post default", # hut, vllg, vlly 
            upvotes = "parent post default", # hut, vllg, vlly
            profile_privacy = 'vlly', # vllg
        ),
    ),

)

comment_dict = dict(
    comment_id = "", #
    post = "", # all its privacy, etc. are copied from its parent post
    upvotes = [], # user_ids who have upvoted
    content = "", 

)

campfire_dict = dict(
    campfire_id = "",
    name = "",
    name_history = [], # list of old names,
    users = [], # user_ids
    can_post = "all", # 'post_users'
    post_users = [], # user_ids
    can_comment = "all", # post_users, comment_users
    comment_users = [],
    can_upvote = 'all', # post_users, comment_users
    view_privacy = "public", # "private"
    can_lead = 'leaders', # "all" # allows changing campfire settings and adding managers, and all leader abilities
    leaders = [], # if post_users or all, this is set to
    can_manage = 'managers',
    managers = [], # allows deleting posts, comments, etc. # when a leader is set, they are also added to managers
)

picture_dict = dict(
    picture_id = "",
    tags = [],
    caption = "",
    privacy = "vllg", # vlly, hut, campfire
    
)