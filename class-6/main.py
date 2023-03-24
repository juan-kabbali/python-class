from log import Log
from transformations import UserTransformation, StatusCodeTransformation

with open("assets/web-server-nginx.log") as file:
    for line in file:
        log = Log()
        log.parse(line)
        log = StatusCodeTransformation().transform(log)
        print(f"{log.status} {log.status_verbose}")
