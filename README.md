# CROP PREDICTION MODEL

This repo contains all the file needed for the proper execution of the application.
Download the files and then use your favourite IDE for example pycharm. In the pycharm open the folder as the project and then, open it.

Click on the app.py to run it. If you are in mac, then there can be an error message regarding port 5000 already in use for which you have to change your browser or disable the "apple reciever" from "sharing in system preferences"

The final output will be like this

![image](https://user-images.githubusercontent.com/101086033/218269204-14a91b90-f6f5-470f-957a-f9e7cb782999.png)

then the user has to enter the parameters of the soil, environment he or she is living in, and press the predict button.
and there will be your output showing the appropriate crop for your soil.

![image](https://user-images.githubusercontent.com/101086033/218269299-24740a92-2071-4eca-ae19-3a1748cfa1b4.png)

![image](https://user-images.githubusercontent.com/101086033/218269319-a5b742d5-f4d2-4525-ad5e-f4a2bc5be9ca.png)

Thank you for your time.
Down below is a detailed explanation of the code I have used.

# ABOUT THE MODEL

This code is a script for crop prediction. The code uses the Random Forest Classifier algorithm from the scikit-learn library for the prediction.

Firstly, the code imports the necessary dependencies and libraries, including Pandas, Numpy, Matplotlib, Seaborn, sklearn.ensemble (RandomForestClassifier), sklearn.preprocessing (StandardScaler), and sklearn.model_selection (train_test_split).

Then the code reads two CSV files "Crop_recommendation.csv" and "price.csv". The first data set will be used for training and testing the model, while the second data set will be used for reference.

The code checks the shape of the data set and removes duplicate values, and then checks for any null values. The data is then visualized using box plots from the Plotly library.

The code includes a function "del_out" to remove outliers from the data. The function takes two arguments: the data set and a string indicating the name of the column to be processed.

The code performs a correlation analysis on the data set, generating a heatmap of feature correlations.

The code then prepares the data for training by splitting it into features (X) and the label (Y).

The code uses the Random Forest Classifier algorithm to fit the data and make predictions on the test data. The accuracy of the model is calculated using the accuracy_score method.

A confusion matrix is created using the confusion_matrix method to visualize the performance of the model. Finally code also displays the prediction result for a single input.
