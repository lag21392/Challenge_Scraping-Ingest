import logging
from os import path, makedirs
class Logger:
    @staticmethod
    def create_logger(name):
        log_folder = 'Logs'
        log_file = name + '.log'
        log_path = path.join(log_folder,log_file)

        # Config logger
        logger = logging.getLogger(name)
        
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')        
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # Crea carpeta de log si no existe
        if not path.exists(log_folder):
            makedirs(log_folder)
        if log_path:
            fh = logging.FileHandler(log_path)
            fh.setLevel(logging.INFO)

            # Configura formato de log
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            logger.addHandler(fh)


        ch.setFormatter(formatter)
        logger.addHandler(ch)

        return logger


