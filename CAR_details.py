#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


car = pd.read_excel('Car features.xlsx')
ins = pd.read_excel('Insurance claim.xlsx')
pol = pd.read_excel('Policy features.xlsx')


# In[4]:


# Display the first few rows of the dataset:
car.head()


# In[5]:


car


# In[10]:


# Cleaning max_torque and max_power power columns:
def data_clean(df):
    car["max_torque_Nm"] = car["max_torque"].str.extract(r"([-+]?[0-9]*\.?[0-9]+)(?=\s*Nm)").astype('float64')
    car["max_torque_rpm"] = car["max_torque"].str.extract(r"([-+]?[0-9]*\.?[0-9]+)(?=\s*rpm)").astype('float64') 
    car["max_power_bhp"] = car["max_power"].str.extract(r"([-+]?[0-9]*\.?[0-9]+)(?=\s*bhp)").astype('float64')
    car["max_power_rpm"] = car["max_power"].str.extract(r"([-+]?[0-9]*\.?[0-9]+)(?=\s*rpm)").astype('float64')
data_clean(car)
car


# In[11]:


# Dropping original columns:
car.drop(["max_torque","max_power"],axis=1,inplace=True)
car


# In[12]:


# List all column names:
car.columns.tolist()


# In[14]:


# Define the desired column order
my_order = ['policy_id', 'make', 'segment', 'model', 'max_torque_Nm', 'max_torque_rpm', 'max_power_bhp', 'max_power_rpm',
            'fuel_type', 'engine_type', 'airbags', 'is_esc', 'steering_type', 'is_adjustable_steering', 'is_tpms', 
            'is_parking_sensors', 'is_parking_camera', 'rear_brakes_type', 'is_brake_assist', 'displacement', 'cylinder', 
            'transmission_type', 'gear_box', 'turning_radius', 'length', 'width', 'height', 'gross_weight', 
            'is_front_fog_lights', 'is_rear_window_wiper', 'is_rear_window_washer', 'is_rear_window_defogger',  
            'is_power_door_locks',  'is_central_locking', 'is_power_steering', 'is_driver_seat_height_adjustable', 
            'is_day_night_rear_view_mirror', 'is_ecw', 'is_speed_alert', 'ncap_rating']
# Rearrange columns
car = car[my_order]
car


# In[15]:


# Display basic information about the dataset:
car.info()


# In[16]:


# Many of the columns depend on the car model. So, sorting the data by 'model':
car.sort_values(by='model', inplace=True)
car


# In[17]:


# Checking for missing values:
car.isnull().sum()


# In[18]:


# There are many missing values in the following columns: 
# max_torque_Nm                        7
# max_torque_rpm                       7
# max_power_bhp                        3
# max_power_rpm                        3
# fuel_type                           26
# engine_type                          3
# airbags                              9
# is_esc                               3
# steering_type                        0
# is_adjustable_steering               7
# is_tpms                              3
# is_parking_sensors                   7
# is_parking_camera                    3
# rear_brakes_type                     0
# is_brake_assist                      0
# displacement                         7
# cylinder                             7
# All these depend on the car model. So, we can fill the missing datas on the basis of the car model:

car['fuel_type'] = car.groupby('model')['fuel_type'].ffill()
car['max_torque_Nm'] = car.groupby('model')['max_torque_Nm'].ffill()
car['max_torque_rpm'] = car.groupby('model')['max_torque_rpm'].ffill()
car['max_power_bhp'] = car.groupby('model')['max_power_bhp'].ffill()
car['max_power_rpm'] = car.groupby('model')['max_power_rpm'].ffill()
car['engine_type'] = car.groupby('model')['engine_type'].ffill()
car['airbags'] = car.groupby('model')['airbags'].ffill()
car['is_adjustable_steering'] = car.groupby('model')['is_adjustable_steering'].ffill()
car['is_parking_camera'] = car.groupby('model')['is_parking_camera'].ffill()
car['is_parking_sensors'] = car.groupby('model')['is_parking_sensors'].ffill()
car['cylinder'] = car.groupby('model')['cylinder'].ffill()
car['displacement'] = car.groupby('model')['displacement'].ffill()
car['is_tpms'] = car.groupby('model')['is_tpms'].ffill()
car['is_esc'] = car.groupby('model')['is_esc'].ffill()
car


# In[19]:


# Now checking if all missing values are filled:
car.isnull().sum()


# In[20]:


# Saving the new data with no missing values:
# car.to_excel('car_filled.xlsx', index=False)
# car_filled = pd.read_excel('car_filled.xlsx')
# car_filled
# car_filled.isnull().sum()


# In[21]:


# Display summary statistics:
car.describe()


# In[24]:


