from Models.Model import Model


class fishermen(Model):
    __nameTable = 'fishermen'


    def get(self):
        return super().get(self.__nameTable)
