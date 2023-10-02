import json
import matplotlib.pyplot as plt
import pandas as pd

from datetime import datetime


# *****************************************************************************
# Sleep data.
filename = "sleepData.json"
file = open(filename)
sleepData = json.load(file)
file.close()

top_date_format = "%Y-%m-%dT%H:%M:%S.%f"
inner_date_format = "%H:%M:%S"
converted_date_format = "%Y-%m-%d %H:%M:%S"

dataset = sleepData["sleep"]

value_list = []
datetime_list = []

for day in dataset:
    dayStartTime = datetime.strptime(day["startTime"], top_date_format)
    dayEndTime = datetime.strptime(day["endTime"], top_date_format)

    dayStartDate = dayStartTime.date()
    dayEndDate = dayEndTime.date()

    diffEnds = False
    if dayStartDate != dayEndDate:
        diffEnds = True

    minuteData = day["minuteData"]

    for datapoint in minuteData:
        converted = str(dayStartDate) + " " + datapoint["dateTime"]
        datapoint_datetime = datetime.strptime(converted, converted_date_format)

        if datapoint_datetime < dayStartTime:
            converted = str(dayEndDate) + " " + datapoint["dateTime"]
            datapoint_datetime = datetime.strptime(converted, converted_date_format)

        datetime_list.append(datapoint_datetime)
        value_list.append(datapoint["value"])

sleep_df = pd.DataFrame()
sleep_df["datetime"] = datetime_list
sleep_df["value"] = value_list

# print(sleep_df.head())
sleep_df.sort_values(by="datetime", inplace=True)
sleep_df.to_csv("ike_sleep_data.csv", index=False)

plt.plot(sleep_df["datetime"], sleep_df["value"])
plt.show()
# *****************************************************************************