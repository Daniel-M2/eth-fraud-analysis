import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def run():
    # Create a Title
    st.title('Ethereum Fraud Transcations Detector')
    # Sub Header
    st.subheader('Exploratory Data Analysis of Ethereum Transaction')

    # Add image
    st.image('https://i-invdn-com.investing.com/news/Ethereum_800x533_L_1556445201.jpg',
             caption= 'Source: Investing.com')
    
    # Add Text
    st.write('This page is written by **Daniel Miarsa**')
    st.write("Below is the sample of crypto transacation made by unique wallet addresses on Ethereum blockchain up to 2019 and can be verified on [Etherscan]('https://etherscan.io/'). For further columns information, please kindly check the data on [Kaggle]('https://www.kaggle.com/datasets/vagifa/ethereum-frauddetection-dataset').")

    # Show df
    df = pd.read_csv('./src/transaction_dataset.csv')
    df.drop(columns=['Unnamed: 0','Index'], inplace=True)
    df.columns = df.columns.str.strip()
    st.dataframe(df)
    
    # Short df explanation
    st.write('##### `FLAG` is the label to indicate which wallet is suspicious towards fraudulent activity')
    st.write('* `0` = `Safe Transaction`')
    st.write('* `1` = `Fraud Transaction`')

    # Pie Chart
    st.write('### Safe & Fraud Transaction Data Proportion')
    fig = px.pie(df, names='FLAG')
    st.plotly_chart(fig,)
    st.write('There are 20% fraud transactions in this dataset.')

    # Histogram
    st.write('### Data Distributions')
    cols = df.columns.to_list()
    option = st.selectbox('### Select Column:',cols, index=4)
    fig = plt.figure(figsize=(16,8))
    sns.histplot(df[option], bins=60, kde=True)
    st.pyplot(fig)

    ##### Filter categorical columns null, empty, & '0' values
    a = df.iloc[:, -2:].dropna()
    a_filtered = a[~(a.iloc[:,-2:].isin([' ','0','', "''"]).any(axis=1))]
    
    # Filter top 10 most popular ERC-20 Tokens
    a_0 = a_filtered.iloc[:,0].value_counts().head(10)
    a_1 = a_filtered.iloc[:,1].value_counts().head(10)

    # Barplot - Most SENT
    st.write('### Top 10 Most Sent ERC-20 Tokens')
    fig = plt.figure(figsize=(10,10))
    sns.barplot(data=a_0,orient='h', color='r')
    st.pyplot(fig)

    # Barplot - Most RECEIVED
    st.write('### Top 10 Most Received ERC-20 Tokens')
    fig = plt.figure(figsize=(10,10))
    sns.barplot(data=a_1,orient='h', color='b')
    st.pyplot(fig)

    st.write("According to the dataset, the top 3 most popular ERC-20 tokens are EOS, OmiseGO, and Golem. However, these coins aren't popular anymore or even some tokens on those list might have gone or not exist in this era.")

if __name__ == '__main__':
    run()
