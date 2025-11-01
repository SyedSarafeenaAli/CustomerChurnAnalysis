# THEORY:-

BINARY CLASSIFICATION: Binary classification is a machine learning task where an algorithm sorts data into one of two possible categories or classes. It is used for problems with a yes/no or true/false outcome, such as identifying if an email is spam or not, determining if a customer will buy a product, or diagnosing a disease. 

SHAP: Shapley Additive exPlanations (SHAP) is a game theory-based method for explaining the output of any machine learning model by assigning a SHAP value to each input feature. These values represent the contribution of each feature to a specific prediction, explaining how it affects the output compared to an expected value (average prediction). SHAP provides both local explanations (for individual predictions) and global explanations (for overall model behavior).  

# PROBLEM STATEMENT:-

Telecom companies face high customer attrition rates, leading to significant revenue loss, as acquiring new customers is often 5-25 times more expensive than retaining existing ones. The challenge is to predict which customers are at risk of churning based on historical data, enabling targeted retention strategies like personalized offers or service improvements. Without such prediction, companies rely on reactive measures, resulting in inefficient resource allocation and missed opportunities to reduce churn rates.

# OBJECTIVE:-

The primary objective is to develop a machine learning model that accurately predicts customer churn probability using demographic, service usage, and account-related features. Secondary goals include identifying the most influential factors driving churn (via feature importance analysis) and achieving a model performance that supports practical deployment, such as integrating predictions into customer relationship management (CRM) systems for real-time interventions.

# DATASET AND FEATURES:-

DATASET:

Source: https://www.kaggle.com/datasets/palashfendarkar/wa-fnusec-telcocustomerchurn

The dataset consists of 7,043 customer records from a telecom provider, spanning 21 columns (including the target variable). Each row represents a single customer, with data anonymized for privacy. The dataset is balanced for analysis but reflects real-world class imbalance (approximately 73% non-churners, 27% churners). No missing values in the target, but some numerical features may require encoding or scaling.

FEATURES

The dataset includes a mix of categorical, numerical, and binary features.

customerID:
A unique alphanumeric identifier assigned to each customer. Not used in modeling (dropped during preprocessing) as it carries no predictive value.

gender:
The gender of the customer. Categorical variable with two values: Male or Female. Helps analyze if churn behavior differs by gender.

SeniorCitizen:
Binary indicator (0 or 1) showing whether the customer is a senior citizen. 1 = Yes, 0 = No. Often a key demographic driver in churn.

Partner:
Indicates whether the customer has a partner (spouse or domestic partner). Values: Yes or No. Customers with partners may show lower churn due to shared services.

Dependents:
Indicates whether the customer has dependents (e.g., children). Values: Yes or No. Presence of dependents often correlates with loyalty and lower churn.

tenure:
Number of months the customer has stayed with the company. Ranges from 0 to 72. One of the strongest predictors — longer tenure typically means lower churn risk.

PhoneService:
Indicates whether the customer has phone service. Values: Yes or No. Customers without phone service may rely only on internet, affecting churn patterns.

MultipleLines:
Specifies if the customer has multiple phone lines. Values: Yes, No, or No phone service. Multiple lines may indicate higher engagement or family usage.

InternetService:
Type of internet service subscribed. Values: DSL, Fiber optic, or No. Fiber optic users often have higher churn due to competition and pricing sensitivity.

OnlineSecurity:
Indicates whether the customer has online security add-on. Values: Yes, No, or No internet service. Add-ons increase perceived value and reduce churn.

OnlineBackup:
Indicates whether the customer uses online backup service. Values: Yes, No, or No internet service. Reflects engagement with additional services.

DeviceProtection:
Indicates whether the customer has device protection plan. Values: Yes, No, or No internet service. Bundled services improve retention.

TechSupport:
Indicates whether the customer has tech support add-on. Values: Yes, No, or No internet service. Lack of support is a known churn driver.

StreamingTV:
Indicates whether the customer streams TV content. Values: Yes, No, or No internet service. High usage of streaming may indicate heavy reliance on internet.

StreamingMovies:
Indicates whether the customer streams movies. Values: Yes, No, or No internet service. Similar to StreamingTV, reflects digital engagement.

Contract:
The type of contract the customer is on. Values: Month-to-month, One year, Two year. Month-to-month contracts have significantly higher churn rates.

PaperlessBilling:
Indicates whether the customer opted for paperless billing. Values: Yes or No. Often associated with tech-savvy users and slightly higher churn.

PaymentMethod:
Customer’s preferred payment method. Values: Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic). Automatic payments reduce churn risk.

MonthlyCharges:
The amount charged to the customer each month (in USD). Ranges from ~$18 to ~$118. Higher charges, especially with fiber, correlate with churn.

TotalCharges:
The total amount charged to the customer over their tenure. Numerical value derived from tenure × monthly charges (with some edge cases). Strong indicator of customer lifetime value.

Churn (Target Variable):
Indicates whether the customer left the company within the last month. Values: Yes (churned) or No (retained). The binary outcome to predict.
