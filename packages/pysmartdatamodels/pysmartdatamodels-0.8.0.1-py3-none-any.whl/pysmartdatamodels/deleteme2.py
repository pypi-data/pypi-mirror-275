from pysmartdatamodels import *

subject = "dataModel.Weather"

dataModel = "WeatherForecast"

attribute = "precipitation"

print(description_attribute(subject, dataModel, attribute))

# List the attributes of a data model
print("10 : ")
print(attributes_datamodel(subject, dataModel))