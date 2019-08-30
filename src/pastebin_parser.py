from src.paste import Paste
from lxml import html
import logging


def parse_archive(archive_text):
    doc = html.document_fromstring(archive_text)
    time_filter = "[(td/text() = '1 min ago' or contains(td/text(), 'sec ago'))]"
    trs = doc.xpath(f".//table[@class='maintable']/tr{time_filter}")
    hrefs = []
    for tr in trs:
        try:
            href = _get_element(tr, 'td[1]/a/@href')
            hrefs.append(href)
        except Exception as e:
            logging.error('Failed to parse href. Skipping ..')
    return hrefs


def _get_element(element, path):
    try:
        return element.xpath(path)[0]
    except Exception as e:
        logging.error(f'Failed to parse {element}:{path}\n{e}')
        raise


def parse_paste(paste_text):
    try:
        doc = html.document_fromstring(paste_text)
        title = _get_element(doc, ".//div[@class='paste_box_line1']/@title")
        content = _get_element(doc, "//textarea[@id='paste_code']/text()")
        box_2 = _get_element(doc, ".//div[@class='paste_box_line2']")
        author = _get_element(box_2, 'img').tail
        date = _get_element(box_2, 'span/@title')
        paste = Paste(title, author, date, content)
        return paste
    except Exception as e:
        logging.error('Failed to parse paste. Skipping ..')
        return None
