import datetime
import logging
import logging.config
import sys
import textwrap


# logging.config.fileConfig(fname='logging.conf')


class CustomLogHandler(logging.Handler):
    """ Logging handler that handles custom output """

    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        msg = self.format(record)
        wrapped_text = textwrap.wrap(msg, 160)
        print("{0} - {1:>21}:{2:<4} - {3:8} - {4}".format(datetime.datetime.now(), record.name, record.lineno,
                                                          record.levelname, wrapped_text[0]))
        for line in wrapped_text[1:]:
            print("                                                                    {}".format(line))


logHandler = CustomLogHandler()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logHandler)


def get_logger(name):
    return logging.getLogger(name)


stdOutLogger = get_logger('stdout')
stdErrLogger = get_logger('stderr')


# def enable_debug_output():
#    logger.setLevel(logging.DEBUG)


def _global_exception_log(exctype, value, tb):
    if issubclass(exctype, KeyboardInterrupt):
        sys.__excepthook__(exctype, value, tb)
        return
    stdErrLogger.error(
        'An unexpected exception occurred of type ' + str(exctype) + ': \n' + str(value) + "\nTraceback: " + str(
            tb.format_exc()))

# sys.excepthook = _global_exception_log
