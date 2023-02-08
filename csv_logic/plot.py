from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd


def plot_graph(data):
        # using the pandas libary to read the csv file
        data_source = pd.read_csv(data)
        # getting the total numbers of the data
        total = len(data_source.review)
        # geting the total numbers of positive reviews
        total_positive_in_expectation = len(data_source[data_source.expectation == "positive"])
        # geting the total numbers of negative reviews
        total_negative_in_expectation = len(data_source[data_source.expectation == "negative"])
        # geting the total numbers of neutral reviews
        total_neutral_in_expectation = len(data_source[data_source.expectation == "neutral"])
        # geting the total numbers of positive reviews
        total_positive_in_bertPrediction = len(data_source[data_source.bert_impression == "positive"])
        # geting the total numbers of negative reviews
        total_negative_in_bertPrediction = len(data_source[data_source.bert_impression == "negative"])
        # geting the total numbers of neutral reviews
        total_neutral_in_bertPrediction = len(data_source[data_source.bert_impression == "neutral"])
        # geting the total numbers of positive reviews
        total_positive_in_impressionColunm = len(data_source[data_source.impression == "positive"])
        # geting the total numbers of negative reviews
        total_negative_in_impressionColunm = len(data_source[data_source.impression == "negative"])
        # geting the total numbers of neutral reviews
        total_neutral_in_impressionColunm = len(data_source[data_source.impression == "neutral"])
        # creating a list for the data in the expecration column
        expectedColumn = [total_positive_in_expectation,total_negative_in_expectation, total_neutral_in_expectation]
        # creating a list for the data in the bertPrediction column
        bertPredictionColumn = [total_positive_in_bertPrediction,total_negative_in_bertPrediction, total_neutral_in_bertPrediction]
         # creating a list for the data in the expecration column
        regulerReviewPredictionColumn = [total_positive_in_impressionColunm,total_negative_in_impressionColunm, total_neutral_in_impressionColunm]
        # creting the classification Row data
        classificationRows = ["Positive","Negative","Neutral"]
        print(bertPredictionColumn)
        # Plotting graph 
        plt.bar(classificationRows,bertPredictionColumn,color=["green",'red','grey'])
        # ploting a bar chat from the data parameter
        # data.plot(kind="bar",rot=0,color=["red",'grey','green','white'],ylabel='Numbers of reviews')

        show = plt.show()

        return show

plot_my_graph = plot_graph(f"static/files/extracted_data_2022_08_25-17_59.csv")