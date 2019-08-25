class Paste:

    __normalized_author = ('a guest', 'Guest', 'Unknown', 'Anonymous', None)
    __normalized_title = ('Unknown', 'Untitled', None)

    def __init__(self, title, author, date, content):
        self.author = self.__normalized(author, Paste.__normalized_author);
        self.title = self.__normalized(title, Paste.__normalized_title);
        self.content = content
        self.date = date
        # self.date = time.format('YYYY-MM-DD_HH:mm')  should convert to UTC

    @staticmethod
    def __normalized(val, normalized_val):
        if val in normalized_val:
            return ""
        return val

    def __repr__(self):
        return "Title: {}\nAuthor: {}\nDate: {}\nContent:\n{}\n\n".format(self.title, self.author, self.date, self.content)
