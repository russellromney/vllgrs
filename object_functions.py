"""
contains functions for dealing with operations on vllgrs
"""
import shortuuid
from objects import *

# deal with posts: blog (10,000 words) and textlet (limited to 250 characters)
def return_post(post_id = "",
                post_type = "",
                post_emoji = "", 
                content = "",
                len_char = 0,
                len_word = 0,
                post_user = "",
                post_campfire = "",
                comments = [],
                upvotes = [],
                privacy = "vllg",
                post_date,
                edited = False,
                edited_dates = [],
                edited_history = [], 
                has_picture = True,
                pictures = [], # picture_ids
                is_subpost = False,
                has_subpost = False,
                subpost = "",
                subpost_of = []):
    if not post_type_ in ["textlet","text","blog","picture"]:
        raise Exception("return_post error: incorrect type")
    word_len=len(post_.strip().split())
    char_len=len(post_.strip())
    if type_=="textlet" and char_len > 200:
        raise Exception("return_post error: textlet is over 200 characters")
    if type_=="text" and word_len > 250:
        raise Exception("return_post error: text is over 250 words")
    if type_=="blog" and len(post_.strip().split()) > 5,000:
        raise Exception("return_post error: blog is over 5,000 words")
    this_post = post_dict
    for key in this_post.keys():
        this_post[key] = 
    return dict(
        post_id = shortuuid.uuid()
        post_type = type_,
        content = post_,
        len_char = char_len,
        len_word = word_len,
        user = user_,
        comments = [],
        upvotes = [],
        privacy = "vllg"
        post_date = datetime.today()),
        post_emoji = post_emoji_,
        edited = False
        edited_dates = []
    )

# submit a post to posts
def store_post(post_,db_):
    db_.posts.insert_one(post_)