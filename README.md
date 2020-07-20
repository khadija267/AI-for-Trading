# Time-Series-Anomaly-Detection
Deep Learning model using keras on S&amp;P_500_Index_Data to detect anomalies.
How? 
   1- train Autoencoder network on data woth no anomalies
   2- take a new data poit and try to reconstruct it by the Auroencoder => if the reconstruction error of the new data point is above a threshold we set
                                                                              then we set this data point as an anomaly
