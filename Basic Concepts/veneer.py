class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    strings = self.artist + "\"{}\"".format(self.title) + ". " + str(self.medium) + ", " + str(self.year) + ". " + self.owner.name + ", " + self.owner.location + "."
    return strings
  
class Marketplace:
  def __init__(self):
    self.listings = []
  
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  
  def remove_listing(self, expired_listing):
    self.listings.remove(expired_listing)
    
  def show_listings(self):
    for i in self.listings:
      print(i)

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    if is_museum:
      self.location = location
    else:
      self.location = "Private Collection"

  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
  
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for i in veneer.listings:
        if i.art == artwork:
          art_listing = i
          break
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)
    
  
    
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
    
  def __repr__(self):
    return self.art.title + str(self.price)

veneer = Marketplace()


edytta = Client("Edytta Halpirt","Private Collection",False)
moma  = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Monet, Claude. ", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil in canvas", edytta)

print(girl_with_mandolin)


edytta.sell_artwork(girl_with_mandolin," $6M (USD)")

veneer.show_listings()


moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)





