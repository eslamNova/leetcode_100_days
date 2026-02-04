import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """
    LeetCode Pandas: Customer Placing the Largest Number of Orders

    orders: DataFrame with columns ['order_number', 'customer_number']
    returns: DataFrame with a single column ['customer_number']
             containing the id of the customer who has the most orders.
    """
    # 1) Count how many orders each customer has.
    #    value_counts() returns a Series like:
    #    customer_number
    #    3    2
    #    1    1
    #    2    1
    #    (index = customer_number, values = counts)
    counts = orders["customer_number"].value_counts()

    # 2) Take the customer_number (index) with the largest count.
    #    idxmax() gives the index label of the maximum value.
    top_customer = counts.idxmax()

    # 3) LeetCode expects a DataFrame with one column: customer_number
    #    and one row: the id we just found.
    result = pd.DataFrame({"customer_number": [top_customer]})

    return result


if __name__ == "__main__":
    # Small example so you can run this file locally and see the result.
    data = {
        "order_number": [1, 2, 3, 4],
        "customer_number": [1, 2, 3, 3],
    }
    df = pd.DataFrame(data)
    print(largest_orders(df))


