import requests
import arrow
from lxml import html
from paste import Paste

pb_home_url = 'https://pastebin.com'
pb_archive_url = pb_home_url + '/archive'
# logger ?


def get_document(url):
    # http call to get source page for given url and return it's document.
    response = requests.get(url)
    # check response.status_code? , Exceptions?
    document = html.document_fromstring(response.content)
    return document


def parse_pastes_hrefs(archive_document):
    # parse pastes hrefs from 'Pastes Archive'
    # filtering pastes older than 2 minutes
    # filtering 'syntax' hrefs
    post_time_filter = "[tr/td/text() = '1 min ago' or tr/td/text() = '2 min ago' or contains(tr/td/text(), 'sec ago')]"
    pastes_table_list = archive_document.xpath("//table[@class='maintable']" + post_time_filter)
    if pastes_table_list:
        pastes_table = pastes_table_list[0]
    else:
        return [];
    pastes = pastes_table.xpath("tr/td/a[not(contains(@href, 'archive'))]/@href")
    print('{} new pastes'.format(len(pastes)))
    return pastes


def parse_paste(paste_document):
    # parse paste meta_data & content
    title = author = content = date = None
    title_list = paste_document.xpath("//div[@class='paste_box_line1']/@title")
    if title_list:
        title = title_list[0].strip()
    box_line2_element_list = paste_document.xpath("//div[@class='paste_box_line2']")
    if box_line2_element_list:
        box_line2_element = box_line2_element_list[0]
        author_list = box_line2_element.xpath("img")
        date_list = box_line2_element.xpath("span/@title")
        if author_list:
            author = author_list[0].tail.strip()
        if date_list:
            date = date_list[0]
    return Paste (title, author, date, content)


time = arrow.utcnow().format('YYYY-MM-DD_HH:mm')
filename = '{}_pastes.txt'.format(time)
file = open(filename, "a")

doc = get_document(pb_archive_url)
pastes_hrefs = parse_pastes_hrefs(doc)

for href in pastes_hrefs:
    paste_url = pb_home_url + href
    print(paste_url)
    paste_doc = get_document(paste_url)
    # async?
    paste = parse_paste(paste_doc)
    print(paste)
    file.write(paste.__repr__())
file.close()