# Changing yes and no data to 1 and zero so that numerical analysis becomes easy:
# Replace 'Yes' with 1 and 'No' with 0:
car['is_esc'] = car['is_esc'].replace({'Yes': 1, 'No': 0})
car['is_adjustable_steering'] = car['is_adjustable_steering'].replace({'Yes': 1, 'No': 0})
car['is_tpms'] = car['is_tpms'].replace({'Yes': 1, 'No': 0})
car['is_parking_sensors'] = car['is_parking_sensors'].replace({'Yes': 1, 'No': 0})
car['is_parking_camera'] = car['is_parking_camera'].replace({'Yes': 1, 'No': 0})
car['is_front_fog_lights'] = car['is_front_fog_lights'].replace({'Yes': 1, 'No': 0})
car['is_rear_window_wiper'] = car['is_rear_window_wiper'].replace({'Yes': 1, 'No': 0})
car['is_rear_window_washer'] = car['is_rear_window_washer'].replace({'Yes': 1, 'No': 0})
car['is_rear_window_defogger'] = car['is_rear_window_defogger'].replace({'Yes': 1, 'No': 0})
car['is_brake_assist'] = car['is_brake_assist'].replace({'Yes': 1, 'No': 0})
car['is_power_door_locks'] = car['is_power_door_locks'].replace({'Yes': 1, 'No': 0})
car['is_central_locking'] = car['is_central_locking'].replace({'Yes': 1, 'No': 0})
car['is_power_steering'] = car['is_power_steering'].replace({'Yes': 1, 'No': 0})
car['is_driver_seat_height_adjustable'] = car['is_driver_seat_height_adjustable'].replace({'Yes': 1, 'No': 0})
car['is_day_night_rear_view_mirror'] = car['is_day_night_rear_view_mirror'].replace({'Yes': 1, 'No': 0})
car['is_ecw'] = car['is_ecw'].replace({'Yes': 1, 'No': 0})
car['is_speed_alert'] = car['is_speed_alert'].replace({'Yes': 1, 'No': 0})

car


# In[26]:


car.info()


# In[35]:


# Changing data type of columns:
# df['Column'] = df['Column'].astype(int)
# Not needed as the data type are proper


# In[36]:


# Basic Statistics
car['model'].value_counts()


# In[90]:


# Create a new DataFrame with distinct values
# model_df = pd.DataFrame({'model': car['model'].unique()})
# model_df


# In[91]:


import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    # Extract the numeric part of the 'model' column and convert to integers
    car_unique['model_numeric'] = car_unique['model'].str.extract('(\d+)').astype(int)
    # Sort the DataFrame based on both the numeric and string parts of 'model'
    car_unique_sorted = car_unique.sort_values(by=['model_numeric', 'model'], ascending=[True, True])
    # Drop the temporary 'model_numeric' column if you don't need it
    car_unique_sorted = car_unique_sorted.drop(columns=['model_numeric'])
# Displaying the DataFrame
car_unique_sorted


# In[113]:


# Analysis:
plt.figure(figsize=(20, 16))
car_unique_sorted.set_index('model').plot(kind='line')
plt.title('Line Plot of Features by Car Model')
plt.show()


# In[122]:


car_unique_sorted.plot(x='model', y=('length'), kind='scatter')
plt.title('Scatter Plot of Length by Car Model')
plt.show()


# In[116]:


car_unique_sorted.plot(x='model', y='width', kind='scatter')
plt.title('Scatter Plot of Length by Car Model')
plt.show()


# In[117]:


car_unique_sorted.plot(x='model', y='height', kind='scatter')
plt.title('Scatter Plot of Length by Car Model')
plt.show()


# In[123]:


car.set_index('model')['max_power_bhp'].plot(kind='hist', bins=20)
plt.title('Histogram of Max Power (BHP) by Car Model')
plt.show()


# In[125]:


car.set_index('model')[['length', 'width', 'height']].plot(kind='box')
plt.title('Box Plot of Dimensions by Car Model')
plt.show()


# In[126]:


car['fuel_type'].value_counts().plot(kind='bar')
plt.title('Bar Plot of Fuel Types by Car Model')
plt.show()


# In[127]:


car.plot(x='model', y=['length', 'width', 'height'], kind='hist', figsize=(10, 6))
plt.title('Scatter Plot of Dimensions by Car Model')
plt.xlabel('Car Model')
plt.ylabel('Dimension Value')
plt.legend(['Length', 'Width', 'Height'])
plt.show()


# In[98]:


car['model'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie Chart of Car Models')
plt.show()


# In[99]:


car['segment'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie Chart of Car Segments')
plt.show()


# In[100]:


correlation_matrix = car.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


# In[101]:


car.plot(x='model', y=['length', 'width', 'height'], kind='line')
plt.title('Line Plot of Dimensions by Car Model')
plt.show()


# In[ ]:




