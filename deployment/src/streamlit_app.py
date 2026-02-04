import streamlit as st
import eda
import predict

st.set_page_config(
    page_title='ETH Fraud Prediction',
    layout= 'wide',
    initial_sidebar_state= 'expanded',
)

navigation = st.sidebar.selectbox('Select Page:',('EDA','Predict a Transaction'))

if navigation == 'EDA':
    eda.run()
elif navigation == 'Predict a Transaction':
    predict.run()