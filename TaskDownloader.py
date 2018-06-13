from urllib2 import urlopen, URLError
from json import loads
from TaskTable import instantiate_table


class Task(object):

    def __init__(self, window, url):
        self.window = window
        self.url = url

    def get_all(self):
        tasks = urlopen(self.url).read()

        return loads(tasks)
    
    def get_data_from_internet(self):
        try:
            task_list = self.get_all()
            instantiate_table(self.window, task_list)
        except URLError:
            print("Failed to load the given URL")
