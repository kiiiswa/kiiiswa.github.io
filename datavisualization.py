import pandas
import pylab
from datetime import datetime
data = pandas.read_csv("data/weather_year.csv")
data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]
first_date = data.date.values[0]
#print (data)
#print(len(data))
#print(data.columns)
#print(data[["EDT", "Mean TemperatureF"]])
#print(data.EDT)
#print(data.EDT.head())
#print(data.EDT.head(10))
#print(data["Mean TemperatureF"].head())

print(data)
print(data.mean_temp.head())
print(data.mean_temp.std())
print(data.mean_temp.hist(kind:"bar"))
#pylab.show(print(data.mean_temp.hist()))
print(data.std())
#print(data.date.head())
#print(first_date)
#print(datetime.strptime(first_date, "%m-%d-%Y"))
pylab.show(data.max_temp.plot())
