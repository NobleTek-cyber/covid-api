from flask import Flask, jsonify 
import requests
import csv
from io import StringIO

app = Flask(__name__)


#https://github.com/CSSEGISandData
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-23-2020.csv"

countries = ["Ghana", "Togo", "Nigeria"]
covid_cases = []


@app.route('/api')
def cases():
    resp = requests.get(url)
    data = resp.content.decode('ascii', 'ignore')

    csv_data = StringIO(data)

    reader = csv.reader(csv_data)

    for row in reader:
        if row[0] == "FIPS":
            continue
        if row[3] in countries:
            covid_cases.append({
                "Contry": row[3],
                "Confirm Cases": row[7],
                "Deaths": row[8],
                "Recoveries": row[9],
                "Active Cases": row[10]
            })

    print(covid_cases)

    return jsonify(
        {
        "Covid 19 Cases": [
            {"Country": "Ghana", "Reported Cases": 400},
            {"Country": "Togo", "Reported Cases": 400},
            {"Country": "Nigeria", "Reported Cases": 400}
            ]
        }
    )

if __name__ == "__main__":
    app.run(port=8000, debug=True)