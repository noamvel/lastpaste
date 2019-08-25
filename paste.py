import arrow


class Paste:

    __date_formatter = 'dddd Do [of] MMMM YYYY h:mm:ss A ZZ'
    __normalized_author = ('a guest', 'Guest', 'Unknown', 'Anonymous', None)
    __normalized_title = ('Unknown', 'Untitled', None)

    def __init__(self, title, author, date, content):
        self.author = self.__normalized(author, Paste.__normalized_author);
        self.title = self.__normalized(title, Paste.__normalized_title);
        self.content = content
        self.date = self.__format_date(date)

    @staticmethod
    def __normalized(val, normalized_val):
        if val in normalized_val:
            return ""
        return val

    @staticmethod
    def __format_date(date):
        if 'CDT' in date:
            utc_date = date.replace('CDT', '-05:00')
        if 'CST' in date:
            utc_date = date.replace('CDT', '-06:00')
        time = arrow.get(utc_date, Paste.__date_formatter)
        return time

    def __repr__(self):
        return "Title: {}\nAuthor: {}\nDate: {}\nContent:\n{}\n\n".format(self.title, self.author, self.date, self.content)
