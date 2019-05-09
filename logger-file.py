import logging
import time

logging.basicConfig(filename='/var/log/org/org.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
i = 1
while i < 10000000:
    logging.warning('This will get logged to a file')
    time.sleep(5)
    if i == 1000000:
        break
    i += 1

logging.warning('This will get logged to a file')
