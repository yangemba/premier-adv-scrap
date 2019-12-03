import requests
import concurrent.futures
import asyncio
import logging
import time

slov = [["http://localhost:8888/", {'Content-Type': 'application/json'}] for i
        in range(10)]


async def send():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(executor, requests.get, *(slov[i]))for i in range(10)
        ]
        for response in await asyncio.gather(*futures):
            logging.warning(response.status_code)


def main_perform():
    await send()


if __name__ == '__main__':
    start = time.time()
    main_perform()
    end = time.time() - start
    print(str(end))
