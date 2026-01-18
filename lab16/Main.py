from Login import Login
from LoginHandler import LoginHandler


def main():
    max_elements = 2

    # Initerar ett LoginHandler objekt
    login_list = LoginHandler(max_elements)

    # Initirerar ett Login objekt och lägger till e-post i listan
    login1 = Login("homer@simpson.se", "homer2022")
    ok = login_list.add_new(login1)
    if ok:
        print(f"Object added. Num of elements: {login_list.get_numers_of_elements()}")
    else:
        print("Object could not be added.")

    # Utskrift för att se listan
    print("Listan just nu: ")
    for i, login in enumerate(login_list.login_list):
        print(f"Index {i}:  {login.id}")

    # Initirerar ett Login objekt och lägger till e-post i listan
    login2 = Login("filip@email.com", "password")
    ok = login_list.add_new(login2)
    if ok:
        print(f"Object added. Num of elements: {login_list.get_numers_of_elements()}")
    else:
        print("Object could not be added.")

    # Utskrift för att se listan
    print("Listan just nu: ")
    for i, login in enumerate(login_list.login_list):
        print(f"Index {i}:  {login.id}")

    # Förösker ta bort ett element som inte finns i listan då den just nu har enbart 2 objekt [0,1]
    ok = login_list.remove_elements_at(3)
    if ok:
        print(f"Object deleted. Num of elements: {login_list.get_numers_of_elements()}")
    else:
        print("Object could not be deleted.")

    # Tar bort index 1 från listan
    ok = login_list.remove_elements_at(1)
    if ok:
        print(f"Object deleted. Num of elements: {login_list.get_numers_of_elements()}")
    else:
        print("Object could not be deleted.")

    # Utskrift för att se listan
    print("Listan just nu: ")
    for i, login in enumerate(login_list.login_list):
        print(f"Index {i}:  {login.id}")


if __name__ == "__main__":
    main()
