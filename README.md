# MedCabinet Flask API

The MedCabinet API can be used to recieve cannabis strain predictions based on desired qualities and characteristics. It also provides access to the strain information stored in the connected database

## Endpoints

#### /predict:
input: JSON object `{
"type" :  [],
"effect" : [],
"flavor" : []}`
output: JSON object `{"predictions": [{"description": ,
"effects": , "flavors": , "name": , "rating": , "type": }]} 

####/
