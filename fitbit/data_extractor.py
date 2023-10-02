import gather_keys_oauth2 as Oauth2
import fitbit
import pandas as pd 
import json
import matplotlib.pyplot as plt


# Data we want.
# data = "activities/heart"
# data_response = "activities-heart-intraday"
# filename = "heart"

# data = "activities/steps"
# data_response = "activities-steps-intraday"
# filename = "steps"

# data = "-/hrv"
# data_response = "hrv-intraday"
# filename = "hrv"

# data = "-/spo2"
# data_response = "spo2-intraday"
# filename = "spo2"


# Client ID.
CLIENT_ID = ""
# CLIENT_ID = ""

# Client Secret.
CLIENT_SECRET = ""
# CLIENT_SECRET = ""

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit(
        CLIENT_ID,
        CLIENT_SECRET,
        oauth2=True,
        access_token=ACCESS_TOKEN,
        refresh_token=REFRESH_TOKEN
    )


# Dates of interest.
startTime = pd.to_datetime("2023/07/16")
endTime = pd.to_datetime("2023/08/23")

print()
print(f"Start time: {startTime}")
print(f"End time: {endTime}")
print()

# *****************************************************************************
# Sleep data.
data = "sleep"
filename = "sleep"

sleepData = auth2_client.time_series(data, base_date=startTime, end_date=endTime)
# print(sleepData)
json_object = json.dumps(sleepData, indent=4)
with open("juliusSleepData.json", "w") as outfile:
    outfile.write(json_object)




# date_list = []
# df_list = []
# allDates = pd.date_range(start=startTime, end=endTime)

# for oneDay in allDates:
#     oneDay = oneDay.date().strftime("%Y-%m-%d")
#     oneDayData = auth2_client.intraday_time_series(
#         data,
#         base_date=oneDay,
#         detail_level="1min"
#     )
#     # print(oneDayData)
#     json_object = json.dumps(oneDayData, indent=4)
#     with open("data.json", "w") as outfile:
#         outfile.write(json_object)
#     break

#     oneDayDf = pd.DataFrame(oneDayData[data_response]["dataset"])
#     date_list.append(oneDay)
#     df_list.append(oneDayDf)

#     # print(oneDay)
#     # print()
#     # print(oneDayDf.head())

# # Clean it up.
# final_df_list = []
# for date, df in zip(date_list, df_list):
#     if len(df) == 0:
#         continue
#     df.loc[:, "date"] = pd.to_datetime(date)
#     # df.loc[:, "datetime"] = df.time
#     df['datetime'] = df['date'] + pd.to_timedelta(df['time'])
#     final_df_list.append(df)
# final_df = pd.concat(final_df_list, axis=0)

# # Print the head for sanity check.
# print(final_df.info())
# print(final_df.head())

# # Plot the values.
# final_df.plot(
#     kind="line",
#     x="datetime",
#     y="value"
# )
# plt.show()

# # Save the data.
# final_df.to_csv(filename + '.csv', index=False)