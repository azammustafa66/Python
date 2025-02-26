# CarDekho Price Prediction

## 📌 Project Overview

This project focuses on analyzing and predicting the selling prices of used cars listed on **CarDekho**. Using **Python, Pandas, Seaborn, and Scikit-Learn**, the dataset undergoes **data cleaning, exploratory data analysis (EDA), feature engineering, and model training** to build an effective price prediction model.

## 🔧 Technologies Used

- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **Scikit-Learn** (Linear Regression, Train-Test Split, Evaluation Metrics)
- **Jupyter Notebook** for analysis and visualization

## 📂 Dataset Information

The dataset contains **15,411 records** of used cars with key attributes such as:

- **Vehicle Specifications**: Brand, Model, Age, Mileage, Engine Power
- **Market Factors**: Seller Type, Fuel Type, Transmission Type
- **Target Variable**: Selling Price

## 🛠️ Data Processing & Feature Engineering

1. **Data Cleaning**:
   - Removed unnecessary columns and missing values
   - Replaced incorrect seat values using dataset references
2. **EDA (Exploratory Data Analysis)**:
   - Univariate & Bivariate analysis to identify correlations
   - Distribution of categorical and numerical variables
3. **Feature Selection**:
   - Identified most influential features: **Engine Capacity, Max Power, Vehicle Age**
   - Dropped less impactful features (e.g., Seats, Km Driven)

## 🤖 Model Training & Evaluation

- **Model Used**: Linear Regression
- **Train-Test Split**: 80-20% ratio
- **Performance Metrics**:
  - **R² Score**: 0.67 (Explains 67% of variance in selling price)
  - **MAE**: ₹2.78L (Average prediction error)
  - **RMSE**: ₹4.98L (Prediction deviation)

## 📊 Visualizations

- **Feature Correlation**: Understanding impact on selling price
- **Actual vs. Predicted Prices**: Assessing model performance
- **Price Distribution**: Identifying high-variance cases

## 🚀 Future Improvements

- Implement **advanced ML models** like Random Forest or XGBoost
- Perform **hyperparameter tuning** for better accuracy
- Incorporate **additional market factors** affecting car prices

## 🏁 Conclusion

This project provides a **data-driven approach to predicting used car prices**, leveraging **EDA, feature engineering, and machine learning** to build a moderately accurate regression model. Future iterations can enhance prediction reliability using more sophisticated models and fine-tuned parameters.

---

**👨‍💻 Developed by:** Azam
📅 **Date:** February 2025
