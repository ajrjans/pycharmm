#params.py: reads out all parameters from a chosen Bronkhorst device. Uses the Bronkhorst Propar module.

# Importing the module
import propar

#Define the COM port and node of the sensor here.
sensor = propar.instrument('COM8', 4)

db = sensor.db
parameters = db.get_all_parameters()

#Printing all parameter numbers and their current values.
for i in parameters :
   print(i)
   print(sensor.readParameter(i["dde_nr"]))