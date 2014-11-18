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

# Print the initial inventory of the bike shop for each bike it carries
print "You are entering {} bicycle store".format(my_store.get_name())
print "Our inventory at the moment is this:"
print "-" * 15
for bicycle in range(len(bikes)):
  print bikes[bicycle]

# Print the name of each customer and a list of the bikes offered by the bike shop that they can afford given their budget

# Iterate through clients
for client in range(len(clients)):
  # list of affordable bikes
  options = []
  print ""
  print "{} can afford:".format(clients[client].name)
  # Check which bikes each client can buy at store prices
  for bike in range(len(my_store.inventory)):
    if my_store.inventory[bike].sell_price <= clients[client].funds:
      options.append(my_store.inventory[bike])
  for bike in range(len(options)):
    print "{}. The {} bike".format(bike+1, options[bike].model)
  
  # Select and sell the bicycle each client is going to buy
  selection = int(raw_input("Which bike do you want?, enter a number:\n"))-1
  
  my_store.sell_bike(clients[client], options[selection])
  print "{} bought the {} bicycle, it's remaining funds are ${}".format(clients[client].name, options[selection],clients[client].funds )
  print "After this purchase, the remaining bicycles in the store are:"
  for bike in range(len(my_store.inventory)):
    print my_store.inventory[bike].model
  
  
  
 
print ""
print "-" * 20