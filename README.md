# MedCabinet Flask API

The MedCabinet API can be used to recieve cannabis strain predictions based on desired qualities and characteristics.

## Endpoints

#### /predict:
input: JSON object `{
"type" :  [selected type(s)],
"effect" : [selected effect(s)],
"flavor" : [selected flavor(s)]}`
