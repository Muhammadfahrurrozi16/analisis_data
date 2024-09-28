import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# from babel.numbers import format_currency
sns.set(style='dark')

def create_top_5_cities_customers_2018(all_df):
    all_df['order_purchase_timestamp'] = pd.to_datetime(all_df['order_purchase_timestamp'])
    all_df_2018 = all_df[all_df['order_purchase_timestamp'].dt.year == 2018]
    unique_customers_2018 = all_df_2018[['customer_unique_id', 'customer_city']].drop_duplicates()
    customer_per_city_2018 = unique_customers_2018.groupby('customer_city').size().reset_index(name='total_customers')
    customer_per_city_2018.sort_values(by='total_customers', ascending=False, inplace=True)
    top_5_cities_customers_2018 = customer_per_city_2018.head(5)

    return top_5_cities_customers_2018
def create_top_5_customer_vs_other_cities(all_df):
    all_df['order_purchase_timestamp'] = pd.to_datetime(all_df['order_purchase_timestamp'])
    all_df_2018 = all_df[all_df['order_purchase_timestamp'].dt.year == 2018]
    unique_customers_2018 = all_df_2018[['customer_unique_id', 'customer_city']].drop_duplicates()
    customer_per_city_2018 = unique_customers_2018.groupby('customer_city').size().reset_index(name='total_customers')
    customer_per_city_2018.sort_values(by='total_customers', ascending=False, inplace=True)
    top_5_cities_customers_2018 = customer_per_city_2018.head(5)
    customer_per_city_2018['category'] = customer_per_city_2018['customer_city'].apply(
    lambda x: x if x in top_5_cities_customers_2018['customer_city'].values else 'Other')
    customer_category_2018 = customer_per_city_2018.groupby('category')['total_customers'].sum().reset_index()

    return customer_category_2018
def create_top_5_cities_seller_2018(all_df):
    all_df['order_purchase_timestamp'] = pd.to_datetime(all_df['order_purchase_timestamp'])
    all_df_2018 = all_df[all_df['order_purchase_timestamp'].dt.year == 2018]
    unique_sellers_2018 = all_df_2018[['seller_id', 'seller_city']].drop_duplicates()
    seller_per_city_2018 = unique_sellers_2018.groupby('seller_city').size().reset_index(name='total_sellers')
    seller_per_city_2018.sort_values(by='total_sellers', ascending=False, inplace=True)
    top_5_cities_sellers_2018 = seller_per_city_2018.head(5)

    return top_5_cities_sellers_2018

def create_top_5_seller_vs_other_cities(all_df):
    all_df['order_purchase_timestamp'] = pd.to_datetime(all_df['order_purchase_timestamp'])
    all_df_2018 = all_df[all_df['order_purchase_timestamp'].dt.year == 2018]
    unique_sellers_2018 = all_df_2018[['seller_id', 'seller_city']].drop_duplicates()
    seller_per_city_2018 = unique_sellers_2018.groupby('seller_city').size().reset_index(name='total_sellers')
    seller_per_city_2018.sort_values(by='total_sellers', ascending=False, inplace=True)
    top_5_cities_sellers_2018 = seller_per_city_2018.head(5)
    seller_per_city_2018['category'] = seller_per_city_2018['seller_city'].apply(
    lambda x: x if x in top_5_cities_sellers_2018['seller_city'].values else 'Other')
    seller_category_2018 = seller_per_city_2018.groupby('category')['total_sellers'].sum().reset_index()

    return seller_category_2018


main_df = pd.read_csv("dashboard/all_data.csv")

top_5_cities_customers_2018 =  create_top_5_cities_customers_2018(main_df)
customer_category_2018 = create_top_5_customer_vs_other_cities(main_df)
top_5_cities_sellers_2018 = create_top_5_cities_seller_2018(main_df)
seller_category_2018 = create_top_5_seller_vs_other_cities(main_df)


with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")

st.subheader("Best 5 city customer")

fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#90CAF9"] + ["#D3D3D3"] * (len(top_5_cities_customers_2018) - 1)
sns.barplot(
    x='customer_city',
    y='total_customers',
    data=top_5_cities_customers_2018,
    palette=colors,
    ax=ax
)
ax.set_title("Top 5 Cities with the Most Customers in 2018", loc="center", fontsize=30)
ax.set_ylabel('Number of Customers', fontsize=20)
ax.set_xlabel('City', fontsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Best 5 vs other city customer")

labels_customer = customer_category_2018['category']
sizes_customer = customer_category_2018['total_customers']
colors_customer = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666', '#FFD700']
fig1, ax1 = plt.subplots(figsize=(8, 8))
ax1.pie(sizes_customer, labels=labels_customer, autopct='%1.1f%%', startangle=90, colors=colors_customer)
ax1.axis('equal')
plt.title('Customer Distribution: Top 5 Cities vs Other Cities (2018)', fontsize=16)
st.pyplot(fig1)

st.subheader("Best 5 city seller")
    
fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#90CAF9"] + ["#D3D3D3"] * (len(top_5_cities_sellers_2018) - 1)
sns.barplot(
    x='seller_city',
    y='total_sellers',
    data=top_5_cities_sellers_2018,
    palette=colors,
    ax=ax
)
ax.set_title("Top 5 Cities with the Most Sellers in 2018", loc="center", fontsize=30)
ax.set_ylabel('Number of Sellers', fontsize=20)
ax.set_xlabel('City', fontsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Best 5 vs other city seller")

labels_seller = seller_category_2018['category']
sizes_seller = seller_category_2018['total_sellers']
colors_seller = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666', '#8A2BE2']

fig2, ax2 = plt.subplots(figsize=(8, 8))
ax2.pie(sizes_seller, labels=labels_seller, autopct='%1.1f%%', startangle=90, colors=colors_seller)
ax2.axis('equal') 

plt.title('Seller Distribution: Top 5 Cities vs Other Cities (2018)', fontsize=16)

st.pyplot(fig2)

st.caption('Copyright')
