
class Latin:
   def __init__(self):
      self.translations={'car':'carlete','bike':'biklete'}
   
   def translate(self,word):
      print(self.translations.get(word))

class Russian:
   def __init__(self):
      self.translations={'car':'mashina','bike':'velik'}
   
   def translate(self,word):
      print(self.translations.get(word))

def Factory(language):
   languages={
      'Latin':Latin,
      'Russian':Russian,
   }
   return languages[language]()

words=['car','bike']

l=Factory('Latin')
l.translate(words[0])