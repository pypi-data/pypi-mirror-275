#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nbformat
import codecs
import numpy as np
from sklearn.metrics import precision_score, recall_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt   
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from  nbconvert.exporters import HTMLExporter
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor 
from ydata_profiling import ProfileReport
import statsmodels.api as sm
import statsmodels.formula.api as smf
def func(file_loc,header_row_number=0):

    if header_row_number==0: 
        df=pd.read_csv(file_loc)
        
    else:
        df=pd.read_csv(file_loc,header=header_row_number)
    print(df.head(3))
        # Data Cleaning & Exploratory Analysis
             # Identify categorical and continuous variables
    categorical_vars = df.select_dtypes(include=['object']).columns

            
    continuous_vars = df.select_dtypes(exclude=['object']).columns
    # Check for missing values in each column
    missing_values = df.isnull().any()
    if str(missing_values[missing_values].index.tolist())!='[]':
            # Display the result
        print("\nColumns with Missing Values:")
        print(missing_values[missing_values].index.tolist())

        # Example: Histogram for a numerical column
    for j in continuous_vars:
        sns.histplot(df[j], bins=20)
        plt.title('Distribution of Numerical Column')
        plt.show()

        # Example: Countplot for a categorical column
    for i in categorical_vars:
        sns.countplot(x=i, data=df)
        plt.title('Count of Each Category in Categorical Column')
        plt.show()
    for i in categorical_vars:
        df[i] = df[i].astype('category').cat.codes
    correlation_matrix = df.corr()

    # Set up the matplotlib figure
    plt.figure(figsize=(10, 8))

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")

    # Add title and rotate x-axis labels
    plt.title('Correlation Heatmap')
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)

    # Display the plot
    plt.tight_layout()
    plt.show()
    
    target=str(input('\nFrom the list of columns to choose from: '+str(df.columns)
                     +'\n Specify which column that you want to use as target variable: \n'))
    id_col=str(input(' If there is an ID column you would like to exclude from analysis'+ 
                     ', please specify the ID column: '+
                    'If not, press Enter'))
    if id_col in df.columns:
        X = df.drop([target,'Site','season','year'], axis=1).drop(id_col,axis=1)
        y = df[target]
    else:
        X = df.drop(target, axis=1)
        y = df[target]
    # VIF dataframe 
    vif_data = pd.DataFrame() 
    vif_data["feature"] = X.columns 

    # calculating VIF for each feature 
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) 
                              for i in range(len(X.columns))] 

    print(vif_data)
        # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Display the shapes of the resulting datasets
    print("Training set shape:", X_train.shape, y_train.shape)
    print("Testing set shape:", X_test.shape, y_test.shape)
 

        # Replace 'your_target_column' with the actual column you're trying to predict
        # Replace 'your_n_estimators' with the desired number of trees in the forest
        # Replace other hyperparameters based on your specific requirements
    inp=input('Which ML model would you like to perform? Enter C for Classification, R for Regression' + 
              ', SR for OLS Regression')
    if inp.upper()=='C':
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
                # Train the Random Forest model
        clf.fit(X_train, y_train)

            # Make predictions on the test set
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", accuracy)
        precision = precision_score(y_test, y_pred,average='micro')
        recall = recall_score(y_test, y_pred,average='micro')

        print("Precision:", precision)
        print("Recall:", recall)

            # Draw a confusion matrix
        conf_matrix = confusion_matrix(y_test, y_pred)

            # Create a heatmap for the confusion matrix
        plt.figure(figsize=(8, 6))
        sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False
                    #,xticklabels=['Predicted 0', 'Predicted 1'],yticklabels=['Actual 0', 'Actual 1']
                   )
        plt.xlabel('Predicted Label')
        plt.ylabel('True Label')
        plt.title('Confusion Matrix')
        plt.show()
    elif inp.upper()=='R':
        clf=RandomForestRegressor(random_state=42)
        clf.fit(X_train, y_train)
        # Make predictions on the test set
        y_pred = clf.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        print("Mean Squared Error "+ str(mse))
        r2 = r2_score(y_test, y_pred)
        print("R ^2 "+ str(r2))

    elif inp.upper()=='SR':
        
 

        # Fit the OLS (Ordinary Least Squares) regression model
        clf = sm.OLS( y_train,X_train).fit()

        # Print the summary of the regression model
        print(clf.summary())

        # Evaluate the model performance
        


        # You can further explore other metrics or perform hyperparameter tuning as needed


        # Assuming you've already trained the Random Forest model (clf) and made predictions (y_pred)

        # Calculate precision and recall

        # Assuming 'id' is the name of your ID column
    id_column = y_test[id_col]

        # Create a DataFrame with the IDs and corresponding predictions
    prediction_df = pd.DataFrame({'ID': id_column, 'prediction': y_pred})

        # Merge the prediction DataFrame with the original DataFrame on the 'id' column
    result_df = pd.concat([df, prediction_df],ignore_index=True )

        # Display the resulting DataFrame
        # Save the prediction result to a CSV file
    prediction_df.to_csv('prediction_result.csv', index=False)
    print("Prediction output is stored in prediction_result.csv")
        # Save the complete result to a CSV file
    #result_df.to_csv('complete_prediction_result.csv', index=False)
    notebook_name = 'Open Source Library work.ipynb'
    output_file_name = 'output.html'

    exporter = HTMLExporter()
    output_notebook = nbformat.read(notebook_name, as_version=4)

    output, resources = exporter.from_notebook_node(output_notebook)
    codecs.open(output_file_name, 'w', encoding='utf-8').write(output)
    print("Your file containing the output is stored in output.html")

