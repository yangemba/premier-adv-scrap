import requests
import concurrent.futures
import asyncio
import logging
import time

link_listt = ['http://localhost:8888/' for x in range(100)]

slov = url_list = [f'https://premier.ua/zhilaia-nedvizhimost/arenda-zhilia?page={x}'
            for x in range(50)]


async def async_send():
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(executor, requests.get, slov[i])for i in range(10000)
        ]
        for response in await asyncio.gather(*futures):
            logging.warning(response.status_code)


def sync_sender(link_list):
    max_workers = min(20, len(link_list))
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as \
            executor:
        response_list = executor.map(requests.get, link_list)
    return list(response_list)


def main_perform_async():
    asyncio.run(async_send())


def main_perform_sync():
     sync_sender(slov)


if __name__ == '__main__':
    start = time.time()
    # main_perform_async()
    main_perform_sync()
    end = time.time() - start
    print(str(end))
