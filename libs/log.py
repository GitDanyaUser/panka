import os
from uuid import uuid4
import logging
from datetime import datetime

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

def logit(mseg: str, level: str):
    log_uuid = uuid4()
    log_time = datetime.now().strftime('%d%m%Y')
    log_name = os.path.join(log_dir, f'{log_uuid}_{log_time}.log')
    logging.basicConfig(
        filename=log_name,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s %(message)s',
    )
    log_method = getattr(logging, level.lower(), logging.info)
    log_method(mseg)
