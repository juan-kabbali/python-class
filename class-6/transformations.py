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
        if domain := self.get_domain_from_email(log.user):
            log.is_email = True
            log.domain = domain
        return log

    def get_domain_from_email(self, user: str) -> str | None:
        regex = re.compile(r"\S+@(?P<domain>\S+\.\S+)")
        if match := re.search(regex, user):
            return match.group("domain")
        return None


class StatusCodeTransformation(BaseTransformation):

    def transform(self, log: Log) -> Log:
        log.status_verbose = http.HTTPStatus(int(log.status)).phrase
        return log


class DateTransformation(BaseTransformation):

    def transform(self, log: Log) -> Log:
        return log
