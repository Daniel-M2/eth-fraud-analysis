import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load File
with open('./src/best_xgb.pkl', 'rb') as file_1:
  best_xgb = pickle.load(file_1)

def run():
  st.write("# Is this wallet address safe? Let's Find Out!!")
  st.write('### Input your data here:')

  # Create a form
  with st.form(key='Form Parameters'):
    address = st.text_input('Wallet Address:',value='0x396343362be2A4dA1cE0C1C210945346fb82Aa49')
    avg_min_sent = st.number_input('Avg Between Sent Transactions (min.):', value=3000,help='Average gap time between SENT transactions of a wallet address in minutes')
    avg_min_received = st.number_input('Avg Between Received Transactions (min.):',value=830, help='Average gap time between RECEIVED transactions of a wallet address in minutes')
    time_diff = st.number_input('Time Difference between first & last transaction (min.):', value=468000.63,help='The distance between a wallet address first transaction & last transaction')
    
    st.markdown('---')
    
    sent_tnx = st.number_input('Total Sent Transactions (Cummulative):',value=1352)
    rec_tnx = st.number_input('Total Received Transactions (Cummulative):',value=121)
    create_con = st.number_input('Total Smart Contract Transactions (Cummulative):',value=2)
    
    st.markdown('---')    
    
    unique_rec_address = st.slider('Have RECEIVED from (...) unique wallet address:', min_value =0, value=30, max_value=20000, key='unique_rec_address')
    unique_sent_address = st.slider('Have SENT to (...) unique wallet address:',  min_value =0, value=2, max_value=20000, key='unique_sent_address')
    
    st.markdown('---')    
    st.write('#### Recevied')
    min_val_rec = st.number_input('Minimum value RECEIVED (ETH) in a single transaction:', help='in ETH equivalent')
    max_val_rec = st.number_input('Maximum value RECEIVED (ETH) in a single transaction:', help='in ETH equivalent')
    avg_val_rec = st.number_input('Average value RECEIVED (ETH) in a single transaction:', help='in ETH equivalent')
    
    st.write('#### Sent')
    min_val_sent = st.number_input('Minimum value SENT (ETH) in a single transaction:', help='in ETH equivalent')
    max_val_sent = st.number_input('Maximum value SENT (ETH) in a single transaction:', help='in ETH equivalent')
    avg_val_sent = st.number_input('Average value SENT (ETH) in a single transaction:', help='in ETH equivalent')

    st.write('#### Sent to Contract')
    min_val_sent_con = st.number_input('Minimum value SENT to SMART CONTRACT (ETH) in a single transaction:', help='in ETH equivalent')
    max_val_sent_con = st.number_input('Maximum value SENT to SMART CONTRACT (ETH) in a single transaction:', help='in ETH equivalent')
    avg_val_sent_con = st.number_input('Average value SENT to SMART CONTRACT (ETH) in a single transaction:', help='in ETH equivalent')

    st.markdown('---')

    tot_trx = st.number_input('Count Transaction of a Wallet Address (Cummulative):', value=1, help='Measure how many transactions have been made from a wallet')
    tot_eth_sent = st.number_input('Total ETH Sent to other wallets (Cummulative):')
    tot_eth_rec = st.number_input('Total ETH Received from other wallets (Cummulative):')
    tot_eth_sent_con = st.number_input('Total ETH Sent to SMART CONTRACT (Cummulative):')
    final_balance = st.number_input('Current ETH balance of a wallet address', help='Total ETH Received - Total ETH Sent - Total ETH Sent to contract')

    st.markdown('---')
    st.write('#### ERC-20 Transcations')

    tot_ERC20_trx = st.number_input('Count of ERC-20 Tokens Transactions (Cummulative):', value=0, key='tot_ERC20_trx')
    ERC20_eth_rec = st.number_input('Total ERC-20 Token Received (Cummulative):', help='in ETH equivalent equivalent')
    ERC20_eth_sent = st.number_input('Total ERC-20 Token Sent (Cummulative):', help='in ETH equivalent equivalent')
    ERC20_eth_sent_con = st.number_input('Total ERC-20 Token Sent to Smart Contract (Cummulative):', help='in ETH equivalent equivalent')

    ERC20_unique_sent_address = st.number_input('Have SENT to (...) unique wallet address:', value=0, key='ERC20_unique_sent_address')
    ERC20_unique_rec_address = st.number_input('Have RECEIVED from (...) unique wallet address:', value=0, key='ERC20_unique_rec_address')
    ERC20_unique_sent_con_ad = st.number_input('Have SENT to (...) unique SMART CONTRACT address:', value=0, key='ERC20_unique_sent_con_ad')
    ERC20_unique_rec_con_ad = st.number_input('Have RECEIVED from (...) unique SMART CONTRACT address:', value=0, key='ERC20_unique_rec_con_ad')

    st.markdown('---')
    st.write('#### Time Gap')
    ERC20_avg_min_sent = st.number_input('Avg between Sent Transactions (min.):', value=0.00, key='ERC20_avg_min_sent', help='Average gap time between SENT transactions of a wallet address in minutes')
    ERC20_avg_min_rec = st.number_input('Avg between Received Transactions (min.):', value=0.00, key='ERC20_avg_min_rec',help='Average gap time between RECEIVED transactions of a wallet address in minutes')
    ERC20_avg_min_sent_con = st.number_input('Avg between Sent Transactions to SMART CONTRACT (min.):', value=0.00,key='ERC20_avg_min_sent_con',help='Average gap time between SENT transactions of a wallet address in minutes')
    ERC20_avg_min_rec_con = st.number_input('Avg between Received Transactions from SMART CONTRACT (min.):', value=0.00,key='ERC20_avg_min_rec_con', help='Average gap time between RECEIVED transactions of a wallet address in minutes')

    st.markdown('---')
    st.write('#### Recevied')
    ERC20_min_val_rec = st.number_input('Minimum value RECEIVED (ETH) in a single transaction:', value=0.00, help='in ETH equivalent', key='ERC20_min_val_rec')
    ERC20_max_val_rec = st.number_input('Maximum value RECEIVED (ETH) in a single transaction:', value=0.00, help='in ETH equivalent', key='ERC20_max_val_rec')
    ERC20_avg_val_rec = st.number_input('Average value RECEIVED (ETH) in a single transaction:', value=0.00, help='in ETH equivalent', key='ERC20_avg_val_rec')

    st.write('#### Sent')
    ERC20_min_val_sent = st.number_input('Minimum value SENT (ETH) in a single transaction:', value=0.00, help='in ETH equivalent', key='ERC20_min_val_sent')
    ERC20_max_val_sent = st.number_input('Maximum value SENT (ETH) in a single transaction:', value=0.00, help='in ETH equivalent', key='ERC20_max_val_sent')
    ERC20_avg_val_sent = st.number_input('Average value SENT (ETH) in a single transaction:', value=0.00, help='in ETH equivalent', key='ERC20_avg_val_sent')

    st.write('#### Sent to Smart Contract')
    ERC20_min_val_sent_con = st.number_input('Minimum value SENT to SMART CONTRACT (ETH) in a single transaction:', value=0.00, help='in ETH equivalent', key='ERC20_min_val_sent_con')
    ERC20_max_val_sent_con = st.number_input('Maximum value SENT to SMART CONTRACT (ETH) in a single transaction:', value=0.00, help='in ETH equivalent', key='ERC20_max_val_sent_con')
    ERC20_avg_val_sent_con = st.number_input('Average value SENT to SMART CONTRACT (ETH) in a single transaction:', value=0.00, help='in ETH equivalent', key='ERC20_avg_val_sent_con')

    st.markdown('---')
    st.write('#### Unique Address Count')
    tot_uniq_token_sent = st.slider('Count of unique ERC-20 Token Name SENT to other address (Cummulative):',min_value=0, value=4, max_value=1000)
    tot_uniq_token_rec = st.slider('Count of unique ERC-20 Token Name RECEIVED to other address (Cummulative):',min_value=0, value=6, max_value=1000)

    st.markdown('---')
    st.write('#### Token Names')
    sent_list = ['EOS', 'OmiseGO','Golem','blockwell.ai KYC Casper Token', 'StatusNetwork','BAT', 'Qtum','Bancor','Reputation','Tronix','Others','Unknown']
    rec_list = ['OmiseGO','Blockwell say NOTSAFU', 'DATAcoin','Livepper Token','EOS','XENON','Golem','GSENetwork','Tronix','blockwell.ai KYC Casper Token','Others','Unknown']

    ERC20_sent_name = st.selectbox('ERC-20 Token Name:', sent_list)
    ERC20_rec_name = st.selectbox('ERC-20 Token Name:', rec_list)

    submit = st.form_submit_button('Predict')

    data = {'Address': address,
    'Avg min between sent tnx': avg_min_sent,
    'Avg min between received tnx': avg_min_received,
    'Time Diff between first and last (Mins)': time_diff,
    'Sent tnx': sent_tnx,
    'Received Tnx': rec_tnx,
    'Number of Created Contracts': create_con,
    'Unique Received From Addresses': unique_rec_address,
    'Unique Sent To Addresses': unique_sent_address,
    'min value received': min_val_rec,
    'max value received': max_val_rec,
    'avg val received': avg_val_rec,
    'min val sent': min_val_sent,
    'max val sent': max_val_sent,
    'avg val sent': avg_val_sent,
    'min value sent to contract': min_val_sent_con,
    'max val sent to contract': max_val_sent_con,
    'avg value sent to contract': avg_val_sent_con,
    'total transactions (including tnx to create contract':tot_trx,
    'total Ether sent': tot_eth_sent,
    'total ether received': tot_eth_rec,
    'total ether sent contracts': tot_eth_sent_con,
    'total ether balance': final_balance,
    'Total ERC20 tnxs': tot_ERC20_trx,
    'ERC20 total Ether received': ERC20_eth_rec,
    'ERC20 total ether sent': ERC20_eth_sent,
    'ERC20 total Ether sent contract': ERC20_eth_sent_con,
    'ERC20 uniq sent addr': ERC20_unique_sent_address,
    'ERC20 uniq rec addr': ERC20_unique_rec_address,
    'ERC20 uniq sent addr.1': ERC20_unique_sent_con_ad,
    'ERC20 uniq rec contract addr': ERC20_unique_rec_con_ad,
    'ERC20 avg time between sent tnx': ERC20_avg_min_sent,
    'ERC20 avg time between rec tnx': ERC20_avg_min_rec,
    'ERC20 avg time between rec 2 tnx': ERC20_avg_min_rec_con,
    'ERC20 avg time between contract tnx': ERC20_avg_min_sent_con,
    'ERC20 min val rec': ERC20_min_val_rec,
    'ERC20 max val rec': ERC20_max_val_rec,
    'ERC20 avg val rec': ERC20_avg_val_rec,
    'ERC20 min val sent': ERC20_min_val_sent,
    'ERC20 max val sent': ERC20_max_val_sent,
    'ERC20 avg val sent': ERC20_avg_val_sent,
    'ERC20 min val sent contract': ERC20_min_val_sent_con,
    'ERC20 max val sent contract': ERC20_max_val_sent_con,
    'ERC20 avg val sent contract': ERC20_avg_val_sent_con,
    'ERC20 uniq sent token name': tot_uniq_token_sent,
    'ERC20 uniq rec token name': tot_uniq_token_rec,
    'ERC20 most sent token type': ERC20_sent_name,
    'ERC20_most_rec_token_type': ERC20_rec_name}
    
    inf_data = pd.DataFrame([data])
    st.write('Input Recap:')
    st.dataframe(inf_data)

    if submit:
        # Predict using XGBoost Classifier
        y_pred_inf = best_xgb.predict(inf_data)
        if y_pred_inf == 1:
          answer = 'FRAUD'
        else:
          answer = 'SAFE'
        st.write(f'### Wallet Addres "{address}" is', answer)

if __name__ == '__main__':
  run()