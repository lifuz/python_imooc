# coding:utf8
class UrlManager(object):

    __newUrl = set([])
    __oldUrl = set([])

    def add_new_url(self, url):

        if url is None:
            return
        if url not in UrlManager.__oldUrl:
            UrlManager.__newUrl.add(url)

    def has_new_url(self):
        if len(UrlManager.__newUrl) > 0 :
            return True
        return False

    def get_new_url(self):
        url = UrlManager.__newUrl.pop()
        UrlManager.__oldUrl.add(url)

        return url

    def add_new_urls(self, urls):

        if urls is None or len(urls) ==0:
            return

        for url in urls:
            self.add_new_url(url)