# -*- coding: utf-8 -*-

class Steer(object):
    def __init__(self, client):
        self.client = client
        self.line = 90
        self.obj_list = []
        self.state = 'NONE'
        self.speed = '0'
        self.light_signal = 'NONE'
        self.obs = 'NO'


    def Set_ObjectDetection(self, obj):  # YOLO Object detection
        self.obj_list = obj


    def Control(self):
        # speed limit
        if 'bear' in self.obj_list:
            print('bear')
            if self.speed != '30':
                self.client.send('slow'.encode())
                self.speed = '30'
                print('제한속도 : 30')


        if self.light_signal == 'LIGHT_STOP':
            self.light_signal = 'DRIVE'
            self.state = 'DRIVE'
            self.client.send('lw'.encode())
            print('GO')

        if self.light_signal != 'LIGHT_STOP':
            if self.state != 'STOP':
                self.state = 'DRIVE'
                if self.line < 45:
                    self.client.send("0".encode())
                elif self.line < 135:
                    self.client.send(str(self.line - 45).encode())
                else:
                    self.client.send("90".encode())