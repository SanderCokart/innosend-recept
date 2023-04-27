"""
A simple flask template with 1 api route for a GET, and POST request.
"""

import json

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def get_recipes_from_json():
    """
    Returns recipes.json.
    """
    # open json file
    json_data = open('recipes.json')

    # load json file
    recipes = json.load(json_data)

    # return json object    
    return recipes


def get_recipe_from_id(recipes, recipe_id):
    """
    Returns recipe with id.
    """
    # get recipe with id
    print(recipe_id)
    for recipe in recipes:
        print(recipe)
        if int(recipe['id']) == int(recipe_id):
            print('hier aangekomen')
            return recipe

    return None

@app.route('/recipes', methods=['GET'])
def get_recipes():
    """
    Returns recipes.json.

    """
    return jsonify({'status': 'success', 'data': get_recipes_from_json()}), 200

@app.route('/recipes', methods=['POST'])
def add_recipe():
    """
    Adds a recipe to the global variable.
    """
    # get json data from request
    data = request.get_json()

    # get recipes from json file
    recipes = get_recipes_from_json()

    required_keys = [*recipes[0]]

    # remove id from required keys
    required_keys.remove('id')

    # get last id
    last_id = int(recipes[-1]['id'])

    # check if all required keys are in the request
    if not all(key in data for key in required_keys):
        # get the missing keys
        missing_keys = [key for key in required_keys if key not in data]

        return jsonify({'status': 'error', 'message': 'Missing required keys', 'details': missing_keys}), 400

    # add id to the recipe
    data['id'] = last_id + 1

    # add recipe to recipes
    recipes.append(data)

    # write recipes to json file
    with open('recipes.json', 'w') as outfile:
        json.dump(recipes, outfile)

    return jsonify({'status': 'success', 'data': recipes}), 200

@app.route('/recipes/favorite', methods=['POST'])
def favorite_recipe():
    data = request.get_json()
    recipe = None

    # check if id is in the request
    if not 'id' in data:
        return jsonify({'status': 'error', 'message': 'Missing required keys', 'details': ['id']}), 400
    
    # get recipes from json file
    recipes = get_recipes_from_json()

    # get recipe with id
    recipe = get_recipe_from_id(recipes, data['id'])
    
    # check if recipe exists
    if recipe is None:
        return jsonify({'status': 'error', 'message': 'Recipe not found'}), 404
    
    # update favorite. if favorite is true, set it to false and vice versa
    recipe['favorite'] = not recipe['favorite']

    # write recipes to json file
    with open('recipes.json', 'w') as outfile:
        json.dump(recipes, outfile)
    
    return jsonify({'status': 'success', 'data': recipes}), 200


@app.route('/recipes/rate', methods=['POST'])
def rate_recipe():
    data = request.get_json()
    recipe = None

    # check if id is in the request
    if not 'id' in data:
        return jsonify({'status': 'error', 'message': 'Missing required keys', 'details': ['id']}), 400

    # check if rating is in the request
    if not 'rating' in data:
        return jsonify({'status': 'error', 'message': 'Missing required keys', 'details': ['rating']}), 400
    
    #check if rating is between 1 and 5
    if not data['rating'] in range(1, 6):
        return jsonify({'status': 'error', 'message': 'Rating must be between 1 and 5', 'details': ['rating']}), 400

    # get recipes from json file
    recipes = get_recipes_from_json()

    # get recipe with id
    recipe = get_recipe_from_id(recipes, data['id'])
    
    # check if recipe exists
    if recipe is None:
        return jsonify({'status': 'error', 'message': 'Recipe not found'}), 404

    # update rating
    recipe['rating'] = data['rating']

    # write recipes to json file
    with open('recipes.json', 'w') as outfile:
        json.dump(recipes, outfile)
    
    return jsonify({'status': 'success', 'data': recipes}), 200



# Run the app
if __name__ == '__main__':
    app.run(debug=True)
