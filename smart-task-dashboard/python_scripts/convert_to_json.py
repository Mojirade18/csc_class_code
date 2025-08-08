import json

tasks = []

with open('../data/tasks.txt', 'r') as file:
    for line in file:
        if '|' in line:
            task, date = line.strip().split('|')
            tasks.append({
                'task': task.strip(),
                'date': date.strip()
            })

with open('../data/tasks.json', 'w') as json_file:
    json.dump(tasks, json_file, indent=4)

print("Converted to tasks.json")
