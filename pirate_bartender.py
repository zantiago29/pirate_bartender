import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def pref_questions():
    """function that takes drinks preferences from customer and creates new dictionary"""
    customer_preferences = {}
    for key, value in questions.items():
        customer_input = input(value + " ")
        customer_preferences[key] = (customer_input == "y" or customer_input == "yes")
    return customer_preferences
    
def create_drink(value): #why is (value) a parameter of the creat_drink function?
    """use preferences to create a drink"""
    #create empty list
    my_drink = []
    for key, value in value.items():
        if value is True:
            my_drink.append(random.choice(ingredients[key])) #why key and not value?
    return my_drink
    
# result

def main():
    results = pref_questions()
    print("Based on your choices, I recommend a cocktail with:")
    for drink in create_drink(results):
        print("    " + drink)
        
if __name__ == "__main__":
    main()
    
    
    

        
    













