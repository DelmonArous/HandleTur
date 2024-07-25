import pandas as pd
import numpy as np

def find_cheapest_stores(df_shopping_list, sort_by = 'Cheapest store'):

    # Initialize an empty list to store the results
    cheapest_stores = []

    # Extract store names dynamically (all columns except 'Grocery item')
    stores = df_shopping_list.columns.difference(['Grocery item'])

    # Initialize a dictionary to store total costs and savings
    # Initialize dictionaries to store total costs and savings
    total_cost = {store: 0 for store in stores}
    total_savings = {store: 0 for store in stores}

    # Iterate through each row in the shopping list DataFrame
    for index, row in df_shopping_list.iterrows():
        item = row['Grocery item']
        prices = row[stores]

        # Sort the prices
        sorted_prices = prices.sort_values()

        # Find the minimum, second minimum, and maximum prices
        min_price = sorted_prices.iloc[0]
        min_stores = sorted_prices[sorted_prices == min_price].index.tolist()

        # Handle ties for the minimum price
        if len(min_stores) > 1:
            # More than one store has the minimum price
            remaining_prices = sorted_prices[~sorted_prices.index.isin(min_stores)]
            if not remaining_prices.empty:
                second_min_price = remaining_prices.min()
                second_min_stores = remaining_prices[remaining_prices == second_min_price].index.tolist()
            else:
                second_min_price = min_price
                second_min_stores = min_stores
        else:
            # No tie for minimum price
            second_min_price = sorted_prices.iloc[1]
            second_min_stores = sorted_prices[sorted_prices == second_min_price].index.tolist()

        # Choose the first store for second minimum price if there are multiple
        second_min_store = second_min_stores[0]
        max_price = sorted_prices.iloc[-1]
        max_store = sorted_prices.index[-1]
        
        # Handle ties for the second minimum price
        if len(second_min_stores) > 1:
            # If multiple stores have the second minimum price, choose the one that is not the same as the minimum price
            second_min_store = next(store for store in second_min_stores if store not in min_stores)

        # Calculate savings for the item
        savings = second_min_price - min_price
        cheapest_stores.append((item, min_stores[0], second_min_store, max_store, min_price, second_min_price, max_price, savings))
        
        # Update total cost and savings
        total_cost[min_stores[0]] += min_price
        total_savings[min_stores[0]] += savings

    # Create a DataFrame from the results
    df = pd.DataFrame(
        cheapest_stores,
        columns=
            [
                'Grocery item',
                'Cheapest store',
                'Second cheapest store',
                'Most expensive store',
                'Cheapest price',
                'Second cheapest price',
                'Most expensive price',
                'Savings'
            ]
    )

    # Sort the DataFrame by 'Cheapest store', 'Second cheapest store', and 'Most expensive store'
    df = df.sort_values(by=[sort_by, 'Grocery item'])

    # Calculate the total cost and total savings
    total_cost_all_items = np.round(df['Cheapest price'].sum(), 1)
    total_savings_all_items = np.round(df['Savings'].sum(), 1)

    return df, total_cost, total_savings, total_cost_all_items, total_savings_all_items
