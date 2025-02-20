"""
This file is a local test of NLP techniques applied to a test set of results, which:
    * Extracts the article bodies from the list
    * Applies NLP techniques / analysis
    * Explores other interesting data from results
    *
"""
import json
import os
from pydantic import BaseModel, Field
import spacy
from transformers import pipeline
import os

test_file = r'.\test_requests\apitube\Tesla_20250217_154219.json'
# only positives
test_file = r'.\test_requests\apitube\Google_20250220_160116.json'


class NLPResult(BaseModel):
    body: str = Field(..., min_length=10)
    # sentiment: float = Field(..., ge=0, le=1)
    sentiment_score: float
    sentiment: str
    # entities: list

results_list: list[NLPResult] = []

class NewsProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.sentiment_analyzer = pipeline(task = "sentiment-analysis",
                                           model = "distilbert-base-uncased-finetuned-sst-2-english",
                                           truncation=True)
    
    def process_article(self, article_body):
        doc = self.nlp(article_body)
        # entities = [(ent.text, ent.label_) for ent in doc.ents]
        
        sentiment = self.sentiment_analyzer(article_body)

        return {
            # 'entities': entities,
            'sentiment': sentiment
        }
    
news_processor_worker = NewsProcessor()

## TODO: add sentiment analysis for each found body
with open(test_file, mode='rb') as localfile:
    test_data = json.load(localfile)
    test_results = test_data.get('results', [])
    for result in test_results:
        result_body = result.get('body', '')
        if result_body:
            analysis_result = news_processor_worker.process_article(result_body)
            # entities = analysis_result.get('entities')
            sentiment_list = analysis_result.get('sentiment')
            sentiment = sentiment_list[0].get('label')
            sentiment_score = sentiment_list[0].get('score')
            result_obj = NLPResult(
                body = result_body,
                sentiment_score = sentiment_score,
                sentiment = sentiment,
                # entities = entities
                )
            results_list.append(result_obj)

# saving pydantic models to json
save_path = os.path.join('.', 'test_nlp_results', 'test_tesla_nlp_results.json')
with open(save_path, 'w') as file:
    json.dump([result.model_dump() for result in results_list], file)

# results_list_python = [result.model_dump() for result in results_list]