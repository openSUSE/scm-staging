import logging
from typing import cast

# logging for tornado access
from tornado.log import access_log

# logging for tornado application
from tornado.log import app_log

# logging for tornado general
from tornado.log import gen_log

# formatter for tornado
from tornado.log import LogFormatter


class AppLogger(logging.Logger):
    def configure_log_files(
        self,
        root_log_file: str | None = None,
        access_log_file: str | None = None,
        app_log_file: str | None = None,
        general_log_file: str | None = None,
    ) -> None:
        root_format = "%(color)s[%(asctime)s::%(name)s %(levelname)s] %(filename)s:\
                %(lineno)d in %(funcName)s %(end_color)s\n %(message)s\n"
        datetime_format = "%Y-%m-%d %H:%M:%S"
        self.root_formatter = LogFormatter(
            fmt=root_format, datefmt=datetime_format, color=True
        )
        self.access = access_log
        self.app = app_log
        self.general = gen_log

        # the following lines need to be called after options.parse_command_line or else empty
        if access_log_file:
            handler = logging.FileHandler(access_log_file)
            handler.setFormatter(self.root_formatter)
            self.access.addHandler(handler)

        if app_log_file:
            handler = logging.FileHandler(app_log_file)
            handler.setFormatter(self.root_formatter)
            self.app.addHandler(handler)

        if general_log_file:
            handler = logging.FileHandler(general_log_file)
            handler.setFormatter(self.root_formatter)
            self.general.addHandler(handler)

        if root_log_file:
            handler = logging.FileHandler(root_log_file)
            handler.setFormatter(self.root_formatter)
            self.root.addHandler(handler)
        else:
            if not self.root.handlers:
                self.root.addHandler(logging.StreamHandler())
            self.root.handlers[0].setFormatter(self.root_formatter)


logging.setLoggerClass(AppLogger)
LOGGER: AppLogger = cast(AppLogger, logging.getLogger(__name__))
LOGGER.setLevel(logging.DEBUG)
