from user import User
from post import Post



user1 = User("akki.com", "akki", "passwd", "DevOps engineer")
user2 = User("abc.com", 'akhil', 'xyz', "Developer")

user1.get_user_info()
user2.get_user_info()

user1.change_job_title("Sr.DevOps engineer")
user2.change_job_title("Sr. Developer")
print("==================================================")

user1.get_user_info()
user2.get_user_info()

new_post = Post("On a secret mission today", "James bond")
new_post.get_post_info()

new_post1 = Post("my name is : ", user1.name)
new_post1.get_post_info()