# Training dataset
with open('./data/dialogues.txt', encoding='utf-8') as dialogues_file:
    content = dialogues_file.read()

dialogues = content.split('\n\n')

chat_dataset = []
for dialogue in dialogues:
    replicas = dialogue.split('\n')
    replicas = [replica[2:].strip().lower() for replica in replicas]
    replicas = [replica for replica in replicas if replica]
    for i in range(len(replicas) - 1):
        chat_dataset.append((replicas[i], replicas[i+1]))

chat_dataset = list(set(chat_dataset))

def get_dataset(limit):
    return chat_dataset[:limit]
