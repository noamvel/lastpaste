import threading
import logging
import arrow
import time
import schedule
from tinydb import TinyDB
from src.pastebin_client import PastebinArchiveClient, PastebinSinglePasteClient
from src.pastebin_parser import parse_archive, parse_paste


def run_job(job, db_storage):
    time_min = arrow.utcnow().format('YYYY-MM-DD_HH:mm')
    file_storage = f'jobs/pastes_{time_min}.txt'
    storage = [{'storage': f'{file_storage}', 'writer': file_storage_writer},
                {'storage': db_storage, 'writer': db_storage_writer}]
    job_thread = threading.Thread(target=job(storage))
    job_thread.start()


def latest_pastes_job(storage):
    try:
        pastes = get_latest_pastes()
        for s in storage:
            s['writer'](s['storage'], pastes)
            logging.info(f"{len(pastes)} new pastes written to {s['storage']}")
    except Exception as e:
        logging.error(f'Exiting current job ...\n{e}')
    return


def file_storage_writer(storage, pastes):
    with open(storage, 'w') as writer:
        for paste in pastes:
            writer.write(str(paste))
            writer.write('\n')


def db_storage_writer(storage, pastes):
    lines = [p.as_dict() for p in pastes]
    storage.insert_multiple(lines)


def get_latest_pastes():
    archive = PastebinArchiveClient().get()
    hrefs = parse_archive(archive)
    pastes = []
    for href in hrefs:
        paste_txt = PastebinSinglePasteClient(href).get()
        paste = parse_paste(paste_txt)
        if paste:
            pastes.append(paste)
    return pastes


logging.basicConfig(
        filename='latestpastes.log', format='%(asctime)s %(levelname)-5s %(message)s',
        level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
logging.info("Latest pastes started ...")
db = TinyDB('db.json', default_table='pastes')
table = db.table('pastes')
schedule.every(2).minutes.at(':00').do(run_job, latest_pastes_job, table)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        logging.error(f'Exiting latestpaste.{e}')
