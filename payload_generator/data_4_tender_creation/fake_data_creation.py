from faker import Faker


fake = Faker("ru_RU")


class TenderDataFactory:

    @staticmethod
    def factory(type_of_tender):

        if type_of_tender == 'below_TreshouldUA':
            return Doporog()

        if type_of_tender == 'above_TreshouldUA':
            return OpenUA()

        assert 0, 'Bad type detected: ' + type_of_tender


class Doporog(TenderDataFactory):

    def tender_data(self):
        print('DOPOROG DATA')


class OpenUA(TenderDataFactory):

    def tender_data(self):
        print('OpenUA')


obj = TenderDataFactory.factory('below_TreshouldUA')
obj.tender_data()

