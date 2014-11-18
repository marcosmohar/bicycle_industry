from bicycles import *

# Build a list of bicycles for the store inventory
downhill = Bicycle("Downhill", 14, 900)
freestyle = Bicycle("Freestyle", 8, 300)
mtb = Bicycle("Mtb", 14, 400)
fixie = Bicycle("Fixie", 9, 100)
race = Bicycle("Race", 8, 1000) 
city = Bicycle("City", 12, 800)

# Build an inventory of bicycles
bikes = [downhill, freestyle, mtb, fixie, race, city]

# Create a bicycle shop that has 6 different bicycle models in stock
my_store = Bike_shop('Keep rolling!', bikes)

# Create three customers
client1 = Costumer('Alvin', 200)
client2 = Costumer('Justin', 500)
client3 = Costumer('Marcos', 1000)

clients = [client1, client2, client3]

# Print the name of each customer and a list of the bikes offered by the bike shop that they can afford given their budget
for client in range(len(clients)):
  print ""
  print "{} can afford the:".format(clients[client].name)
  for bike in range(len(my_store.inventory)):
    if my_store.inventory[bike].sell_price <= clients[client].funds:
      print "\t{} bicycle".format(my_store.inventory[bike].model)
 
print ""
print "-" * 20

# Print the initial inventory of the bike shop for each bike it carries
print "{} Inventory".format(my_store.get_name())
print "-" * 15
for bicycle in range(len(bikes)):
  print bikes[bicycle]

