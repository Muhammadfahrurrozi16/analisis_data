import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# from babel.numbers import format_currency
sns.set(style='dark')

def create_top_seller_monthly(df):
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['order_month'] = df['order_purchase_timestamp'].dt.to_period('M')
    seller_sales = df.groupby(['seller_id', 'order_month']).agg(total_sales=('price', 'sum')).reset_index()
    top_seller_monthly = seller_sales.sort_values('total_sales', ascending=False).groupby('order_month').first().reset_index()

    return top_seller_monthly
def create_seller_per_city(df):
    seller_location = df[['seller_id', 'seller_city']].drop_duplicates()
    seller_per_city = seller_location.groupby('seller_city').agg(total_sellers=('seller_id', 'count')).reset_index()
    seller_per_city = seller_per_city.sort_values(by='total_sellers', ascending=False)

    return seller_per_city
main_df = pd.read_csv("dashboard/all_data.csv")

# datetime_columns = ["order_date", "delivery_date"]
# all_df.sort_values(by="order_date", inplace=True)
# all_df.reset_index(inplace=True)

# for column in datetime_columns:
#     all_df[column] = pd.to_datetime(all_df[column])

# # Filter data
# min_date = all_df["order_date"].min()
# max_date = all_df["order_date"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
#     start_date, end_date = st.date_input(
#         label='Rentang Waktu',min_value=min_date,
#         max_value=max_date,
#         value=[min_date, max_date]
#     )

# main_df = all_df[(all_df["order_date"] >= str(start_date)) & 
#                 (all_df["order_date"] <= str(end_date))]

top_seller_monthly = create_top_seller_monthly(main_df)
seller_per_city = create_seller_per_city(main_df)

st.subheader("Top seller Monthly")


fig, ax = plt.subplots(figsize=(12, 6))

sns.barplot(data=top_seller_monthly, x='order_month', y='total_sales', hue='seller_id', ax=ax)

ax.set_title('Top Seller per Month by Sales')
ax.set_xlabel('Month')
ax.set_ylabel('Total Sales')

plt.xticks(rotation=45)

ax.legend(title='Seller ID', loc='upper right')

plt.tight_layout()

st.pyplot(fig)

st.subheader("Best City Seller")

fig, ax = plt.subplots(figsize=(12, 6))

sns.barplot(
    data=seller_per_city.head(10), 
    x='seller_city', 
    y='total_sellers', 
    hue='seller_city', 
    dodge=False, 
    legend=False, 
    ax=ax
)
ax.set_title('Top 10 Cities with the Most Sellers')
ax.set_xlabel('City')
ax.set_ylabel('Number of Sellers')

plt.xticks(rotation=45)

plt.tight_layout()

st.pyplot(fig)


st.caption('Copyright')




