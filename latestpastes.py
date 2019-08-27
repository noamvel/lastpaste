import threading

from pbclient.pastebin_client import PastebinArchiveClient, PastebinSinglePasteClient
from pbparser.pastebin_parser import parse_archive, parse_paste
import logging
import arrow
import time
import schedule


def run_job(job):
    job_thread = threading.Thread(target=job)
    job_thread.start()


def latest_pastes():
    time_now = arrow.utcnow()
    time_sec = time_now.format('YYYY-MM-DD HH:mm:ss')
    time_min = time_now.format('YYYY-MM-DD_HH:mm')
    logging.info('\nJob {} started'.format(time_sec))
    filename = 'pbjobs/pastes_{}.txt'.format(time_min)

    archive = PastebinArchiveClient().get()
    hrefs = parse_archive(archive)
    with open(filename, 'w') as writer:
        logging.info('{} new pastes found'.format(len(hrefs)))
        logging.info('Writing new pastes to File {}'.format(filename))
        write_counter = 0
        for href in hrefs:
            paste_txt = PastebinSinglePasteClient(href).get()
            paste = parse_paste(paste_txt)
            if paste:
                writer.write(repr(paste))
                writer.write('\n')
                write_counter += 1
                print(repr(paste))
    logging.info('Job Finished, {} new pastes written.\n'.format(write_counter))


logging.basicConfig(filename='latestpastes.log', level=logging.INFO)
schedule.every(1).minutes.at(":00").do(run_job, latest_pastes)
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        logging.error("Exiting 'latestpastes'.\n{} ".format(e))
