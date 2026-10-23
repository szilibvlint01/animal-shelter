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
            case "4":
                print()
                print("Goodybe!")
                print()
                break
            case _:
                print()
                print("Not available yet!")
                print()

main()