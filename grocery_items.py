import pandas as pd
import numpy as np

def get_grocery_items(stores):

    # List of specific grocery items
    grocery_items = [
        'banana', 'apple', 'egg', 'milk', 'bread', 'cheese', 'butter', 'yogurt', 'chicken', 'beef',
        'pork', 'fish', 'lettuce', 'tomato', 'cucumber', 'carrot', 'potato', 'onion', 'garlic', 'pepper',
        'salt', 'sugar', 'flour', 'rice', 'pasta', 'beans', 'peas', 'corn', 'spinach', 'broccoli',
        'cauliflower', 'zucchini', 'eggplant', 'avocado', 'orange', 'grapefruit', 'lemon', 'lime', 'strawberry', 'blueberry',
        'raspberry', 'blackberry', 'grape', 'pear', 'peach', 'plum', 'kiwi', 'watermelon', 'cantaloupe', 'honeydew',
        'pineapple', 'mango', 'papaya', 'coconut', 'almond', 'walnut', 'pecan', 'hazelnut', 'pistachio', 'cashew',
        'chocolate', 'candy', 'cookie', 'cake', 'pie', 'donut', 'bagel', 'croissant', 'muffin', 'toast',
        'jam', 'jelly', 'peanut butter', 'honey', 'syrup', 'oatmeal', 'cereal', 'granola', 'cracker', 'chip',
        'pretzel', 'popcorn', 'soda', 'juice', 'tea', 'coffee', 'water', 'wine', 'beer', 'whiskey',
        'vodka', 'rum', 'gin', 'brandy', 'champagne', 'liqueur', 'energy drink', 'sports drink', 'milkshake', 'smoothie'
    ]

    # Ensure we have exactly 100 items (repeat the list if necessary)
    while len(grocery_items) < 100:
        grocery_items += grocery_items

    # Slice to ensure exactly 100 items
    grocery_items = grocery_items[:100]

    # Generate random prices for each grocery store
    np.random.seed(0)  # For reproducibility
    prices = {store: np.round(np.random.uniform(10, 100, 100), 2) for store in stores}

    # Create the DataFrame
    data = {'Grocery item': grocery_items}
    data.update(prices)

    df = pd.DataFrame(data)

    return df
