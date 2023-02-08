import os
import  pandas as pd
import matplotlib.pyplot as plt
from flask import flash, redirect, url_for
from bert_logic.bertLogic import BertLogic
from datetime import datetime
from database.db_schema import Payload
from app_connector import db
# initializer

class CsvLogic(BertLogic):
    
    def __init__(self):
        # initializing the BertLogic class
        BertLogic.__init__(self)
        
    def check_validity(self,path,is_admin,user_id):
        # storing the path in a variable 
        file_path =  path
        #spliting the path by '.' into a list and saving the output to the check variable
        check = path.split(".")
        #checking if 'csv' is in the of the splited path, this will help us know if it is a csv file.
        if "csv" in check and is_admin == True:
            # if the file is a csv file and it is uploaded by an admin, then the next line of code is to open the file
            data =  self.admin_data_extraction(file_path,user_id)
            return  data
        else:
            # showing an error on the fontend that the file uploaded is not a csv file
            flash("This is not a csv file",category='error')
            # deleting the file
            os.remove(path=file_path)
            return ""
               
    def admin_data_extraction(self,path,user_id):
        try:
            # if the file is a csv file, then the next line of code is to open the file
            # with pandas and saving it to the {data_source👇👇👇} variable 
            data_source = pd.read_csv(path)
            # the next line is to extract each review from the review column in the dataset
            all_reviews = [review[:512] for review in data_source.review if len(review) > 0]
            # the next line is to extract each address from the address column in the dataset
            address = [address for address in data_source.address]
            # the next line is to extract each country from the country column in the dataset
            country = [country for country in data_source.country]
            # the next line is to extract each city from the city column in the dataset
            city = [city for city in data_source.city]
            # the next line is to extract each reting from the rating column in the dataset
            rating = [rating for rating in data_source.rating]
            # the next line is to extract each name from the name column in the dataset
            hotel_names = [name for name in data_source.name] 
            # the next line is to extract each expectation from the expectation column in the dataset
            expectation = [expectation for expectation in data_source.expectation] 
            # the next lines is a dictionary of {key:value} that contains the {rating:impression}, 
            # the key is rating, while the value is the impression 
            impression_dict = {1:"negative",2:"negative",3:"neutral",4:"positive",5:"positive"}
            # the next line is list of impressions. 
            # we compare the ratings colunm in the data_source with the impression_dict key to 
            # get the proper impression. then we add the value to the impression list 
            impression = [impression_dict[i] for i in rating]
            # looping through the review list and passing each review to 
            # to the sequenceClassification methon to get each review classified by our bert model 
            # and adding the result to the bert_impressions list.
            bert_impressions = [self.sequenceClassification(review) for review in all_reviews]
            # creating a dictionary of the extracted data's we will use to create a new csv
            data_format ={
                "name":hotel_names,"country":country,"city":city,"address":address
                ,"hotel.name": hotel_names,"review":all_reviews,"rating":rating,"impression":impression,
                "expectation":expectation,"bert_impression": bert_impressions
            }     
            # using pandas to create a new dataframe
            extracted_data_set = pd.DataFrame(data_format)
            # setting the path and date that the file will be saved as
            dateAndPath = f"static/files/extracted_data_{datetime.now().strftime('%Y_%m_%d-%H_%M')}.csv"
            # using extracted_data_set frame  to create a new csv file and saving it to the static/non/ directory 
            extracted_data_set.to_csv(dateAndPath)
            # calling the confusion_matrics to do is thign and give us our value
            self.confusion_matrics_calculated(dateAndPath)
            # Adding the classifield csv to the database
            self.addToDb(dateAndPath,user_id)
            # Displaying a success message on the frontend 
            flash("Data Extraction Completed Successfully!!.", category="success")
            location = dateAndPath.split("/")
            return f'{location[2]}'
        except:
            # diaplaying an error message for data that are not well formated
            flash("Invalid data format!!\n Your dataset is not properly formated.\n Please follow the guidlines on the page.",category="error")
            # removing the csv file from the system.
            os.remove(path=path) 

    def confusion_matrics_calculated(self,path):
        # reading the csv file with pandas
        data = pd.read_csv(path)
        # looping through the bert_impression column and 
        # adding each impression to a list called impression
        bert_prediction = [impression for impression in data.bert_impression]
        # looping through the expectation column and 
        # adding each impression to a list called correct_impression
        expected_prediction =[expectation for expectation in data.expectation]
        total_correct_review_classified = 0
        for i in range(len(data)):
            if bert_prediction[i] == expected_prediction[i]:
                total_correct_review_classified+=1

        # declearing our formula variables
        TP = 0 
        FN = 0
        FP = 0
        TN = 0
        # the function {checker} compare the information on the right with the information on the left
        # It takes to parameters called label1 and label2
        def checker(label1, label2):
            # declearing a variable called count to keep track of the total pass cases
            count = 0
            # looping through the lenght of the csv data. the index variable increases on 
            # itaration automaticaly 
            for index in range(len(data)):
                # checking each row of the correct_impression to see if it match the label
                # and each row of the bert_impression of the same index to see if the  match the second label
                if expected_prediction[index] == label1 and bert_prediction[index] == label2:
                    # if the above condition pass, we are incrementing count by 1
                    count+=1
            # at the end of the loop i am returning the current value of count. 
            return count
        # checking for TP(True Positive)
        positive_as_positive = checker("positive","positive")
        # checking for FN(False Negative)
        positive_as_neutral =  checker("positive","neutral")
        # checking for FN(False Negative)
        positive_as_negative = checker("positive","negative")
        # checking for TN(True Negative)
        neutral_as_neutral = checker("neutral","neutral")
        # checking for FP(FAlse Positive)
        neutral_as_positive = checker("neutral","positive")
        # checking for TN(True Negative)
        neutral_as_negative = checker("neutral","negative")
        # checking for TN(True Negative)
        negative_as_negative = checker("negative","negative")
        # checking for TN(True Negative)
        negative_as_neutral = checker("negative","neutral")
        # checking for FP(FAlse Positive)
        negative_as_positive = checker("negative","positive")
        # add  each value to the it ancesstor
        TP = positive_as_positive
        FN = positive_as_neutral + positive_as_negative
        FP = negative_as_positive + neutral_as_positive
        TN = neutral_as_neutral + negative_as_neutral + negative_as_negative + neutral_as_negative
        # printing the each value of the fomula variable
        print(f'TP:{TP}, FN:{FN}, FP:{FP}, TN:{TN}')
        print(f'positive_as_positive:{positive_as_positive},')
        print(f'positive_as_neutral:{positive_as_neutral},')
        print(f'positive_as_negative:{positive_as_negative},')
        print(f'negative_as_positive:{negative_as_positive},')
        print(f'neutral_as_positive:{neutral_as_positive},')
        print(f'negative_as_negative:{negative_as_negative},')
        print(f'neutral_as_negative:{neutral_as_negative},')
        print(f'negative_as_neutral:{negative_as_neutral},')
        print(f'neutral_as_neutral:{neutral_as_neutral},')
        # calculating accuracy with the formula
        f1 = (TP + TN )/ (TP + FP + TN + FN)
        precision = TP / (TP + FP)
        recall = TP / (TP + FN)
        accuracy = total_correct_review_classified/len(data)
        print(f'accuracy: {accuracy}')
        print(f'F1: {f1}')
        print(f'precission: {precision}')
        print(f'recall: {recall}')

    def defaultData(self):
        # this part of the code need to run just once
        data = pd.read_csv("static/files/extracted_data_2022_08_25-17_59.csv")
        impression = [impression for impression in data.bert_impression]
        correct_impression =[expectation for expectation in data.expectation]
        hotel_name = [name for name in data.name]
        hotel_country = [country for country in data.country]
        hotel_city = [city for city in data.city]
        hotel_address = [address for address in data.address]

        # Looping through the data and saving it to the database
        for index in range(len(data)):
            add_data =  Payload(
            user_id = 1,    
            name = hotel_name[index].lower(), 
            country= hotel_country[index].lower(), 
            city = hotel_city[index].lower(), 
            address= hotel_address[index].lower(),
            expected_impression= correct_impression[index].lower(),
            bert_impression = impression[index].lower())
            db.session.add(add_data)
            db.session.commit()

    def addToDb(self,path,user_id):
        # this part of the code need to run just once
        data = pd.read_csv(path)
        impression = [impression for impression in data.bert_impression]
        correct_impression =[expectedData for expectedData in data.expectation]
        hotel_name = [name for name in data.name]
        hotel_review = [review for review in data.review]
        hotel_country = [country for country in data.country]
        hotel_city = [city for city in data.city]
        hotel_address = [address for address in data.address]

        # Looping through the data and saving it to the database
        for index in range(len(data)):
            add_data =  Payload(user_id= user_id,
            hotel_name = hotel_name[index].lower(),
            review = hotel_review[index].lower(),
            hotel_country= hotel_country[index].lower(), 
            hotel_city = hotel_city[index].lower(), 
            hotel_address= hotel_address[index].lower(),
            expected_impression= correct_impression[index].lower(),
            bert_impression = impression[index].lower())
            db.session.add(add_data)
            db.session.commit()
         
   
    
