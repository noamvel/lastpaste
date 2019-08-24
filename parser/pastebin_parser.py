from paste import Paste
from lxml import html
import logging


def parse_archive(archive_text):
    # parse pastes hrefs from 'Pastes Archive'
    # filtering pastes older than 2 minutes
    # filtering 'syntax' hrefs
    archive_doc = html.document_fromstring(archive_text)
    post_time_filter = "[tr/td/text() = '1 min ago' or tr/td/text() = '2 min ago' or contains(tr/td/text(), 'sec ago')]"
    pastes_table_list = archive_doc.xpath("//table[@class='maintable']" + post_time_filter)
    if pastes_table_list:
        pastes_table = pastes_table_list[0]
    else:
        return [];
    pastes = pastes_table.xpath("tr/td/a[not(contains(@href, 'archive'))]/@href")
    logging.info('{} new pastes'.format(len(pastes)))
    return pastes


def parse_paste(paste_text):
    # parse paste meta_data & content
    title = author = content = date = None
    paste_doc = html.document_fromstring(paste_text)
    title_list = paste_doc.xpath("//div[@class='paste_box_line1']/@title")
    if title_list:
        title = title_list[0].strip()
    box_line2_element_list = paste_doc.xpath("//div[@class='paste_box_line2']")
    if box_line2_element_list:
        box_line2_element = box_line2_element_list[0]
        author_list = box_line2_element.xpath("img")
        date_list = box_line2_element.xpath("span/@title")
        if author_list:
            author = author_list[0].tail.strip()
        if date_list:
            date = date_list[0]
    paste = Paste (title, author, date, content)
    logging.info(paste)
    return paste

