class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    return """{}. "{}".{}, {}. Owned by {}.  {}""".format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)

class Marketplace:
  def __init__(self):
    self.listings = []
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  def remove_listing(self, list_to_remove):
    self.listings.remove(list_to_remove)
  def show_listings(self):
    for listing in self.listings:
      print(listing)

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return "{}, {}".format(self.art, self.price)

veneer = Marketplace()

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      newlist = Listing(art = artwork, price = price, seller = artwork.owner)
      veneer.add_listing(newlist)
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      for listing in veneer.listings:
        if listing.art == artwork:
          artwork.owner = self
          veneer.remove_listing(listing)


edytta = Client(name = "Edytta Halpirt", location = "Private Collector", is_museum = False)

moma = Client(name = "The MoMA", location = "New York", is_museum = True)

girl_with_mandolin = Art(artist = "Picasso, Pable", title = "Girl with a Mandolin", year = 1910, medium = "oil on canvas", owner = edytta)

edytta.sell_artwork(girl_with_mandolin, "$6M")
moma.buy_artwork(girl_with_mandolin)
