""" Добавление колонок, характеризующих данные """

class AddColumns(object):
    def template_method(self):
        self.allnew_columns_list()
        self.normalnew_columns_list()
        self.step_three()

    def allnew_columns_list(self):
        raise NotImplementedError()

    def normalnew_columns_list(self):
        raise NotImplementedError()
