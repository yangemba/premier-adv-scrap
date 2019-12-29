import faster_than_requests as requests
import time


slov = ['http://localhost:8888/' for x in range(100)]

url_list = ['https://ngrok.com/download' for x in range(2)]

start = time.time()
response = requests.scraper(url_list)
# print(response)
print(f'{time.time() - start}')














