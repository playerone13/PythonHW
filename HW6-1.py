from time import sleep

class TrafficLight:
    __color = "Черный"

    def runnig(self):
        while True:
            print('Красный')
            sleep(7)
            print('Желтый')
            sleep(2)
            print('Зеленый')
            sleep(7)
            print('Желтый')
            sleep(2)

trafficlight = TrafficLight()
trafficlight.runnig()