import requests

headers = {
    'Authorization': 'Token VfmhEWOQQvRqiVimXhvGr0ODDPV2R-Ccwf2VCBhMkr52zaKhU_jx1XU0zn99H7BCM5djv--IlHgxgIkLBDgKJA==',
    'Content-Type': 'application/json',
}

params = (
    ('org', 'brandzone'),
    ('bucket', 'crawler_logs'),
)

data = '{ "start": "2021-01-02T00:00:00Z", "stop": "2021-06-03T00:00:00Z"}'

response = requests.post('http://85.95.244.39:8086/api/v2/delete/', headers=headers, params=params, data=data)
#response = requests.post('http://85.95.244.39:8086/api/v2/delete/?org=brandzone&bucket=crawler_logs', headers=headers, data=data)

print(response.status_code)
print(response.reason)


