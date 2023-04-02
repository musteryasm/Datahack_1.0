The project consists of three Jupyter Notebooks: "DataHack_PreProcessing.ipynb", "Datahack_FeatureSelection.ipynb", and "Datahack_Model.ipynb".

(I)In "DataHack_PreProcessing.ipynb", the dataset is pre-processed to prepare it for analysis. The first step is to check for missing values in the dataset. Next, the rows that contain negative values are dropped. Then, unnecessary values such as "ALL IN ONE SAVORY", "CCard Convenience", "Staff Discount", "Cake Cutting Charge", etc. are removed. Finally, label encoding is performed on the "client_id" and "order_id" columns. This ensures that only the relevant data is used for further analysis.

(II)In "Datahack_FeatureSelection.ipynb", a cluster is created for the "order_id" column. This is done to group together similar items that are ordered by customers. This allows for more meaningful analysis to be conducted.

(III)In "Datahack_Model.ipynb", the Apriori algorithm is used for data mining. The algorithm identifies frequent itemsets in a dataset by iteratively extending smaller itemsets until no more frequent itemsets can be found. The algorithm is based on the observation that if an itemset is frequent, then all of its subsets must also be frequent. Based on this algorithm, the notebook is used to predict the output label based on the user input.
