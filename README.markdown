This is a Jupyter Notebook project utilizing a used car dataset from Kaggle for cars. (https://www.kaggle.com/datasets/ander289386/cars-germany?resource=download)


1. Exploratory Data Analysis and Visualization
•	Basic data exploration and visualization
•	Look at data types, summary statistics, box plots and histograms to see data value distribution
•	Data is right skewed towards more expensive vehicles, meaning the majority of vehicles are at the lower price range. Inter Quartile Range is about 7.5k to 19.5k Euros in price.
2. Data Wrangling and Enriching
•	Add additional column for manufacturer country using external Excel spreadsheet.
•	Perform a left join to add country attribute for car makers.
•	Perform data wrangling for incomplete entries after join.
3. Elementary Analysis
   1. correlation with prices
      •	More data wrangling and modification
      •	Coefficient of correlation calculation done for numerical values, only noteworthy correlation with price would be horsepower

   2. depreciation over time

The next step is testing for coefficients of correlation affecting the price of the vehicle. Whether it is mileage, horsepower,
or age of the vehicle that is best correlated with the price.


Another point of analysis is finding value retention or car depreciation year over year. The secondary market for automobiles
is one of the robust so knowing which vehicles best retain value and what factors might impact that would  be a critical
point of consideration for industry players.

Later, I will eventually get around to figuring out how to devise a price predictor. What factors affect the outcome
of the price of an automobile.

Finally, I may develop a front end space to this proejct, incorporating HTML, CSS, Javascript and the like.

I'm just testing something
