import arrow


class Paste:

    __date_formatter = 'dddd Do [of] MMMM YYYY h:mm:ss A ZZ'
    __normalized_author = ('a guest', 'Guest', 'Unknown', 'Anonymous')
    __normalized_title = ('Unknown', 'Untitled')

    def __init__(self, title='', author='', date='', content=''):
        self.author = self.__normalize(author, Paste.__normalized_author);
        self.title = self.__normalize(title, Paste.__normalized_title);
        self.content = self.__normalize(content, []);
        self.date = self.__format_date(date)

    @staticmethod
    def __normalize(val, normalized_val):
        if val is None:
            return ''
        striped_val = val.strip()
        if striped_val in normalized_val:
            return ''
        return striped_val

    @staticmethod
    def __format_date(date):
        if date is None:
            return ''
        if 'CDT' in date:
            utc_date = date.replace('CDT', '-05:00')
        elif 'CST' in date:
            utc_date = date.replace('CST', '-06:00')
        else:
            return date
        time = arrow.get(utc_date, Paste.__date_formatter).to('utc')
        return time

    def __repr__(self):
        return f"{{'Title': '{self.title}', 'Author': '{self.author}', 'Date': '{self.date}', 'Content': '{self.content}'}}"

    def as_dict(self):
        return {'Title': f'{self.title}', 'Author': f'{self.author}', 'Date': f'{self.date}', 'Content': f'{self.content}'}



