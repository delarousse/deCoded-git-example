#define a new empty dictionary
our_dictionary = {}
print(our_dictionary)
# define a dictionary with values
bestRapperCategories = {"southern":"Outkast","conscious":"Cole","mumble":"Migos"}
print(bestRapperCategories)
# reference an item in a dictionary
print(bestRapperCategories["southern"])
# changing an item in a dictionary
bestRapperCategories["southern"] = "Kodak"
print(bestRapperCategories)
# adding items to a dictionary
bestRapperCategories["northern"] = "Jay-Z"
print(bestRapperCategories)
# deleting items from a dictionary
del bestRapperCategories["mumble"]
print(bestRapperCategories)