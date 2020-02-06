# MedCabinet Flask API

The MedCabinet API can be used to recieve cannabis strain predictions based on desired qualities and characteristics. It also provides access to the strain information stored in the connected database

## Endpoints

#### /predict:
This route utilizes our predictive model to return strain predictions based on user input

input: JSON object `{
"type" :  [],
"effect" : [],
"flavor" : []}`

output: JSON object `{"predictions": [{"description": ,
"effects": , "flavors": , "name": , "rating": , "type": }]}` 

#### /strain:
This route accesses the database to return information about a specific cannabis strain

input: `{"strain": ""}`

returns: `{"description": "", "effects": "", "flavors": "", "name": "", "rating": "", "type": ""}`
