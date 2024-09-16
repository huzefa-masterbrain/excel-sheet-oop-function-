import user
from post import post

app_user_one = user.User("nn@nn.com","nana janashia","pwd1","DevOps engineer")
app_user_one.get_user_info()

app_user_two = user.User("aa@aa.com","james bond","supersecret","Agent")
app_user_two.get_user_info()

new_post = post("on a secret mission today",app_user_two.name)
new_post.get_post_info()