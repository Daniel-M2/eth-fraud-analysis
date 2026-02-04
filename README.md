# Ethereum Fraud Transaction Detectors

## Repository Outline
```
1. README.md - Project Criteria
2. notebook.ipynb - This notebook contains the whole data processing, analysis, and modeling
3. inference.ipynb - This is a notebook for inferencing new data
4. deployment - This file contains the model deployment code on HuggingFace
5. url.txt - This file contains some links to access the dataset, model, and deployment page
```

## Problem Background
Financial fraud & hacking keep happening in the crypto currency industries. In 2024, there were 303 hacking cases with total funds stolen of $2.2 Billion [(Chainanalysis, 2024)]('https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2025/'). Moreover, earlier this year, Bybit (Centralized Exchange) suffered a 400,000 ETH (~ $1.4 Billion) loss from a single hacking case by North Korean hackers, making this incident the largest single theft in the crypto industry's history [(Crystal Intelligence, 2025)]('https://crystalintelligence.com/investigations/the-10-biggest-crypto-hacks-in-history/').


## Project Output
The outpouts of this project are machine learning model (XGBoost Classifier), model deployment (streamlit & hugging face), and inference data.

## Data
The ETH transaction data is taken from [Kaggle]('https://www.kaggle.com/datasets/vagifa/ethereum-frauddetection-dataset') & can be verified on [Etherscan](https://etherscan.io/).
```
- This data contains 9823 rows & 48 columns
- Missing values only occur in ERC-20 transaction columns, with a total of 2717 entries
- The target class proportion is quite imbalanced and most features contain extreme values (outliers)
```

## Method
In detecting fraud transactions, multiple supervised machine learning models are used (KNN, SVC, Decision Tree, Random Forest, & XGBoost) to determine which model predicts better classification in this dataset.



## Stacks
**Programming Language:** Python

**Libraries:**
* Pandas
* Numpy
* Seaborn
* Pyplot
* Scikit-learn
* Phik
* XGBoost
* Streamlit

**Tools:**
* Jupyter Notebook
* HuggingFace
* Python Script

## Reference
- [Crypto Hacks Report]('https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2025/')
- [Top 10 Biggest CEXs Hacks in History]('https://crystalintelligence.com/investigations/the-10-biggest-crypto-hacks-in-history/')
- [MIT Brothers Ethereum Fraud]('https://www.theblock.co/post/378414/prosecutors-seek-new-trial-mit-brothers-25-million-ethereum-fraud-case-ends-mistrial')
- [Faheem U.R.S. (2024)](https://medium.com/@faheemsiddiqi789/how-can-i-determine-if-my-data-is-balanced-or-imbalanced-080819af408c)
- [Schober *et al.,* 2018](https://www.researchgate.net/publication323388613_Correlation_Coefficients_Appropriate_Use_and_Interpretation)

---

**Additional Reference:**
- [ERC-20 Token List](https://etherscan.io/tokens)
- [Ethereum Smart Contract Video](https://www.youtube.com/watch?v=qAgkGOPyLrk)