import logging
import modulesa.modulea as ma
import modulesb.moduleb as mb
import log


def main():
    log.setup_custom_logger()
    logging.info('Started')
    ma.do_something()
    mb.do_something()
    logging.info('Finished')


if __name__ == '__main__':
    main()
