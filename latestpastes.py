from pbclient.pastebin_client import PastebinArchiveClient, PastebinSinglePasteClient
from pbparser.pastebin_parser import parse_archive, parse_paste
import logging
import arrow
import time
import schedule


logging.basicConfig(filename='latestpastes.log', level=logging.INFO)


now = arrow.utcnow().format('YYYY-MM-DD_HH:mm')
logging.info('\nJob {} started'.format(now))
filename = 'pbjobs/{}_pastes.txt'.format(now)

archive = PastebinArchiveClient().get()
hrefs = parse_archive(archive)

with open(filename, 'w') as writer:
    logging.info('{} new pastes found'.format(len(hrefs)))
    logging.info('Writing to File {}'.format(filename))
    write_counter = 0
    for href in hrefs:
        paste_txt = PastebinSinglePasteClient(href).get()
        paste = parse_paste(paste_txt)
        if paste:
            writer.write(paste.__repr__())
            write_counter += 1
            print(paste)
logging.info('Job Finished, {} new pastes written.\n'.format(write_counter))








