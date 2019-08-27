import threading
from pbclient.pastebin_client import PastebinArchiveClient, PastebinSinglePasteClient
from pbparser.pastebin_parser import parse_archive, parse_paste
import logging
import arrow
import time
import schedule
from tinydb import TinyDB


def run_job(job, db_table):
    job_thread = threading.Thread(target=job(db_table))
    job_thread.start()


def latest_pastes(db_table):
    time_now = arrow.utcnow()
    time_sec = time_now.format('YYYY-MM-DD HH:mm:ss')
    time_min = time_now.format('YYYY-MM-DD_HH:mm')
    logging.info('\nJob {} started'.format(time_sec))
    filename = 'jobs/pastes_{}.txt'.format(time_min)

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
                db_table.insert(repr(paste))
                write_counter += 1
    logging.info('Job Finished, {} new pastes written.\n'.format(write_counter))


# initiation - logger, db, schedule jobs
logging.basicConfig(filename='latestpastes.log', level=logging.INFO)
db = TinyDB('db.json', default_table='pastes')
table = db.table('pastes')
schedule.every(2).minutes.at(':00').do(run_job, latest_pastes, table)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        logging.error("Exiting 'latestpastes'.\n{} ".format(e))
