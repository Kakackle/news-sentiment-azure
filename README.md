# News API ETL project with sentiment analysis, streamlit graphs etc
## Desired Project diagram
![project diagram](project_diagram\Project_diagram.png)
## Desired Project outline:
* Streamlit on Azure web apps website showing graphs of number of articles and average sentiment for a few selected companies per day
* Airflow with docker on azure container instances running daily to get data from API, run simple NLP (sentiment analysis from NLTK is enough) and save results
* Either SQL db or blob storage (cheaper) for results of API and combined NLP results (counts of articles, average sentiment)

## Initial project differences
1. Skip airflow and just use Azure functions to do all the tasks - Airflow scheduling requires extra development configurations

## Aspects to determine:
* SQL or blob? SQL - easier for querying, makes sense to append new rows by date, but more expensive on Azure. Blob - significantly cheaper, have to store results in separate files or append to a file
* Streamlit - just 4 graphs?
* Streamlit - will it autoupdate when the user opens the page? Should, it just reads the data from the specified source, so no need for Azure Functions etc
* Scanning for new articles daily - a container being launched till the job gets finished and the data updated?

## Possible extensions:
* Make data available through an API? Azure Functions with FastAPI to make a simple Swagger app?
* Use Kafka somehow? For real-time / streaming integration, maybe by including graphs of stock prices along with the sentiments - but how? You’d need a producer and a consumer, so you’d need to start a producer somewhere (container instance) when the website is open which can get expensive
* Option for user to add new company / run a script to determine the sentiment on a company of choice - when clicked in app would launch an Azure Function / Logic App to do the API request and NLP tasks and return to user? Or save to separate folder in blob for user requests
* Email alerts when number of articles / sentiment is low - where? in web app? In Airflow container? Logic app when saving to blob that would check for conditions?

## What would it showcase:
* Airflow
* Docker and container management
* Streamlit
* Storage practices

## Initial steps to take
* Experiment with API locally - limitations etc, figure out the companies
* Experiment with NLP and aggregations locally
* Create appropriate structure for data in blob/sql - raw results, NLP resutls etc?
* Start saving results to cloud
* Create Airflow scripts to run the above tasks
* Create a streamlit app locally, connecting to cloud storage
* Make it interactive, clean
* Experiment with deploying app, costs etc
* Add API feature?

# Important considerations
### ALTERNATIVE APIs:
* https://apitube.io/en-pl/pricing - no mention of CORS
* https://www.thenewsapi.com/pricing - no mention of cors but only 3 per request?
* https://newsapi.ai/plans - free but max 2000 requests lifetime?
* https://newsapi.org/ - CORS may prevent container isntances / not localhost, 100 req / day

### If encountering SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)')
need to install certifi and extend python's cert file .pem with API certificates
https://stackoverflow.com/questions/51925384/unable-to-get-local-issuer-certificate-when-using-requests

### If ...