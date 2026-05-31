import re
from utils.normal_ranges import NORMAL_RANGES

def extract_parameters(text):

    data = {}

    hb = re.search(r'Hemoglobin.*?(\d+\.\d+)', text,re.DOTALL)

    if hb:
        data["Hemoglobin"] = {
            "value": float(hb.group(1)),
            "unit": "g/dL"
        }

    wbc = re.search(r'Total WBC Count.*?(\d+\.\d+)', text,re.DOTALL)

    if wbc:
        data["WBC"] = {
            "value":float(wbc.group(1)),
            "unit": "thou/cumm"
        }

    platelets = re.search(r'Platelet Count.*?(\d+\.\d+)', text,re.DOTALL)

    if platelets:
        data["Platelets"] = {
            "value":float(platelets.group(1)),
            "unit":"lakh/cumm"
        }

    return data
def analyzer_parameters(data):

    results = []

    for parameter, details in data.items():

        value = details["value"]
        unit = details["unit"]

        low = NORMAL_RANGES[parameter]["low"]
        high = NORMAL_RANGES[parameter]["high"]

        if value < low:
            status = "LOW"

        elif value > high:
            status = "HIGH"

        else:
            status = "NORMAL"

        results.append({
            "parameter": parameter,
            "value": value,
            "unit": unit,
            "status": status
        })

    return results

def generate_summary(results):

    abnormal = []

    for item in results:

        if item["status"] != "NORMAL":
            abnormal.append(
                f"{item['parameter']} is {item['status']}"
            )

    if len(abnormal) == 0:
        return "All analyzed parameters are within normal limits."

    return ", ".join(abnormal)

