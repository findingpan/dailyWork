import logging
#CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET

# day = datetime.datetime.now().strftime('%Y%m%d')

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%d %b %Y %H:%M:%S',
                filename='e:/sendToYang_log.log',
                filemode='a+')
    
logging.debug('This is debug message \n')
logging.info('This is info message \n')
logging.warning('This is warning message \n')