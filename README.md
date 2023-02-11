# Crop Prediction

First download the files all of them in one folder.

Now open them in an IDE. For example if you choose pycharm open them

click on app.py and run it youll get a link with numbers as port
click on the port and you will be directed to the web app like this one

![image](https://user-images.githubusercontent.com/101086033/218281654-b18f8881-47fa-42fa-9c49-d52d5b23fb98.png)

then enter the parameters as per your soil

![image](https://user-images.githubusercontent.com/101086033/218281728-2ab1b596-be72-425f-84d2-9ea2ed7acb86.png)

and click on "predict the crop"

it will not only show you the best crop to be grown here, but it also analyses the maximum price which can be provided for that crop and displays that market and geolocation.

![image](https://user-images.githubusercontent.com/101086033/218281781-75ec7f92-7435-4c23-87a8-b4d1b524d29c.png)

# About the model

Importing dependencies:
The first few lines of code import the required libraries. The libraries used are:
IPython - used to interact with the Python interpreter
pandas - used to load, manipulate and analyze data
numpy - used to perform scientific computing with Python
matplotlib.pyplot - used for data visualization
seaborn - used to create aesthetically pleasing visualizations
sklearn.ensemble - used to implement machine learning algorithms, specifically the Random Forest Classifier in this code
sklearn.preprocessing - used to scale and normalize the data
sklearn.model_selection - used to split the data into training and testing sets
Plotting Boxplots:
The code creates boxplots for three different variables in the data set - 'N', 'P', and 'K'. The plotly.express.px.box method is used to create the plots and the fig.show() method is used to display the plots.

Removing Outliers:
The del_out function is used to remove outliers from the data set. The function takes two arguments - the data set and the variable for which outliers need to be removed. The function first calculates the first quartile (Q1) and third quartile (Q3) of the variable. Then, it calculates the interquartile range (IQR) which is the difference between Q3 and Q1. Finally, the function removes the data points that are outside the range (Q1 - 1.5 * IQR) to (Q3 + 1.5 * IQR).

Correlation Heatmap:
The code then creates a correlation heatmap using the seaborn.heatmap method. The heatmap shows the correlation between the variables in the data set.

Splitting the Data:
The data set is split into training and testing sets using the train_test_split method from the sklearn.model_selection library. The test size is set to 0.3, which means 30% of the data will be used for testing and 70% for training.

Training the Model:
The Random Forest Classifier algorithm is used to train the model. The fit method is used to train the model on the training data.

Making Predictions:
The model is used to make predictions on the test data using the predict method. The accuracy of the model is then evaluated using the accuracy_score method from the sklearn.metrics library.

Plotting the Confusion Matrix:
A confusion matrix is then plotted to visualize the performance of the model. The confusion matrix displays the number of correct and incorrect predictions for each class.

Making a Prediction for a New Data Point:
A function named prediction is defined which takes seven arguments and returns the prediction made by the model for a new data point.

Getting Crop Details:
The get_crop_details function is defined which takes a crop name as an argument and returns details about the crop, such as the correct market and place where the maximum price for that crop is provided.
