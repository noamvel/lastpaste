import arrow
from pbclient.pastebin_client import PastebinArchiveClient, PastebinSinglePasteClient
from pbparser.pastebin_parser import parse_archive, parse_paste
import logging

logging.basicConfig(filename='latestpastes.log', level=logging.INFO)
time = arrow.utcnow().format('YYYY-MM-DD_HH:mm')
logging.info('\nJob {} started'.format(time))
filename = 'pbjobs/{}_pastes.txt'.format(time)

archive = PastebinArchiveClient().get()
hrefs = parse_archive(archive)

with open(filename, 'w+') as writer:
    logging.info('Writing to File {}'.format(filename))
    for href in hrefs:
        paste_txt = PastebinSinglePasteClient(href).get()
        paste = parse_paste(paste_txt)
        print(paste)
        writer.write(paste.__repr__())
logging.info('Job Finished Successfully\n')








