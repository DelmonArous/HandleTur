import pandas as pd

def get_shopping_list(df_grocery_items):

    # Randomly select 25 items from the DataFrame
    df = df_grocery_items.sample(n=25, random_state=1)

    # Extract store names dynamically (all columns except 'Grocery item')
    stores = df.columns.difference(['Grocery item'])

    # Ensure the price columns are numeric
    for store in stores:
        df[store] = pd.to_numeric(df[store])

    return df
