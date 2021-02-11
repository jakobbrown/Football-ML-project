# Football-ML-project
This project makes use of in-game football datasets, as well as scraping some financial data for different clubs to model the performance of a club the following season, with the aim of building a predictive model for predicting league points totals for a team based on the team's data from the season prior as the input variables. The outputs from this regression model can then subsequently be ordered to produce a league ranking/league table for the whole league for any given season. 

The in-game statistics were obtained in csv format, one per season per team. They were from the paid website https://footystats.org/, and so - although I can't see any legal documentation on the website, I assume they have rights over the data files and so I won't make them available here. 

The financial data however I scraped from transfermrkt.com, with the help of a tutorial I will post below, along with other sources that either inspired the idea for this project or helped me greatly with their code online. 

This project was used as coursework for the 'Principles of Data Science' module of my masters in data science, demonstrating a 'tiny project' that included all key stages of a typical data science pipeline, save for model deployment.

Future improvements to be made definitely include quantifying prior season achievement for teams that have been promoted from the lower division, and scaling it relative to the performance of the teams in the division they are being promoted to. At the moment the model only predicts the 3 promoted teams to be in the bottom 3 in order of their previous lower division ranking. More informative and valuable stats have been made available in recent years such as xG, xA etc. It was preferred however to have more training data from the previous years and so these stats were ommited on the basis they would have severely limited the amount of data available to be trained on. In the future, incorporation of these statistics would no doubt prove extremely valuable predictors.


Scraping tutorial: https://fcpython.com/blog/introduction-scraping-data-transfermarkt
