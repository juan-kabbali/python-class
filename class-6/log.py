import re


class Log:
    def __init__(self):
        self.ip = None
        self.user = None
        self.is_email = None
        self.status = None
        self.status_verbose = None

    def parse(self, line: str):
        # print(f"parsing --> {line}")
        regex = re.compile(r"(?P<ip>\S{7,15}) (?P<session>\S{1}|\S{15}) (?P<user>\S{1,50}) \[(?P<timestamp>\S{20}) "
                           r"(?P<utc>\S{5})\] \"(?P<method>GET|POST|DELETE|PATCH|PUT) (?P<url>\S{1,4096}) "
                           r"(?P<version>\S{1,10})\" (?P<status>\d{3}) (?P<size>\d+) -")
        match = re.search(regex, line)
        self.ip = match.group("ip")
        self.user = match.group("user")
        self.status = match.group("status")

    def __str__(self):
        return f"""
        ip: {self.ip}
        user: {self.user}
        is_email: {self.is_email}
        status: {self.status}
        status_verbose: {self.status_verbose}
        """
