# We run a Candy shop where we sell candies and lollipops
# One lollipop's price is 10$
# And it made from 5gr of sugar
# One candie's price is 20$
# And it made from 10gr of sugar
# we can raise their prices with a given percentage
#
# Create a CandyShop class
# It can store sugar and money as income. The constructor should take the amount of sugar in gramms.
# we can create lollipops and candies store them in the CandyShop's storage
# If we create a candie or lollipop the CandyShop's sugar amount gets reduced by the amount needed to create the sweets
# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candie or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"

class Candy(object):
    
    
    def __init__(self):
        self.type_of_sweet == type_of_sweet
        if self.type_of_sweet == "candy":
            self.price_per_piece = 20
            self.needed_sugar = 10
        elif self.type_of_sweet == "lollipop":
            self.price_per_piece = 10
            self.needed_sugar = 5

    def raise_prices(self, percent):
        self.price_per_piece += self.price_per_piece / 100 * float(self.percent)
        return(self.price_per_piece)

   
class CandyShop(object):

    def __init__(self, all_sugar):
        self.all_sugar = all_sugar
        self.all_money = 0
        self.candies = []


    def create_sweets(self, type_of_sweet):
        self.candies.append(str(type_of_sweet))


    def get_status(self):
        sum_candy = 0
        sum_lollipop = 0
        for candy in self.candies:
            if self.candy.type_of_sweet == "candy":
                sum_candy += 1
                sugar_candy = self.candy.type_of_sweet(self.needed_sugar)
            if self.candy.type_of_sweet == "lollipop":
                sum_lollipop += 1
                sugar_lollipop = candy.type_of_sweet(self.needed_sugar)
        all_sugar -= sum_candy * sugar_candy + sum_lollipop * sugar_lollipop
        return "Invetory: "+ sum_candy + " candies, " + sum_lollipop + " lollipops, Income: 0, Sugar: " + all_sugar + "gr"

    def sell(self):
        pass
        

    def buy_sugar(self):
        pass




# candy_shop = CandyShop(300)
# candy_shop.create_sweets("candy")
# candy_shop.create_sweets("candy")
# candy_shop.create_sweets("lollipop")
# candy_shop.create_sweets("lollipop")
# print(candy_shop)
# Should print out:
# Invetory: 2 candies, 2 lollipops, Income: 0, Sugar: 270gr

#candy_shop.sell("candy", 1)
#print(candy_shop


# Should print out:
# "Invetory: 1 candies, 2 lollipops, Income:20, Sugar: 285gr"

#candy_shop.raise_prices(5)
#candy_shop.sell("lollipop", 1)
#print(candy_shop)

# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:35, Sugar: 285gr"

#candy_shop.buy_sugar(300)
#print(candy_shop)

# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:5, Sugar: 315gr"
