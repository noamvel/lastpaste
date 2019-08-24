import arrow
from client.pastebin_client import PastebinArchiveClient, PastebinSinglePasteClient
from parser.pastebin_parser import parse_archive, parse_paste
import logging

logging.basicConfig(filename='latestpastes.log', level=logging.INFO)
logging.info('Started')

time = arrow.utcnow().format('YYYY-MM-DD_HH:mm')
filename = '{}_pastes.txt'.format(time)
file = open(filename, "a")

archive_txt = PastebinArchiveClient().get()
pastes_hrefs = parse_archive(archive_txt)

for href in pastes_hrefs:
    paste_txt = PastebinSinglePasteClient(href).get()
    paste = parse_paste(paste_txt)
    file.write(paste.__repr__())
file.close()
logging.info('Finished')








