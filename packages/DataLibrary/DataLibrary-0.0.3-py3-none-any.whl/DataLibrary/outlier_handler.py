class OutlierHandler:
  import pandas as pd
import numpy as np
class OutlierHandler:
    def detect_outliers(self, data, threshold):
      
        z_scores = (data - np.mean(data)) / np.std(data)
        outliers = np.abs(z_scores) > threshold
        return outliers

    def remove_outliers(self, data, threshold):
        
        outliers = self.detect_outliers(data, threshold)
        data_without_outliers = data[~outliers]
        return data_without_outliers

    def correct_outliers(self, data, threshold):
       
        outliers = self.detect_outliers(data, threshold)
        data_corrected = data.copy()
        non_outlier_mean = np.mean(data[~outliers])
        data_corrected[outliers] = non_outlier_mean
        return data_corrected
