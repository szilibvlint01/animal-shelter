import json

def load_animals(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_animals(file_path, animals):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(animals, file)


def show_animals(animals):
    for animal in animals:
        print(f"ID: {animal["id"]}")
        print(f"Name: {animal["name"]}")
        print(f"Type: {animal["type"]}")
        print(f"Age: {animal["age"]}")
        print(f"Available: {animal["available"]}")
        


def get_available_animals(animals):
    available_animals = []

    for animal in animals:
        if animal["available"]:
            available_animals.append(animal)
    return available_animals


def find_animal_by_id(animals, animal_id):
    for animal in animals:
        if animal["id"] == animal_id:
            return animal
    return None


def update_animal_status(animals, adoption):
    animal = find_animal_by_id(animals, adoption["animal_id"])

    if animal:
        animal["available"] = False

