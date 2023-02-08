# we are going to be using a pre-trained nlp module
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
# touch
'''
we are going to use the argmax function form touch to be able to extract
our high sequence result 
'''
# transformers
""" 
the autoTokenizer will allow us to pass in a string<review> and convert that to a 
sequence of numbers, that we can then pass to our nlp model. & 
AutomodelforSequenceClassification  is going to give us the architecture to
be able to load in our nlp model
"""

class BertLogic:
    def __init__(self): 
        
        # finiteautomata/bertweet-base-sentiment-analysis
        # philschmid/distilbert-base-multilingual-cased-sentiment-2
        # # Instantiating Model
        # self.tokenizer = AutoTokenizer.from_pretrained('finiteautomata/bertweet-base-sentiment-analysis',add_prefix_space=True)
        # self.model = AutoModelForSequenceClassification.from_pretrained('finiteautomata/bertweet-base-sentiment-analysis')
        self.tokenizer = AutoTokenizer.from_pretrained('Teeto/reviews-classification',add_prefix_space=True)
        self.model = AutoModelForSequenceClassification.from_pretrained('Teeto/reviews-classification')


    def  sequenceClassification(self, data):
        try:
            tokenize_data = self.tokenizer(data,truncation = True,max_length= 512, padding = True, return_tensors='pt')
            with torch.no_grad():
                # unpacking the data into model's, because we are using pytorch we need to add ** to unpack the
                # dictionary of tokens
                store_model = self.model(**tokenize_data)
                # we went over all encoders’ states to test target and 
                # source states to return up with scores for each state in encoders. Then we could use softmax to normalize all scores, 
                # which generates the probability distribution conditioned on the right track states.
                get_logit = torch.softmax(store_model.logits, dim=1)
                # using the argmax to get the highest token probability
                get_all_label = torch.argmax(get_logit,dim=1)
                # getting the label
                store_label = [self.model.config.id2label[id] for id in get_all_label.tolist()]
                print(store_label[0].lower())
                # returning the list of all bert impressions on the dataset
                return store_label[0].lower()
        except:
            return "None"


