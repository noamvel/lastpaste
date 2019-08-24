from paste import Paste
from lxml import html
import logging


def parse_archive(archive_text):
    # parse pastes hrefs from 'Pastes Archive'
    # filtering pastes older than 2 minutes
    # filtering 'syntax' hrefs
    archive_doc = html.document_fromstring(archive_text)
    post_time_filter = "[(td/text() = '1 min ago' or td/text() = '2 min ago' or contains(td/text(), 'sec ago'))]"
    filtered_tr_list = archive_doc.xpath("//table[@class='maintable']/tr{}".format(post_time_filter))
    if not filtered_tr_list:
        return [];
    hrefs = []
    for e in filtered_tr_list:
        href = e.xpath("td/a[not(contains(@href, 'archive'))]/@href")
        if href:
            hrefs.append(href[0])
    logging.info('{} new pastes'.format(len(hrefs)))
    return hrefs


def parse_paste(paste_text):
    # parse paste meta_data & content
    title = author = content = date = None
    paste_doc = html.document_fromstring(paste_text)
    if not paste_doc:
        return None
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
    # textarea id="paste_code"
    content = paste_doc.xpath("//textarea[@id='paste_code']/text()")[0].strip()
    paste = Paste (title, author, date, content)
    return paste

