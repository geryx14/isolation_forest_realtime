import sys
import logging
from colorlog import ColoredFormatter
from config import Config

def logger_init():

    formatter = ColoredFormatter(
        "%(log_color)s%(asctime)s %(levelname)-8s %(name)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
    )
    
    out_stream_handler = logging.StreamHandler(sys.stdout)
    out_stream_handler.setLevel(logging.DEBUG)
    out_stream_handler.addFilter(lambda x:x.levelno <= logging.WARNING)
    out_stream_handler.setFormatter(formatter)
    err_stream_handler = logging.StreamHandler(sys.stderr)
    err_stream_handler.setLevel(logging.ERROR)
    err_stream_handler.setFormatter(formatter)

    logging.basicConfig(
        level=Config.LOGGING_LEVEL,
        format=Config.LOGGING_FORMAT,
        handlers=[out_stream_handler,err_stream_handler]
    )
    logging.getLogger().addHandler(out_stream_handler)
    logging.getLogger().addHandler(err_stream_handler)
    logging.getLogger("httpx").setLevel(logging.ERROR)