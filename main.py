from shelter.animals import(
    load_animals,
    save_animals,
    show_animals,
    get_available_animals,
    find_animal_by_id,
    update_animal_status
    )

from shelter.adoptions import(
    load_adoptions,
    save_adoptions,
    create_adoption,
    add_adoption,
    show_adoptions
)

def main():
    animals = load_animals("data/animals.json")
    adoptions = load_adoptions("data/adoptions.json")

    while True:
        print()
        print("====ANIMAL SHELTER====")
        print()
        print("1. Show available animals.")
        print()
        print("2. Adopt animal.")
        print()
        print("3. Show adoptions.")
        print()
        print("4. Exit.")
        print()

        choice = input("Choose an option: ")

        match choice:
            case "1":
                available_animals = get_available_animals(animals)

                if available_animals:
                    show_animals(available_animals)
                else:
                    print("No available animals.")

            case "2":
                animal_id = input("Enter animal ID: ")

                if animal_id.isdigit():
                    animal_id = int(animal_id)
                    animal = find_animal_by_id(animals, animal_id)

                    if animal == None:
                        print("Animal not found.")

                    elif animal["available"] == False:
                        print("Animal already adopted.")

                    else:
                        adopter_name = input("What is your name? ")

                        adoption = create_adoption(animal, adopter_name)
                        add_adoption(adoptions, adoption)
                        update_animal_status(animals, adoption)

                        save_animals("data/animals.json", animals)
                        save_adoptions("data/adoptions.json", adoptions)

                        print("Adoption successful!")

                else:
                    print("Please enter a valid number.")


            case "3":
                if adoptions:
                    show_adoptions(adoptions)
                else:
                    print("No adoptions.")

            case "4":
                print()
                print("Goodbye!")
                print()
                break
            case _:
                print()
                print("Not available yet!")
                print()

main()