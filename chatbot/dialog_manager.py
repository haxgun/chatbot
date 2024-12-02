import json


def save_dialog(user_id, dialog_id, prompt, response):
    try:
        with open('dialogues.json', 'r') as file:
            dialogues = json.load(file)
    except FileNotFoundError:
        dialogues = {}

    if user_id not in dialogues:
        dialogues[user_id] = {}

    if dialog_id not in dialogues[user_id]:
        dialogues[user_id][dialog_id] = []

    dialogues[user_id][dialog_id].append({"prompt": prompt, "response": response})

    max_length = 4096  # лимит для модели GPT-3.5 Turbo
    while len(json.dumps(dialogues[user_id][dialog_id])) > max_length:
        dialogues[user_id][dialog_id].pop(0)

    with open('dialogues.json', 'w') as file:
        json.dump(dialogues, file, indent=4)


def load_dialog_context(user_id, dialog_id):
    try:
        with open('dialogues.json', 'r') as file:
            dialogues = json.load(file)
        return dialogues.get(user_id, {}).get(dialog_id, [])
    except FileNotFoundError:
        return []
