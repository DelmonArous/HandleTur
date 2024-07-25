# %%
import pandas as pd
import numpy as np
from grocery_items import get_grocery_items
from shopping_list import get_shopping_list
from cheapest_stores import find_cheapest_stores

# List of grocery stores
stores = ['Meny', 'Spar', 'Kiwi', 'Rema 1000', 'Bunnpris', 'Coop Extra', 'Coop Prix', 'Coop Obs', 'Coop Mega', 'Joker']

# Get the grocery items DataFrame
df_grocery_items = get_grocery_items(stores)

# Get the shopping list DataFrame
df_shopping_list = get_shopping_list(df_grocery_items)

# Get the cheapest store Dataframe and 
df_cheapest_stores, total_cost, total_savings, total_cost_all_items, total_savings_all_items = find_cheapest_stores(df_shopping_list)

# Display the results
print(df_cheapest_stores)
print("\nTotal cost per store:")
print(total_cost)
print("\nTotal savings per store:")
print(total_savings)
print(f"\nTotal cost for all items: {total_cost_all_items:.2f}")
print(f"Total savings for all items: {total_savings_all_items:.2f}")
