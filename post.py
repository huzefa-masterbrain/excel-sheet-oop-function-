# post.py
class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author

    def get_post_info(self):
        print("Content:", self.content)
        print("Author:", self.author)
