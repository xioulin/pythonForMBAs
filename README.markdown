This project is based on techniques from the book [Python for MBAs](https://www.pythonformbas.com/), which is a fantastic resource for business professionals looking to develop their Python data analytics capabilities.

This is a Jupyter Notebook project utilizing a [used car dataset from Kaggle for cars.](https://www.kaggle.com/datasets/ander289386/cars-germany?resource=download) 

For a screen recorded walk through, please check out [my youtube page](https://www.youtube.com/@pkc-Steelkilt). 


ok, i know, i just hyperlink the youtube video and link to the jupyter notebook, explaining what I did. 
This will show my work process, how I think, how I approach issues, and explain what I did. 
This will show that I will leave behind well documented code which will make it much easier for whoever follows me.


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
   Depreciation by year:
   Depreciation by mileage:
   


   Find cars with the same make and model over the ten year span. Find how much price depreciates and what affects that depreciation. 



Another point of analysis is finding value retention or car depreciation year over year. The secondary market for automobiles is one of the robust so knowing which vehicles best retain value and what factors might impact that would  be a critical point of consideration for industry players.

