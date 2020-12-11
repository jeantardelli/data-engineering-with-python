"""
pythonlog

This module illustrates a simple logging script.
"""
import logging

logging.basicConfig(level=0, filename='python-log.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
#logging.basicConfig(level=0, filename='python-log.log', filemode='w', format='%(levelname)s - %(message)s')

logging.debug('Attempted to divide by zero')
logging.warning('User left field blank in the form')
logging.error("Coudn't find specified file")


logging.info('Something happened')
logging.info('Something else happened, and it was bad')
