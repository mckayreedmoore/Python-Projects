#parent element
class computer:
    def turnOn():
        print('Ensure that the computer is plugged in and press the power button')
    cpuManufacturer = ''
    gpuManufacturer = ''


class laptop(computer):
    #difference in this fuction to reflect the differences when you power a laptop on
    def turnOn():
        print('If the battery is charged press the power button. If not, plug in the charger and press the power button.')
    dedicatedGPU = ''
    discDrive = ''
        

class phone(computer):
    #difference in this function to reflect the differences when you power a phone on
    def turnOn():
        print('If the battery is charged hold the power button. If not, plug in the charger and hold the power button.')
    phoneManufacturer = ''
    expandableStorage = ''
