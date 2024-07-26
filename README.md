In this simulation environment, the task was to write a Pyhton program to parse through a massive data set, extracting key elements for the purpose of fraud analysis. 
This documentation provides a guide for analyzing the 'transactions.csv' dataset, a subset of the PaySim mobile money simulation dataset.
The dataset is originally part of the research conducted by E. A. Lopez-Rojas, A. Elmir, and S. Axelsson in their paper 
"PaySim: A financial mobile money simulator for fraud detection" presented at the 28th European Modeling and Simulation Symposium (EMSS) in 2016.

Step 1: Load the Dataset

  Read the dataset into a Pandas dataframe. The first row of the CSV contains the column names.

Step 2: Perform Analysis Tasks

2.1 Return the Column Names

  Retrieve the column names from the dataframe as a list.

2.2 Return the First 'k' Rows

  Get the first 'k' rows from the dataframe.

2.3 Return a Random Sample of 'k' Rows

  Fetch a random sample of 'k' rows from the dataframe.

2.4 Return a List of Unique Transaction Types

  Extract a list of unique transaction types.

2.5 Return the Top 10 Transaction Destinations with Frequencies

  Get a Pandas series of the top 10 transaction destinations with their frequencies.

2.6 Return Rows with Detected Fraud

  Retrieve all rows where fraud was detected.

2.7 Return Number of Distinct Destinations per Source

  Get a dataframe with the number of distinct destinations each source has interacted with, sorted in descending order.
  

Visualization Tasks


Visualization 1: Transaction Types Bar Chart

  Create bar charts for transaction types and transaction types split by fraud.

Visualization 2: Scatter Plot for Cash Out Transactions

  Create a scatter plot for origin account balance delta vs. destination account balance delta for Cash Out transactions.
  

Conclusion


The provided functions and visualizations offer a structured approach to analyzing the 'transactions.csv' dataset.
These tools help in understanding the data distribution, detecting fraud patterns, and identifying potential anomalies,
contributing to effective fraud detection and prevention strategies.
