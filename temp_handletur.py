# %%
import pandas as pd
import numpy as np

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
meny_prices = np.round(np.random.uniform(10, 100, 100), 2)
spar_prices = np.round(np.random.uniform(10, 100, 100), 2)
kiwi_prices = np.round(np.random.uniform(10, 100, 100), 2)
rema_1000_prices = np.round(np.random.uniform(10, 100, 100), 2)
bunnpris_prices = np.round(np.random.uniform(10, 100, 100), 2)

# Create the DataFrame
data = {
    'Grocery item': grocery_items,
    'Meny': meny_prices,
    'Spar': spar_prices,
    'Kiwi': kiwi_prices,
    'Rema 1000': rema_1000_prices,
    'Bunnpris': bunnpris_prices
}

df = pd.DataFrame(data)

# Randomly select 25 items from the DataFrame
shopping_list_df = df.sample(n=25, random_state=1)

# Ensure the price columns are numeric
for store in ['Meny', 'Spar', 'Kiwi', 'Rema 1000', 'Bunnpris']:
    shopping_list_df[store] = pd.to_numeric(shopping_list_df[store])

# Initialize an empty list to store the results
cheapest_stores = []

# Initialize a dictionary to store total costs and savings
total_cost = {'Meny': 0, 'Spar': 0, 'Kiwi': 0, 'Rema 1000': 0, 'Bunnpris': 0}
total_savings = {'Meny': 0, 'Spar': 0, 'Kiwi': 0, 'Rema 1000': 0, 'Bunnpris': 0}

# Iterate through each row in the shopping list DataFrame
for index, row in shopping_list_df.iterrows():
    item = row['Grocery item']
    prices = row[['Meny', 'Spar', 'Kiwi', 'Rema 1000', 'Bunnpris']]
    
    # Find the minimum and second minimum prices
    sorted_prices = prices.sort_values()
    min_price = sorted_prices.iloc[0]
    min_store = sorted_prices.index[0]
    second_min_price = sorted_prices.iloc[1]
    second_min_store = sorted_prices.index[1]
    max_price = sorted_prices.iloc[-1]
    max_store = sorted_prices.index[-1]
    
    # Calculate savings for the item
    savings = second_min_price - min_price
    cheapest_stores.append((item, min_store, second_min_store, max_store, min_price, second_min_price, max_price, savings))
    
    # Update total cost and savings
    total_cost[min_store] += min_price
    total_savings[min_store] += savings

# Create a DataFrame from the results
cheapest_stores_df = pd.DataFrame(cheapest_stores, columns=['Grocery item', 'Cheapest store', 'Second cheapest store', 'Most expensive store', 'Cheapest price', 'Second cheapest price', 'Most expensive price', 'Savings'])

# Calculate the total cost and total savings
total_cost_all_items = cheapest_stores_df['Cheapest price'].sum()
total_savings_all_items = cheapest_stores_df['Savings'].sum()

# Display the results
print(cheapest_stores_df)
print("\nTotal cost per store:")
print(total_cost)
print("\nTotal savings per store:")
print(total_savings)
print(f"\nTotal cost for all items: {total_cost_all_items:.2f}")
print(f"Total savings for all items: {total_savings_all_items:.2f}")

# %%
