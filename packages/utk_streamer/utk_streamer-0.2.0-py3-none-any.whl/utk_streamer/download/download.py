import requests
import os


class StreamerDownload:
    def __init__(self, path, download_path):
        self.path = path
        self.download_path = download_path
        self.__make_download_path()

    def __make_download_path(self):
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)
        return

    def download(self):
        r = requests.get(self.path)
        filename = f"{self.path.split('/')[-2]}_{self.path.split('/')[-1]}"
        with open(f"{self.download_path}/{filename}", 'wb') as f:
            f.write(r.content)
        return