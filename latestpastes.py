import arrow
from pb_client.pastebin_client import PastebinArchiveClient, PastebinSinglePasteClient
from pb_parser.pastebin_parser import parse_archive, parse_paste
import logging

logging.basicConfig(filename='latestpastes.log', level=logging.INFO)
time = arrow.utcnow().format('YYYY-MM-DD_HH:mm')
logging.info('\nJob {} started'.format(time))
filename = 'pb_jobs/{}_pastes.txt'.format(time)
file = open(filename, "a")

archive = PastebinArchiveClient().get()
hrefs = parse_archive(archive)
logging.info('Writing to File {}'.format(file.name))
for href in hrefs:
    paste_txt = PastebinSinglePasteClient(href).get()
    paste = parse_paste(paste_txt)
    print(paste)
    file.write(paste.__repr__())
file.close()
logging.info('Finished\n')








