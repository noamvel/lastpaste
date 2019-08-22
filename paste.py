class Paste:

    def __init__(self, author, title, content, time):
        self.author = author
        self.title = title
        self.content = content
        self.date = time.format('YYYY-MM-DD_HH:mm')

    def __repr__(self):
        return "Title: {}\nAuthor: {}\nDate:{}\nContent:{}".format(self.title, self.author, self.date, self.content)
