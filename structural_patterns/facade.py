
class Washing:
   def wash(self):
      print('washes...')

class Rinsing:
   def rinse(self):
      print('rinses...')

class Spinning:
   def spin(self):
      print('spins...')

class Facade:
   def __init__(self):
      self.washing=Washing()
      self.rinsing=Rinsing()
      self.spinning=Spinning()
   
   def work(self):
      self.washing.wash()
      self.rinsing.rinse()
      self.spinning.spin()

washing_machine=Facade()
washing_machine.work()
