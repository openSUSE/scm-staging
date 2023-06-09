import logging

# logging for tornado access
from tornado.log import access_log

# logging for tornado application
from tornado.log import app_log

# logging for tornado general
from tornado.log import gen_log

# formatter for tornado
from tornado.log import LogFormatter


LOGGER = logging.getLogger(__name__)


def make_logger(
    root_log_file=None,
    access_log_file=None,
    app_log_file=None,
    general_log_file=None,
):
    """all log going to standard if not define file for it."""

    root_format = "%(color)s[%(asctime)s::%(name)s %(levelname)s] %(filename)s:\
            %(lineno)d in %(funcName)s %(end_color)s\n %(message)s\n"
    datetime_format = "%Y-%m-%d %H:%M:%S"
    LOGGER.root_formatter = LogFormatter(
        fmt=root_format, datefmt=datetime_format, color=True
    )
    LOGGER.access = access_log
    LOGGER.app = app_log
    LOGGER.general = gen_log
    # the following lines need to be called after options.parse_command_line or else empty
    if access_log_file:
        handler = logging.FileHandler(access_log_file)
        handler.setFormatter(LOGGER.root_formatter)
        LOGGER.access.addHandle(handler)

    if app_log_file:
        handler = logging.FileHandler(app_log_file)
        handler.setFormatter(LOGGER.root_formatter)
        LOGGER.app.addHandle(handler)

    if general_log_file:
        handler = logging.FileHandler(general_log_file)
        handler.setFormatter(LOGGER.root_formatter)
        LOGGER.general.addHandle(handler)

    if root_log_file:
        handler = logging.FileHandler(root_log_file)
        handler.setFormatter(LOGGER.root_formatter)
        LOGGER.root.addHandle(handler)
    else:
        LOGGER.root.handlers[0].setFormatter(LOGGER.root_formatter)


LOGGER.make_logger = make_logger
