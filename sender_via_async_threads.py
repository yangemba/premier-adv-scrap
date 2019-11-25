import requests
import concurrent.futures
import asyncio
import logging
import time


async def send():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(executor, requests.get, 'http://localhost:8888/')
            for i in range(10)
        ]
        for response in await asyncio.gather(*futures):
            logging.warning(response.status_code)


def main_perform():
    asyncio.run(send())


if __name__ == '__main__':
    start = time.time()
    main_perform()
    end = time.time() - start
    print(str(end))
