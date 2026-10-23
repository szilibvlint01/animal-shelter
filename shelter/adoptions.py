import json


def load_adoptions(file_path):
    with open(file_path, "r",encoding="utf-8") as file:
        return json.load(file)


def save_adoptions(file_path, adoptions):
    with open (file_path, "w",encoding="utf-8") as file:
        json.dump(adoptions,file)


def create_adoption(animal, adopter_name):
    new_adoption = {"animal_id" : animal["id"],
                    "animal_name" : animal["name"],
                    "adopter" : adopter_name
                    }
    return new_adoption

def add_adoption(adoptions, adoption):
    adoptions.append(adoption)


def show_adoptions(adoptions):
    for adoption in adoptions:
        print(f"Animals id: {adoption["animal_id"]}")
        print(f"Animal name: {adoption["animal_name"]}")
        print(f"Adopter name: {adoption["adopter"]}")
