
class Washing:
   def wash(self):
      print('washes...')

class Spinning:
   def spin(self):
      print('spines.....')

class Rinsing:
   def rinse(self):
      print('rinses...')

class Facade_machine:
   def __init__(self):
      self.washing=Washing()
      self.spinning=Spinning()
      self.rinsing=Rinsing()
   
   def work(self):
      self.washing.wash()
      self.spinning.spin()
      self.rinsing.rinse()

washing_machine=Facade_machine()
washing_machine.work()