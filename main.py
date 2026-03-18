


from email.mime import message

from requests import post

from Post import Post

class Post1:

    Post_id = 0

choice = input("Enter your username: ")
if choice == "Jason Noble":
    print("entered username is correct")
    choice = input("Enter your password: ")
    if choice == "NobleKing26":
        print("entered password is correct")
        choice1 = input("would you like to post a message? (yes/no): ")
        if choice1 == "yes":
            print("Jason Noble: This is my first post!")
            self.post_id = self.post.post_id
            Post.post_id += 1
        else:
            print("You chose not to post a message:")
    else:
        print("entered password is incorrect")
    def __str__(self):
        return self.post.__str__()
    
    def set_message(self, message):
        self.message = message
        print("This is my first post!")
    
    def get_user_name(self):
        return self.username
    
    def get_post_id(self):
        return self.post_id
else:
    print("entered username is incorrect")