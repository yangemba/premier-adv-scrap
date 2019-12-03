import time
from concurrent.futures import ThreadPoolExecutor
import asyncio
import urllib.request
import urllib.error
​
NUMBER_OF_THREADS = 10

​
def generate_urls():
    urls = [
        "https://github.com/",
        "https://trello.com/",
        "https://nodejs.org/en/",
        "https://golang.org/",
        "https://www.python.org/",
        "https://www.ruby-lang.org/en/",
        "http://www.cplusplus.com/",
    ]
    result = []
    number_of_repeats = 5
    for _ in range(number_of_repeats):
        result.extend(urls)
    return result

​
​

def url_request_function(url):
    try:
        with urllib.request.urlopen(url) as response:
            return response.status
    except urllib.error.URLError:
        return 500

​
async def async_sender(func_obj, c_urls):
    response_list = []
    with ThreadPoolExecutor(max_workers=NUMBER_OF_THREADS) as \
            executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(executor, func_obj, url)
            for url in c_urls
        ]
        for response in await asyncio.gather(*futures):
            response_list.append(response)
    return response_list

def sync_sender(func_obj, c_urls):
    with ThreadPoolExecutor(max_workers=NUMBER_OF_THREADS) as \
            executor:
        response_list = executor.map(func_obj, c_urls)
    return list(response_list)

​
def async_run(urls):
    response_list = asyncio.run(async_sender(url_request_function,
                                             urls))
    return response_list

​
def sync_run(urls):
    response_list = sync_sender(url_request_function, urls)
    return response_list

​
​

def sync_test(list_of_urls_to_test):
    start_time = time.time()
    response_list = sync_run(list_of_urls_to_test)
    print(response_list)
    end_time = time.time()
    print(f"sync run: {end_time - start_time} seconds")

​
def async_test(list_of_urls_to_test):
    start_time = time.time()
    response_list = async_run(list_of_urls_to_test)
    print(response_list)
    end_time = time.time()
    print(f"Async run: {end_time - start_time} seconds")

​
​

def sync_then_async(list_of_urls_to_test):
    print("Sync then async")
    sync_test(list_of_urls_to_test)
    async_test(list_of_urls_to_test)
    print("*" * 50)

​
def async_then_sync(list_of_urls_to_test):
    print("Async then sync")
    async_test(list_of_urls_to_test)
    sync_test(list_of_urls_to_test)
    print("*" * 50)

def main():
    list_of_urls_to_test = generate_urls()
    print(list_of_urls_to_test)

sync_then_async(list_of_urls_to_test=list_of_urls_to_test)
time.sleep(10)
async_then_sync(list_of_urls_to_test=list_of_urls_to_test)

if __name__ == '__main__':

