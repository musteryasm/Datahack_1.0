
<img src="Today.png" width="1000"> </img>

### Overview

This project comprises three Jupyter Notebooks, each playing a vital role in data preprocessing, feature selection, and predictive modeling. Alongside, there's a ChatBox and a user-friendly website to enhance the overall user experience.

---

#### (I) Data Preprocessing: "DataHack_PreProcessing.ipynb"

In this notebook, we perform essential data preprocessing tasks to prepare the dataset for thorough analysis. The process unfolds as follows:

- **Handling Missing Values:** We diligently identify and address any missing data points within the dataset to ensure data integrity.

- **Filtering Negative Values:** Rows containing negative values are filtered out to maintain data quality and consistency.

- **Data Cleansing:** We eliminate irrelevant values such as "ALL IN ONE SAVORY," "CCard Convenience," "Staff Discount," "Cake Cutting Charge," etc., streamlining the dataset for analysis.

- **Label Encoding:** To facilitate further analysis, we perform label encoding on the "client_id" and "order_id" columns.

---

#### (II) Feature Selection: "Datahack_FeatureSelection.ipynb"

In this notebook, we focus on feature selection and creating meaningful clusters for analysis. The pivotal steps include:

- **Creating Clusters:** We create clusters for the "order_id" column, allowing us to group similar items ordered by customers. This step enhances the depth of our analysis.

---

#### (III) Predictive Modeling: "Datahack_Model.ipynb"

In this notebook, we harness the power of the Apriori algorithm for data mining. The Apriori algorithm identifies frequent itemsets in the dataset by iteratively extending smaller itemsets until no more frequent itemsets can be found. Key highlights include:

- **Frequent Itemset Mining:** Leveraging the Apriori algorithm, we unearth frequent itemsets within the data, providing valuable insights for predictive modeling.

- **Output Prediction:** Using the algorithmic insights, this notebook enables us to make predictions based on user input, enhancing decision-making.

---

#### (IV) ChatBox

**Food Item Recommendations:** Our ChatBox is equipped to recommend food items based on customer preferences. Leveraging collaborative filtering, it predicts preferences by analyzing the choices of similar users. While this is a powerful feature, building an effective recommendation system requires substantial data and resources.

---

#### (V) Website

Our static website is designed to provide an engaging user interface. It showcases essential information about restaurants and features an integrated ChatBox for user interaction. The website offers a seamless experience for users seeking information or recommendations related to food.

---

### Getting Started

To begin exploring this project, you can follow these steps:

1. Clone this repository to your local machine.
2. Access the Jupyter Notebooks for data preprocessing, feature selection, and modeling.
3. Explore the ChatBox for food recommendations.
4. Visit the website to access static information and interact with the ChatBox.

### Dependencies

This project relies on various libraries and tools, including but not limited to:

- Python
- Jupyter Notebook
- Scikit-Learn
- Pandas
- NumPy
- ChatBot Framework
- HTML/CSS/JavaScript (for the website)

Please ensure you have these dependencies installed to run the project effectively.

### Contributing

We welcome contributions and enhancements to this project. If you have suggestions, bug fixes, or additional features to propose, please open an issue or submit a pull request.
