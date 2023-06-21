import json
import unittest
import datetime

with open("resources/data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("resources/data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("resources/data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)


# print(jsonData1)
# print(jsonData2)
# print(jsonExpectedResult)


def convertFromFormat1(jsonObject):
    location = jsonData1['location'].split('/')
    jsonDict1 = {
        'deviceID': jsonData1['deviceID'],
        'deviceType': jsonData1['deviceType'],
        'timestamp': jsonData1['timestamp'],
        'location': {
            'country': location[0],
            'city': location[1],
            'area': location[2],
            'factory': location[3],
            'section': location[4]
        },
        'data': {
            'status': jsonData1['operationStatus'],
            'temperature': jsonData1['temp']
        }
    }

    return jsonDict1


def convertFromFormat2(jsonObject):
    timestamp = datetime.datetime.strptime(
        jsonData2['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ').timestamp() * 1000

    jsonDict2 = {
        'deviceID': jsonData2['device']['id'],
        'deviceType': jsonData2['device']['type'],
        'timestamp': int(timestamp),
        'location': {
            'country': jsonData2['country'],
            'city': jsonData2['city'],
            'area': jsonData2['area'],
            'factory': jsonData2['factory'],
            'section': jsonData2['section']
        },
        'data': {
            'status': jsonData2['data']['status'],
            'temperature': jsonData2['data']['temperature']
        }
    }

    return jsonDict2


def main(jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main(jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main(jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )


if __name__ == '__main__':
    unittest.main()
