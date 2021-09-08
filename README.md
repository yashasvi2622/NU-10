# NU-10 : OHLC ENGINE
## StocksChart 
* This project is a model dashboard on which the user would be able to analyze the sentiment of a specific stocks for different time periods (eg. weekly,monthly).
### OHLC Chart :
* An OHLC chart is a type of bar-chart that shows open, high, low, and closing prices for each period. OHLC charts are useful since they show the four major data points over a period, with the closing price being considered the most important by many traders.
* The chart type is useful because it can show increasing or decreasing momentum. When the open and close are far apart it shows strong momentum, and when the open and close are close together it shows indecision or weak momentum. The high and low show the full price range of the period, useful in assessing volatility. There are several patterns traders watch for  OHLC charts.
### CandleStick Chart:
* Candlestick charts are used by traders to determine possible price movement based on past patterns. Candlesticks are useful when trading as they show four price points (open, close, high, and low) throughout the period of time the trader specifies.
* Many algorithms are based on the same price information shown in candlestick charts.Trading is often dictated by emotion, which can be read in candlestick charts.


## Required Packages :
* Python 3.9
* Pandas : pip install pandas
* Django: pip install django
* Plotly: pip install plotly
* pyEX: pip install pyEx

## Installation & Execution :
* Download all the files of the repository. Create a project in IDE and add the files of the repository to the project. Now run the command prompt and go the directory of the repository.
* Now to establish the server execute the following command:  Python manage.py runserver

## Dashboard Design and Visualization :
* Main-Dashboard:
![alt text](https://github.com/yashasvi2622/HNU-10/blob/main/NU-10%20images/search1.jpeg "Dashboard")

* User needs to enter a valid symbol to search for the respective stock :
![alt text](https://github.com/yashasvi2622/HNU-10/blob/main/NU-10%20images/search2.jpeg "Valid-Symbol")

* OLHC Graph- Users can switch between  OHLC graphs to candlestick graphs by clicking on the button :
:
![alt text](https://github.com/yashasvi2622/HNU-10/blob/main/NU-10%20images/graph1.jpeg "Valid-Symbol")

* Candlestick Graph :
![alt text](https://github.com/yashasvi2622/HNU-10/blob/main/NU-10%20images/graph4.jpeg "Valid-Symbol")

* Users can see other information about the company by clicking on the “more info” button (e.g. : PE ratio, 52 Weeks high/low) :
![alt text](https://github.com/yashasvi2622/HNU-10/blob/main/NU-10%20images/graph3.jpeg "Valid-Symbol")

## Specifications
### Technologies/ libraries used :- 
* Frontend: HTML,CSS,Javascript  
* Backend: Pandas,django,plotly
* Users would be able to filter the graph for different timestamps. (e.g. : 1D, 5D, 6M)



