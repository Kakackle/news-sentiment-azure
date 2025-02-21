# Important links and resources as to how to do things
### Run Container Instances on a schedule
1. https://stackoverflow.com/questions/73204957/scheduling-start-of-a-container-in-azure-container-apps - use azure functions or logic apps to instantiate and close the instance OR just use functions?
2. https://learn.microsoft.com/en-us/azure/container-apps/jobs?tabs=azure-cli - officlial tool to schedule "job" (Container App Jobs) runs with crontab expressions? OR using github actions for example?
3. https://learn.microsoft.com/en-us/azure/azure-functions/functions-container-apps-hosting - use Azure Functions with containerized apps - cheaper, easier, possibly
4. https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-scheduled - ACR tasks on schedule
5. https://learn.microsoft.com/en-us/azure/scheduler/migrate-from-scheduler-to-logic-apps - logic apps
### General Container Apps information
1. https://learn.microsoft.com/en-us/azure/container-apps/overview
2. https://learn.microsoft.com/en-us/azure/azure-functions/functions-deploy-container-apps?tabs=acr%2Cbash&pivots=programming-language-python
### Streamlit on Azure
1. https://learn.microsoft.com/en-us/answers/questions/1470782/how-to-deploy-a-streamlit-application-on-azure-app
2. https://discuss.streamlit.io/t/how-to-deploy-streamlit-to-azure/45667/3
3. https://benalexkeen.com/deploying-streamlit-applications-with-azure-app-services/
4. https://techcommunity.microsoft.com/blog/appsonazureblog/deploy-streamlit-on-azure-web-app/4276108


### Apitube links
1. https://apitube.io/cookbook/get-recent-articles-from-top-tech-blogs
2. https://docs.apitube.io/platform/news-api/parameters
3. https://apitube.io/cookbook/get-news-articles-in-multiple-languages - DOESN'T WORK. If you want results from multiple countries, categories etc you have to get each one individually, if they are exclusive, like an article being in language en and fr
for this you might want to use /category/...&query endpoints instead of /everything&query

