# calculate average sentiment from the dat
import json
from collections import Counter
import os

file_path = os.path.join('.', 'test_nlp_results', 'test_tesla_nlp_results.json')
file = open(file_path, mode='r')
results_list = json.load(file)

def most_common_sentiment(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]

avg_sentiment = 0
sentiment_scores = []
sentiment_labels = []
# print(type(results_list))
for result in results_list:
    # sentiment = {
    #     'score': results_list.get('sentiment_score'),
    #     'label': results_list.get('sentiment'),
    # }
    # print(type(result))
    sentiment_score = result.get('sentiment_score')
    sentiment_scores.append(sentiment_score)
    sentiment_labels.append(result.get('sentiment'))
    avg_sentiment += sentiment_score

avg_sentiment = avg_sentiment/len(sentiment_scores)
avg_sentiment_label = most_common_sentiment(sentiment_labels)
print(sentiment_scores)
print('*************************')
print(avg_sentiment)
print(avg_sentiment_label)