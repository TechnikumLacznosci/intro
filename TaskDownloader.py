from urllib2 import urlopen
from json import loads


class Task(object):

    def __init__(self, url):
        self.url = url

    def get_all(self):
        tasks = urlopen(self.url).read()

        return loads(tasks)