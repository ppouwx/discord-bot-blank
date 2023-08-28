word_list = ["words", "here"]
def save_data(data):
    with open('word_of_the_day.json', 'w') as f:
        json.dump(data, f)

def load_data():
    if os.path.isfile('word_of_the_day.json'):
        with open('word_of_the_day.day', 'r') as f:
            return json.load(f)
    return {}