import logging
# import logging.config
import os
from datetime import datetime


def create_logger():
    
    path_dir_log = os.path.join(os.path.dirname(__file__), 'logs')

    if not os.path.exists(path_dir_log):
        os.mkdir(path_dir_log)

    now = datetime.now()
    file_log = os.path.join(path_dir_log, F'logs_{now.year}{now.month}{now.day}.log')
    logging.basicConfig(filename=file_log,
                        encoding='utf-8',
                        level=logging.DEBUG,
                        format='%(asctime)s %(name)s %(levelname)s %(message)s')
    # logging.config.fileConfig('logger.conf')

logger = logging.getLogger('PropuskLogger')