#  AI-for-Trading
## 1. Time-Series-Anomaly-Detection:
Deep Learning model using keras on S&amp;P_500_Index_Data to detect anomalies.
How? 
   1- train Autoencoder network on data woth no anomalies
   2- take a new data poit and try to reconstruct it by the Auroencoder, if the reconstruction error of the new data point is above a threshold we setthen we set this data point as an anomaly.
   <p float="center">
  <img src="https://github.com/khadija267/AI-for-Trading/blob/master/images/4.png?raw=true" width="400" /> 
    <img src="https://github.com/khadija267/AI-for-Trading/blob/master/images/5.png?raw=true" width="400" /> 
      <img src="https://github.com/khadija267/AI-for-Trading/blob/master/images/6.png?raw=true" width="400" /> 

</p>
## 2. Crypto data analysis:
Applying Genesis Period Analysis, First Halving Analysis, and Second Halving Analysis.
<p float="center">
  <img src="https://github.com/khadija267/AI-for-Trading/blob/master/images/1.png?raw=true" width="400" /> 
    <img src="https://github.com/khadija267/AI-for-Trading/blob/master/images/2.png?raw=true" width="400" /> 
      <img src="https://github.com/khadija267/AI-for-Trading/blob/master/images/3.png?raw=true" width="400" /> 

</p>

## 3. Turn of Month Effect:
Strategy is equity prices increase during the last 4 days and the first 3 days of each month.
We buy the BTC on close at the first day of the month and sell it on the following day.

Title: Turn of the Month Strategy Template
Description: The strategy buys the asset on the last day of a month and
sells the asset on the first day of the next month. If the asset price
is greater than the 10-day SMA then the strategy continues to hold the
asset.
Dataset: BTC_1min
<p float="center">
  <img src="https://github.com/khadija267/AI-for-Trading/blob/master/images/7.png?raw=true" width="400" /> 
    <img src="https://github.com/khadija267/AI-for-Trading/blob/master/images/8.png?raw=true" width="400" /> 

</p>


