class Animal(object):
  def __init__(self, name, weight, voice):
    self.name = name
    self.weight = weight
    self.voice = voice

  def feed(self):
    # кормить
    print('Feed', self.name)

  def voice(self):
    # различать по голосам(коровы мычат, утки крякают и т.д.)
    print('voice', self.name, self.voice)

  def product(self):
    raise NotImplementedError("Please Implement this method")


class Sheep(Animal):
  def __init__(self, name, weight):
    super().__init__(name, weight, 'beee')

  def shave(self):
    # овец стричь
    print('Shave', self.name)

  def product(self):
    self.shave()


class MilkyAnimal(Animal):
  def milk(self):
    # корову и коз доить
    print('Take milk from', self.name)

  def product(self):
    self.milk()


class Cow(MilkyAnimal):
  def __init__(self, name, weight):
      
    super().__init__(name, weight, 'mooo')


class Goat(MilkyAnimal):
  def __init__(self, name, weight):
    super().__init__(name, weight, 'meee')


class Bird(Animal):
  def __init__(self, name, weight, voice):
    super().__init__(name, weight, voice)

  def egg(self):
    # собирать яйца у кур, утки и гусей
    print('Take eggs from', self.name)

  def product(self):
    self.egg()


class Goose(Bird):
  def __init__(self, name, weight):
    super().__init__(name, weight, 'honk')


class Chicken(Bird):
  def __init__(self, name, weight):
    super().__init__(name, weight, 'kudah')


class Duck(Bird):
  def __init__(self, name, weight):
    super().__init__(name, weight, 'krya')


goose_1 = Goose('Gray', 6.2)
goose_2 = Goose('White', 7.1)
cow = Cow("Man'ka", 150.3)
sheep_1 = Sheep('Barashek', 20.6)
sheep_2 = Sheep('Curly', 24.7)
chicken_1 = Chicken('KoKo', 3.1)
chicken_2 = Chicken('Kukareku', 3.5)
goat_1 = Goat('Roga', 16.8)
goat_2 = Goat('Kopyta', 18)
duck = Duck('Kryakva', 4)

animals = [goose_1, goose_2, cow, sheep_1, sheep_2, chicken_1, chicken_2, goat_1, goat_2, duck]


print('feed animals\n')
for animal in animals:
    animal.feed()
print('\ninteraction with animals:\n')
for animal in animals:
    animal.product()


total_weight = 0
heaviest_animal = None
for animal in animals:
  total_weight = total_weight + animal.weight
print('\nTotal weight of animals:', format(total_weight, '.2f'))

for animal in animals:
  if heaviest_animal is None:
    heaviest_animal = animal
  elif animal.weight > heaviest_animal.weight:
    heaviest_animal = animal
print('The heaviest animal is', heaviest_animal.name)
