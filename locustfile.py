from app import predict

def predict():
    data = {"CHAS": {"0": 0}, "RM": {"0": 6.575}, "TAX": {"0": 296.0}, "PTRATIO": {"0": 15.3}, "B": {"0": 396.9},
            "LSTAT": {"0": 4.98}}
    url = 'https://udacity-c2.azurewebsites.net/'
    response = requests.post(url, data)
    assert response.status_code == 200
