from flask import Flask, jsonify
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # CORS-u aktivləşdiririk
    
@app.route('/professions', methods=['GET'])
def get_professions():
    url = "https://vet.edu.gov.az/professions/specialty/list?start=0&length=1291"
    response = requests.get(url)
    data = response.json()

    result = []
    for item in data["data"]:
        # Nested structure-i sadələşdiririk
        formatted_item = {
            "İxtisas Adı": item["name"],
            "Təhsil Müddəti": item["education_duration"],
            "Müəssisə": item["enterprise"]["name"],  # Nested "enterprise" daxilindəki "name"
            "İxtisas ID": item["enterprise"]["enterprise_id"]  # Nested "enterprise" daxilindəki "enterprise_id"
        }
        result.append(formatted_item)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
