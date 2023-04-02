import argparse
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules


def generate_association_rules(input_item):
    df = pd.read_csv('grouped_items.csv')
    transactions = []
    x = []
    for i in range(len(df)):
        itm = df.iat[i, 1]
        x = itm.split(',')
        transaction = []
        for i in x:
            j = i.replace("'", "")
            if j.startswith("["):
                j = j[1:]
            elif j.endswith("]"):
                j = j[:1]
            if j.startswith(" "):
                j = j[1:]
            transaction.append(j)
        transactions.append(transaction)
    new_transactions=[]
    for i in transactions:
        transaction=[]
        new_transactions.append(i[:-1])
    te = TransactionEncoder()
    te_ary = te.fit(new_transactions).transform(new_transactions)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
    filtered_rules = rules[(rules['lift'] > 1) & (rules['confidence'] > 0.5)]
    sorted_rules = filtered_rules.sort_values(by=['lift', 'confidence'], ascending=False)
    if sorted_rules.empty:
        return "No association rules found with the given minimum support and confidence values."
    # Get the most likely bought items with the input_item as antecedent
    rules_antecedent = sorted_rules[sorted_rules['antecedents'].apply(lambda x: input_item in x)]
    rules_antecedent = rules_antecedent.sort_values(by=['lift', 'confidence'], ascending=False)

    # Get the most likely bought items with the input_item as consequent
    rules_consequent = sorted_rules[sorted_rules['consequents'].apply(lambda x: input_item in x)]
    rules_consequent = rules_consequent.sort_values(by=['lift', 'confidence'], ascending=False)
    merged_rules = pd.concat([rules_antecedent, rules_consequent])
    top_items = merged_rules.head(10)['antecedents'].apply(lambda x: list(x)[0])
    return list(top_items)


def get_most_likely_bought_item(input_item):
    likely_items = generate_association_rules(input_item)
    temp = likely_items[0]
    i = 0
    while temp == input_item:
        i += 1
        if i == len(likely_items):
            temp = likely_items[0]
            break
        temp = likely_items[i]
        if temp == '':
            temp = likely_items[i+1]
        else:
            pass
    return temp


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the most likely bought item from a retail dataset')
    parser.add_argument('input_item', type=str, help='Input item to get the most likely bought item')
    args = parser.parse_args()
    input_item = args.input_item
    output_item = get_most_likely_bought_item(input_item)
    print(f'The most likely bought item with {input_item} is {output_item}')
