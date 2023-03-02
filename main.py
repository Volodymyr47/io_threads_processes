import random
import string
from threading import Thread
from multiprocessing import Process
from datetime import datetime


def random_text(length):
    letter = string.ascii_letters
    result = ''.join(random.choice(letter) for _ in range(length))
    return result


text = random_text(99999999)


def write_to_file(data, flow='Main flow'):
    start = datetime.now()
    with open('external_file.txt', 'w') as file:
        file.write(data)
    end = datetime.now()
    print(f'Execution time {flow}:', end - start)


write_to_file(text)
thread_1 = Thread(target=write_to_file, kwargs={'data': text, 'flow': 'thread_1'})
thread_2 = Thread(target=write_to_file, kwargs={'data': text, 'flow': 'thread_2'})
process_1 = Process(target=write_to_file, kwargs={'data': text, 'flow': 'process_1'})
process_2 = Process(target=write_to_file, kwargs={'data': text, 'flow': 'process_2'})

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()

process_1.start()
process_2.start()
process_1.join()
process_2.join()
