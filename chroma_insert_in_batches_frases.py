import chromadb
import time

BATCH_SIZE = 1

chroma_client = chromadb.Client()
chroma_client = chromadb.PersistentClient(path="db")
collection = chroma_client.get_or_create_collection(name="english")

start_time = time.time()
start = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(start_time))
print("Starting time: ", start)


with open('phrases.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    lines = [line.replace('\n', '') for line in lines]

total= (len(lines)//BATCH_SIZE)

lines = [lines[i:i + BATCH_SIZE] for i in range(0, len(lines), BATCH_SIZE)]

start_number = 0
for i, line in enumerate(lines):
    ids = [str(i) for i in range(start_number, start_number + len(line))]
    collection.add(
        documents=line,
        ids=ids
    )

    print(f'Progress: {i}/{total}', end='\r')
    start_number = start_number + len(line)

end_time = time.time()
end = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(end_time))
print("Ending time: ", end)

seconds = end_time - start_time
seconds = round(seconds, 1)
print("Seconds spent: ", seconds)



