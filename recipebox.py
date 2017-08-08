ingredients = {"ice cream": "1/2 gallon", "fine graham crackers": "1 1/2 cup", "melted butter": "6 tablespoons", "sugar": "1/4 cup + 2 tablespoons", "store-bought cheescake":"8-9 inch at room temperature", "strawberries" : "1 pint, hulled an cut", "lemon" : "1/2 juiced"}
instructions = ["Set the ice cream out at room temperature to soften for about 30 minutes. Meanwhile, use a fork to mix together the graham cracker crumbs, butter, and 1/4 cup sugar in a bowl. Press this mixture over the bottom and sides of a 9-inch springform pan with your fingers; then press all over with the flat bottom of a glass to get the crust really well pressed together and compact. Set aside.",
"When the ice cream has softened, cream it in a mixer with a paddle attachment (or by hand in a bowl with a wooden spoon) until soft and creamy, but not melted. Break the cheesecake into pieces and beat or fold it into the ice cream. Pour the mixture into the prepared springform pan and smooth the top. Put that in the freezer to set.",
"Now combine the strawberries, the remaining 2 tablespoons sugar, and the lemon juice in non-reactive saucepan and warm over medium heat just until the strawberries begin to break down and give off their juice, 3 to 5 minutes. Stick that into the refrigerator to chill.",
"When you're ready to serve, remove the sides of the springform pan and put the frozen cheesecake on a cake plate. Spoon the strawberries over the top and serve."]
ingredients1 = {"fettuccini pasta" : "24 ounces", "butter" : "1 cup", "heavy cream" : "3/4 pint" : "salt and pepper", "garlic salt" : "1 dash", "romano cheese" : "3/4 cups", "parmasan cheese" : "1/2 cup"}
instructions2 = ["Bring a large pot of lightly salted water to a boil. Add fettuccini and cook for 8 to 10 minutes or until al dente; drain.", "In a large saucepan, melt butter into cream over low heat. Add salt, pepper and garlic salt. Stir in cheese over medium heat until melted; this will thicken the sauce.", "Add pasta to sauce. Use enough of the pasta so that all of the sauce is used and the pasta is thoroughly coated. Serve immediately."]

recipebook = {"fake strawberry cheesecake" : ingredients }

for keys,values in ingredients.items():
    print(values)
    print(keys)
    print("")
i= 1
for entry in instructions:
    print (str(i) + ":", entry)
    i +=1

for keys,values in ingredients1.items():
    print(values)
    print(keys)
    print("")
i=1
for entry in instructions:
    print (str(i) + ":", entry)
    i +=1
