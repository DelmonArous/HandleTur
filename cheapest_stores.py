import pandas as pd

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
    total_cost_all_items = df['Cheapest price'].sum()
    total_savings_all_items = df['Savings'].sum()

    return df, total_cost, total_savings, total_cost_all_items, total_savings_all_items
