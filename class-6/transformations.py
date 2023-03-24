import http
import re
from abc import abstractmethod
from email.utils import parseaddr
from log import Log


class BaseTransformation:

    @abstractmethod
    def transform(self, log: Log) -> Log:
        raise NotImplementedError


class UserTransformation(BaseTransformation):

    def transform(self, log: Log) -> Log:
        log.is_email = self.is_email(log.user)
        return log

    def is_email(self, user: str) -> bool:
        regex = re.compile(r"\S+@\S+\.\S+")
        if re.search(regex, user):
            return True
        return False


class StatusCodeTransformation(BaseTransformation):

    def transform(self, log: Log) -> Log:
        log.status_verbose = http.HTTPStatus(int(log.status)).phrase
        return log

