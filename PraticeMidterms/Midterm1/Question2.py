def bread(flour, water, yeast, salt):

    # floor dividing here allows to see the most amout of full servings
    # each individual ingredent can make
    MostFlour = flour // 600
    MostWater = water // 300 
    MostYeast = yeast // 100 
    MostSalt = salt // 10 

    # we then return the minimum of those variable becasue the item
    # that we have the lease of will be our limiting factor in making more bread

    return min(MostFlour, MostWater, MostYeast, MostSalt)


flour = int(input("How much flour do you have in grams: "))
water = int(input("How much water do you have in grams: "))
yeast = int(input("How much yeast do you have in grams: "))
salt = int(input("How much salt you have in grams: "))
    


print(f"You can make {bread(flour, water, yeast, salt)} full servings of bread with the current amout of ingredients.")



'''
# You can also do this to do it in one line :)
def bread(flour, water, yeast, salt):
    return min(flour // 600, water // 300, yeast // 100, salt // 10)
'''
