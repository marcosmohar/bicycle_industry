class Bicycle(object):
  """
  Must have a model, weight and cost to produce
  """
  
  def __init__(self, model, weight, cost):
    self.model = model
    self.weight = weight
    self.cost = cost
    self.sell_price = self.cost * 1.2
  
  def get_cost(self):
    return self.cost
  
  def get_price(self):
    return self.sell_price
  
  def get_model(self):
    return self.model
  
  def __repr__(self):
        return "The {} bicyle costs ${} in store.".format(
            self.model, self.sell_price)
  
class Bike_shop(object):
  """ 
  Must have a name, an inventory, be able to sell bicycles and check profits
  """
  
  def __init__(self, name, inventory):
    self.name = name
    self.inventory = inventory
    self.profit = 0
  
  def get_name(self):
    return self.name
  
  def get_inventory(self):
    return self.inventory
  
  def get_profit(self):
    return self.profit
  
  def sell_bike(self, customer, bike):
    """
    Removes bicycle from inventory, updates profits and adds bicycle to costumber inventory
    """
    self.inventory.remove(bike)
    customer.buy_bike(bike)
    self._profit += bike.get_price() - bike.get_cost()

    
class Costumer(object):
  """
  Costumers have a name, funds and the ability to buy and store bicycles
  """
  def __init__(self, name, funds):
    self.name = name
    self.funds = funds
    self.bikes = []
    
  def get_name(self):
    return self.name
  
  def get_funds(self):
    return self.funds
  
  def get_bicycles(self):
    return self.bikes
    
  def buy_bike(self, bicycle):
    """ Add new bicycle to our stock after paying for it"""
    self.funds = self.funds - bicycle.sell_price
    bikes.append(bicycle)
    
  
    
    
    
    
    
    
    
