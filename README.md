# PROBLEM STATEMENT:-

Telecom companies face high customer attrition rates, leading to significant revenue loss, as acquiring new customers is often 5-25 times more expensive than retaining existing ones. The challenge is to predict which customers are at risk of churning based on historical data, enabling targeted retention strategies like personalized offers or service improvements. Without such prediction, companies rely on reactive measures, resulting in inefficient resource allocation and missed opportunities to reduce churn rates.

# OBJECTIVE:-

The primary objective is to develop a machine learning model that accurately predicts customer churn probability using demographic, service usage, and account-related features. Secondary goals include identifying the most influential factors driving churn (via feature importance analysis) and achieving a model performance that supports practical deployment, such as integrating predictions into customer relationship management (CRM) systems for real-time interventions.

# DATASET AND FEATURES:-

DATASET:

The dataset consists of 7,043 customer records from a telecom provider, spanning 21 columns (including the target variable). Each row represents a single customer, with data anonymized for privacy. The dataset is balanced for analysis but reflects real-world class imbalance (approximately 73% non-churners, 27% churners). No missing values in the target, but some numerical features may require encoding or scaling.

FEATURES

The dataset includes a mix of categorical, numerical, and binary features. Below is a table summarizing the key features:



Feature NameTypeDescriptioncustomerIDCategorical (String)Unique identifier for each customer.genderCategoricalCustomer gender (Male/Female).SeniorCitizenBinary (Integer: 0/1)Indicates if the customer is a senior citizen (1 = Yes).PartnerBinary (Yes/No)Whether the customer has a partner (spouse/domestic).DependentsBinary (Yes/No)Whether the customer has dependents.tenureNumerical (Integer)Number of months the customer has been with the company (0-72).PhoneServiceBinary (Yes/No)Indicates if the customer has phone service.MultipleLinesCategoricalIndicates if the customer has multiple phone lines (Yes/No/No phone service).InternetServiceCategoricalType of internet service (DSL/Fiber optic/None).OnlineBackupBinary (Yes/No)Whether the customer has online backup service.DeviceProtectionBinary (Yes/No)Whether the customer has device protection.TechSupportBinary (Yes/No)Whether the customer has tech support.StreamingTVBinary (Yes/No)Whether the customer streams TV.StreamingMoviesBinary (Yes/No)Whether the customer streams movies.ContractCategoricalContract term (Month-to-month/One year/Two year).PaperlessBillingBinary (Yes/No)Whether billing is paperless.PaymentMethodCategoricalPayment method (Electronic check/Mailed check/Bank transfer/Credit card).MonthlyChargesNumerical (Float)Monthly bill amount ($18.25-$118.75).TotalChargesNumerical (Float)Total charges incurred to date (often derived from tenure * monthly).ChurnBinary (Target: Yes/No)Whether the customer churned (1 = Yes).
