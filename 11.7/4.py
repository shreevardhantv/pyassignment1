"""
Excercise 11.7

Question 4: You are given data on user interactions on three social media posts:
“Post1”, “Post2”, and “Post3”. Each post has a list of users who in-
teracted with it in some manner (liked, commented, or shared). Write a
program to find the following:
(a) Common Interactors: Find the users who have interacted with all
three posts.
(b) Exclusive Interactors: Find users who interacted with only one post.
(c) Most Popular Post: Determine which post has the most unique user
interactions.
(d) Post Comparison: Compare two posts to see which users interacted
with both (Post1 and Post2).

Example Input:
post1 = {'Alice': 'like', 'Bob': 'comment', 'Charlie': 'share',
'David': 'like', 'Eve': 'like'}
post2 = {'Alice': 'comment', 'Charlie': 'like', 'David': 'comment',
'Frank': 'share'}
post3 = {'Bob': 'like', 'Charlie': 'comment', 'Eve': 'share',
'Grace': 'like'}

Expected Output:
Common Interactors: Charlie
Exclusive Interactors: Eve, Frank, Grace
Most Popular Post: post1
Common users for post1 and post2: Alice, David
"""

post1 = {'Alice': 'like',
         'Bob': 'comment',
         'Charlie': 'share',
         'David': 'like',
         'Eve': 'like'
         }

post2 = {'Alice': 'comment',
         'Charlie': 'like',
         'David': 'comment',
         'Frank': 'share'}

post3 = {'Bob': 'like',
         'Charlie': 'comment',
         'Eve': 'share',
         'Grace': 'like'}

def analyze_posts(post1, post2, post3):
    post1, post2, post3 = (set(i.keys()) for i in (post1, post2, post3))
    common = (post1 & post2 & post3)
    exclusive = (post1 | post2 | post3) - ((post1 & post2) | (post1 & post3) | (post2 & post3))
    popular = {tuple(post1): "post1", tuple(post2): "post2", tuple(post3): "post3"}[tuple(max((post1, post2, post3), key=lambda x: len(x)))]
    
    common_1_2 = (post1 & post2)

    return common, exclusive, popular, common_1_2

print("Common Interactors: {}\nExclusive Interactors: {}\nMost popular post: {}\nCommon users for post1&post2: {}".format(*analyze_posts(post1, post2, post3)))


    
