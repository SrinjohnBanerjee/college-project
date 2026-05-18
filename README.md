# college-project
This project is about detection of phishing url based on heuristic features of the url and predicted by machine learning models.
The project is written mainly in python which is a dynamically typed Object Oriented Programming language.


The file "training model record" is the  representative of the original file that is used to train the machine learning models.

The methodology:
1.involves figuring out the features of the URLs
2.Followed by extracting them using various libraries which can be found in the final_features.py file.The Jupyter notebook is used for writing the feature extracting functions.
3.Then the functions were applied to the dataframe and the returned values were stored in a new column in the dataframe.
4.The machine learning model use logistic Regression. The logistic Regression algorithm can be used for classification purposes and have a sigmoid graph.

5.Finally the machine learning model is used to predict the output for a given url in the backend and the webpage is rendered in the backend.
6.The website uses JSON to communicate with the backend and acn automatically give the output without clicking any submit button or reloading the page.


Future Scope:
1.The addition of threat Intelligence can be done by using APIs of various platforms such as VirusTotal and AbuseIPDB.
2.Finding out the domain age of a domain to determine the possibility of the url being a phishing url.
3.finding out if the website for a given suspected url's webpage have a lot of redirections.
