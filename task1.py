import pandas as pd
import matplotlib.pyplot as plt # type: ignore

df = pd.read_csv('transactions.csv')

def get_column_names(df):
    return list(df.columns)

def get_first_k_rows(df, k):
    return df.head(k)

def get_rand_sample(df, k):
    return df.sample(n=k)

def get_unique_trans_type(df, type):
    return df[type].unique().tolist()

def get_top_ten_trans_destinations(df, nameDest):
    return df[nameDest].value_counts().head(10)
    
def get_flagged_fraud(df, isFlaggedFraud):
    return df[df[isFlaggedFraud] == True]

def get_dist_dest_per_src(df, nameOrig, nameDest):
    distinctDestinations = df.groupby(nameOrig)[nameDest].nunique().reset_index()
    distinctDestinations.columns = [nameOrig, 'distinct_destinations_count']
    return distinctDestinations.sort_values(by='distinct_destinations_count', ascending=False)

def visual_1(df):
    def transaction_counts(df):
        return df['type'].value_counts()
    
    def transaction_counts_split_by_fraud(df):
        return df.groupby(['type', 'isFlaggedFraud']).size().unstack(fill_value=0)

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar', color='skyblue')
    axs[0].set_title('Transaction Types')
    axs[0].set_xlabel('Transaction')
    axs[0].set_ylabel('Count')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar', stacked=True, color=['skyblue', 'salmon'])
    axs[1].set_title('Transaction Types Split By Fraud')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Count')
    fig.suptitle('Transaction Analysis', fontsize=17)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return ("The first bar chart shows the frequency of each transaction type."
            "The second bar chart shows the frequency of each transaction type split by fraud.")


visual_1(df)


def visual_2(df):
    def query(df):
        return df[df['transaction_type'] == 'CASH_OUT']
        
    plot = query(df).plot.scatter(x='oldbalanceDest', y='newbalanceDest')
    plot.set_title('Origin Account Balance Delta vs. Destination Account Balance Delta')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return "The scatter plot shows the relationship between the change in the origin account balance and the change in the destination account balance for Cash Out transactions. "

visual_2(df)


def visual_custom(df):
    def exercise_custom(df):
        
        return df.groupby('transaction_type')['amount'].mean().sort_values()

    
    plot = exercise_custom(df).plot(kind='bar', color='skyblue')
    plot.set_title('Average Transaction Amount by Transaction Type')
    plot.set_xlabel('Transaction Type')
    plot.set_ylabel('Average Amount')
    
    
    for p in plot.patches:
        plot.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                      ha='center', va='baseline', fontsize=10, color='black', xytext=(0, 5), textcoords='offset points')
    
    return ("This bar chart shows the average transaction amount for each transaction type. "
            "It helps in understanding which types of transactions generally involve higher amounts of money.")


description = visual_custom(df)
print(description)
