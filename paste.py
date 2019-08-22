class Paste:

    def __init__(self, title, author, date, content):
        self.author = author
        self.title = title
        self.content = content
        self.date = date
        # self.date = time.format('YYYY-MM-DD_HH:mm')  should convert to UTC
        # defaults values - take care

    def __repr__(self):
        return "Title: {}\nAuthor: {}\nDate: {}\nContent: {}\n\n".format(self.title, self.author, self.date, self.content)
