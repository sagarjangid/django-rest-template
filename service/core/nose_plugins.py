
import logging
from nose.plugins import Plugin


class SilenceMigrations(Plugin):
    """
    Silence the logging of South DEBUG messages.
    """
    logging_level = logging.ERROR

    def configure(self, options, conf):
        super(SilenceMigrations, self).configure(options, conf)
        logging.getLogger('django.db.backends.schema')\
            .setLevel(self.logging_level)

