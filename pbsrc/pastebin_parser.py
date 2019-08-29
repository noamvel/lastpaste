from pbsrc.paste import Paste
from lxml import html
import logging


def parse_archive(archive_text):
    doc = html.document_fromstring(archive_text)
    time_filter = "[(td/text() = '1 min ago' or contains(td/text(), 'sec ago'))]"
    trs = doc.xpath(f".//table[@class='maintable']/tr{time_filter}")
    hrefs = []
    for tr in trs:
        href = _get_element(tr, 'td[1]/a/@href')
        if href:
            hrefs.append(href)
    return hrefs


def _get_element(element, path):
    if element is None:
        return None
    try:
        return element.xpath(path)[0]
    except Exception as e:
        logging.error(f'Failed to parse {element}:{path}\n{e}\nSkipping')
        return None


def parse_paste(paste_text):
    if not paste_text:
        return None
    doc = html.document_fromstring(paste_text)
    title = _get_element(doc, ".//div[@class='paste_box_line1']/@title")
    content = _get_element(doc, "//textarea[@id='paste_code']/text()")
    box_2 = _get_element(doc, ".//div[@class='paste_box_line2']")
    author = _get_element(box_2, 'img').tail
    date = _get_element(box_2, 'span/@title')
    paste = Paste(title, author, date, content)
    return paste
