"""emitter_light controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot,Supervisor,LED,Receiver
import struct
# create the Robot instance.
supervisor = Supervisor()
# super_visior=Supervisor()

# get the time step of the current world.
timestep = int(supervisor.getBasicTimeStep())

class BlinkingLED:
    def __init__(self, led_device):
        self.led_device = led_device
        self.on = True

    def toggle(self):
        self.led_device.set(self.on)
        self.on = not(self.on)


redLed = BlinkingLED(supervisor.getDevice("red"))
greenLed = BlinkingLED(supervisor.getDevice("green"))
yellowLed = BlinkingLED(supervisor.getDevice("yellow"))
receiver = supervisor.getDevice("receiver")
# redLed.toggle()
receiver.enable(timestep)
# Receiver.enable(receiver,timestep)
print(receiver,"receiver")
print(supervisor.getDevice("red").get())
# greenLed.toggle()
# Main loop:
import time
# - perform simulation steps until Webots is stopping the controller
while supervisor.step(timestep) != -1:
    # print(redLed.get())
    # redLed.set((255,0,0))
    #print(supervisor.step(timestep) )
    # time.sleep(supervisor.step(timestep) )
    try:
        # print(receiver.getString())
        # greenLed.toggle()
        
        if receiver.getQueueLength() > 0:
            message=receiver.getString()
            if message == "green":
                supervisor.getDevice("green").set(1)
                supervisor.getDevice("red").set(0)
            print(message)
            
        else:
            supervisor.getDevice("red").set(1)
            supervisor.getDevice("green").set(0)
            print("---green değil----")
            # receivedData = receiver.getString().decode("utf-8")
            # print("supervisor handle receiver data:", receivedData)
            # sreceiver.nextPacket()
        # else:
            # print("supervisor receiver q is empty")
            
        # data=struct.unpack("i",message)
        
    except OSError as e:
        continue
    message="bos"
    # supervisor.getDevice("red").set(1)
    # supervisor.getDevice("green").set(0)
        
    # if i == 0:
      # new_value = [2.5, 0, 0]
      # translation_field.setSFVec3f(new_value)
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

