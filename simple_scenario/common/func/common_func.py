import re

class CommonFunc(object):

    def get_curr_url(self, driver):
        url = driver.current_url
        return url


    def id_in_url(self, obj1, comp):
        pattern = re.compile(comp)
        for spec_starts in pattern.finditer(obj1):
            spec_start = spec_starts.end()
        id = obj1[int(spec_start): len(obj1)]
        return id






