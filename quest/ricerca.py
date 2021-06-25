from .models import Previsione, CandidatoResidenza, Linguaconosciuta

class RicercaCandidato:
    def __init__(self,params):
        self.params = params
        self.objects = Previsione.objects.all()

    def get_objects(self):
        print(self.params)
        self.filter_by_amm1()
        self.filter_by_amm2()
        self.filter_by_amm3()
        self.filter_by_amm4()
        self.filter_by_lingua()
        return self.objects

    def filter_by_amm1(self):
        if self.params.get('amm1','') != '':
            candidato_residenza = CandidatoResidenza.objects.filter(amm1 = self.params['amm1'])
            self.objects = self.objects.filter(candidato__id__in = candidato_residenza.values_list('candidato__id'))

    def filter_by_amm2(self):
        if self.params.get('amm2','') != '':
            candidato_residenza = CandidatoResidenza.objects.filter(amm2 = self.params['amm2'])
            self.objects = self.objects.filter(candidato__id__in = candidato_residenza.values_list('candidato__id'))

    def filter_by_amm3(self):
        if self.params.get('amm3','') != '':
            candidato_residenza = CandidatoResidenza.objects.filter(amm3 = self.params['amm3'])
            self.objects = self.objects.filter(candidato__id__in = candidato_residenza.values_list('candidato__id'))

    def filter_by_amm4(self):
        if self.params.get('amm4','') != '':
            candidato_residenza = CandidatoResidenza.objects.filter(amm4 = self.params['amm4'])
            self.objects = self.objects.filter(candidato__id__in = candidato_residenza.values_list('candidato__id'))

    def filter_by_lingua(self):
        if self.params.get('lingua','') != '':
            lingua_conosciuta = Linguaconosciuta.objects.filter(lingua = self.params['lingua'])
            self.objects = self.objects.filter(candidato__id__in = lingua_conosciuta.values_list('candidato__id'))
        if self.params.get('livello','') != '':
            lingua_conosciuta = Linguaconosciuta.objects.filter(livello = self.params['livello'])
            self.objects = self.objects.filter(candidato__id__in = lingua_conosciuta.values_list('candidato__id'))
