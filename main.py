from Post import Post


posts_archive = []
posts_archive.append( Post("John", "Hello World!"))
posts_archive.append( Post("Bob", "Hello World!"))
posts_archive.append( Post("Alice", "Hello World!"))

# for p in posts_archive:
#     print(p)


username = input("Enter your username: ")
print("Welcome, " + username + "!")
user_input = input("Please choose an action: new, remove, change user, print, quit")
while (user_input != "quit"):
    if user_input == "new":
        # ask the user for the content of the post and post it
        content = input("Enter the content of your post: ")
        new_post = Post(username, content)
        posts_archive.append(new_post)
    elif user_input == "remove":
        pass # TODO: handle the requrested action
    elif user_input == "change user":
        pass # TODO: handle the requrested action
    elif user_input == "print":
        pass # TODO: handle the requrested action
    user_input = input("Please choose an action: new, remove, change user, print, quit")
print("goodbye")

  # what will happen if the user doesn't enter quit
  # Notice this is tabbed over. This represents the body of
  # the while loop.
  