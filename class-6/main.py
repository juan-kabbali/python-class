from log import Log
from transformations import UserTransformation, StatusCodeTransformation

with open("assets/web-server-nginx.log") as file:
    for line in file:
        log = Log()
        log.parse(line)
        log = StatusCodeTransformation().transform(log)
        log = UserTransformation().transform(log)
        print(log)
