from threading import Thread
from multiprocessing import Process
from datetime import datetime


def read_file(file):
    with open(file, 'r') as f:
        text = f.read()
    return text

all_text = read_file('text.txt')
part_1 = all_text.split('!!!!!!')[0]
part_2 = all_text.split('!!!!!!')[1]


def write_to_file(data, filename, flag):
    with open(filename, flag) as file:
        file.write(data)


start = datetime.now()
write_to_file(all_text, 'main_flow.txt', flag='w')
end = datetime.now()
print(f'Execution time write_to_file():', end - start)


start_t1 = datetime.now()
thread_1 = Thread(target=write_to_file, kwargs={'data': all_text, 'filename': 'treads1.txt','flag': 'a'})
thread_2 = Thread(target=write_to_file, kwargs={'data': all_text, 'filename': 'treads2.txt','flag': 'a'})


thread_1.start()
start_t2 = datetime.now()
thread_2.start()
thread_1.join()
end_t1 = datetime.now()
thread_2.join()
end_t2 = datetime.now()

print(f'Execution time write_to_file() in 1 thread:', end_t1 - start_t1)
print(f'Execution time write_to_file() in 2 thread:', end_t2 - start_t2)
print(f'Execution time write_to_file() threads in general:', end_t2 - start_t1)


start_p1 = datetime.now()
process_1 = Process(target=write_to_file, kwargs={'data': all_text, 'filename': 'processes1.txt','flag': 'a'})
process_2 = Process(target=write_to_file, kwargs={'data': all_text, 'filename': 'processes2.txt','flag': 'a'})

process_1.start()
start_p2 = datetime.now()
process_2.start()
process_1.join()
end_p1 = datetime.now()
process_2.join()
end_p2 = datetime.now()
print(f'Execution time write_to_file() in 1 process:', end_p1 - start_p1)
print(f'Execution time write_to_file() in 2 process:', end_p2 - start_p2)
print(f'Execution time write_to_file() processes in general:', end_p2 - start_p1)
