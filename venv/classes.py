import requests
class Website:
    websites = []

    def __init__(self, name, id, url):
        """

        :param name:
        :param id_w:
        :param url:
        """
        self.name = name
        self.id = id
        self.endpoints = []
        self.add_endpoint(url)
        self.total_websites(self.name)

    def total_websites(self, name):
        """

        :param name:
        :return:
        """
        self.websites.append(self)

    def add_endpoint(self, url):
        """

        :param url:
        :return:
        """
        self.endpoints.append(url)

    def delete(self):
        """

        :return:
        """
        self.websites.remove(self.name)
        del self
        try:
            print(self)
            print("Ainda existe")
        except:
            print("Objecto apagado")

    def check_endpoint(self):
        response = requests.get(self.endpoints)
        response.status_code(self.endpoints)
        if response.status_code == 200:
            print('Success!')
        elif response.status_code == 404:
            print('Not Found.')
