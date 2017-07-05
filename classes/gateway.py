# classfile for the Gateway class
import paho.mqtt.client as mqtt
import socket
import thread

# test import
from time import sleep


class Gateway:
    '''defines a gateway that receives state data from luminaires'''

    def __init__(self):
        '''constructs an instance of Gateway'''
        self.name = 'test_gateway'
        self.luminaires = []
        self.luminaireStateData = [] # list of dictionaries

    def add_luminaire(self, luminaire):
        '''adds a luminaire to collect data from to the gateway'''
        self.luminaires.append(luminaire)

        # reverse link
        luminaire.set_gateway(self)

    def store_state(self, state):
        '''receives snapshot from luminaire and stores it'''
        self.luminaireStateData.append(state)

    def publish_state_data(self):
        '''output collected state data to [console]'''

        # specify mqtt broker address and port
        broker_address = "localhost"
        port = 1883

        # create client and connect to broker
        mqtt_client = mqtt.Client("sim")
        mqtt_client.connect(broker_address, port)
        mqtt_client.loop_start()

        # publish all records to broker
        for record in self.luminaireStateData:

            # publish under topic
            topic = self.name + '/' + record['name']
            print 'posting: ' + topic + ' : ' + str(record)
            mqtt_client.publish(topic, str(record))

    def push_event_to_luminaires(self, event):
        '''adds event to all luminaires queues'''
        for luminaire in self.luminaires:
            luminaire.add_event_to_queue(event)

    def start_gateway_thread(self):
        '''starts the event listener'''
        self.listening = True
        thread.start_new_thread(self.event_listener, ())    

    def event_listener(self):
        '''thread that listens for message from ILEM'''

        # create socket
        s = socket.socket()
        host = socket.gethostname()
        port = 9701 # arbitrary, placeholder
        s.bind((host, port))
        s.listen(5)

        while True:
            c, addr = s.accept() 

            # receive packet
            packet = s.recv(1024)

            ## placeholder until structure of packet is known
            if packet == 'Source - Grid':
                event = 'source-grid'
            elif packet == 'Source - Battery':
                event = 'source-battery'
            elif packet == 'Battery Charging - Grid':
                event = 'charging-grid'
            elif packet == 'Battery Charging - Solar':
                event = 'charging-solar'
            else:
                print 'received instructions unclear'

            self.push_event_to_luminaires(event)

            c.close() 

    # def get_state_data(self, time):
    #     '''pull state data from all luminaires associated with this gateway'''
    #     for luminaire in self.luminaires:
    #         stateData = luminaire.get_state()
    #         stateData['timestamp'] =  time
    #         self.luminaireStateData.append(stateData)

        