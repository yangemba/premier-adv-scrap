from multiprocessing import Pool
import requests
import time


def req(url):

    return requests.get(url)


if __name__ == '__main__':
    start = time.time()
    p = Pool(2)
    print(p.map(req, ['http://localhost:8888/' for x in range(0,2)]))
    end = time.time() - start
    print(str(end))
