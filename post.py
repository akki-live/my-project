class Post:
    def __init__(self, message, author):
        self.message = message
        self.auther = author

    def get_post_info(self):
        print(f"Post: {self.message} written by {self.auther}")

    
        
