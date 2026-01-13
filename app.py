import requests

# Linkdəki məlumatı çəkirik
url = "https://vet.edu.gov.az/professions/specialty/list?start=0&length=1291"

# API sorğusunu göndəririk
response = requests.get(url)

# JSON formatında verilənləri alırıq
data = response.json()

# Verilənləri ekranda göstəririk
for item in data["data"]:
    print(f"İxtisas: {item['name']}")
    print(f"Təhsil Müddəti: {item['education_duration']}")
    print(f"Müəssisə: {item['enterprise']['name']}")
    print("-" * 50)
