#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    count = float("inf")
    for i in range(0, len(recipe)):
          recipe_key = (list(recipe.keys())[i])
          try:
            # if ingredients[recipe_key]:
              portion = ingredients[recipe_key] // recipe[recipe_key]
              if portion < count:
                  count = portion
              else:
                  i += 1
                  
          except KeyError:
              count = 0
              break
            
    return count    


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))