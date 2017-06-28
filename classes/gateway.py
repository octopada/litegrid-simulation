# classfile for the Gateway class


class Gateway:
    '''defines a gateway that receives state data from luminaires'''

    def __init__(self):
        '''constructs an instance of Gateway'''
        self.luminaires = []
        self.luminaireStateData = [] # list of dictionaries

    def add_luminaire(self, luminaire):
        '''adds a luminaire to collect data from to the gateway'''
        self.luminaires.append(luminaire)

    def get_state_data(self, time):
        '''pull state data from all luminaires associated with this gateway'''
        for luminaire in self.luminaires:
            stateData = luminaire.get_state()
            stateData['timestamp'] =  time
            self.luminaireStateData.append(stateData)

    def publish_state_data(self):
        '''output collected state data to [console]'''
        print self.luminaireStateData ## raw

        