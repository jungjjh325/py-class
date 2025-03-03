import re

class Film:
    def __init__(self, film_title, screening):
        self.film_title = film_title
        self.screening = screening

class Film_Menu:
    @classmethod
    def menu(cls):
        print("=-= [영화 대여 시스템] =-=")
        print("1. 영화 대여")
        print("2. 영화 반납")
        print("3. 특정 영화 조회")
        print("4. 전체 영화 조회")
        print("5. 종료")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print()

class Choice:
    def __init__(self):
        self.film_list = Film_List()
        self.rant_film = {}

    def rant_choice(self):
        customer_input = Valid_input.valid_input("대여한 영화제목을 입력하세요: ")

        if re.fullmatch(r"[a-zA-Z기-힣\s]+", customer_input):
            film = self.film_list.films.get(customer_input)
            if film:
                film.screening = "Ranted"
                print(f"{customer_input}을(를) 성공적으로 대여 완료 하였습니다.")
                print()
            else:
                print(f"{customer_input}은 이미 대여되어있거나 존재하지 않습니다.")
                print()
        else:
            print("영화제목은 한글, 영어, 띄어쓰기만 작성할 수 있습니다.")
            print()

    def return_choice(self):
        customer_input = Valid_input.valid_input("반납할 영화제목을 입력하세요: ")

        if re.fullmatch(r"[a-zA-Z기-힣\s]+", customer_input):
            film = self.film_list.films.get(customer_input)
            if film:
                film.screening = "Available"
                print(f"{customer_input}을(를) 무사히 반납 완료 하였습니다.")
                print()
            else:
                print(f"{customer_input}은 대여 가능한 영화이거나 존재하지 않습니다")
                print()
        else:
            print("영화 제목은 한글, 영어, 띄어쓰기만 작성할 수 있습니다.")
            print()

    def search_film(self):
        customer_input = Valid_input.valid_input("검색할 영화 제목을 입력하세요: ")

        if re.fullmatch(r"[a-zA-Z기-힣\s]+", customer_input):
            film = self.film_list.films.get(customer_input)
            if film:
                print(f"{customer_input}는 {film.screening} 상태입니다.")
                print()
            else:
                print(f"{customer_input}은 존재하지 않는 영화입니다.")
                print()
        else:
            print("영화 제목은 한글, 영어, 띄어쓰기만 작성할 수 있습니다.")
            print()

    def films_list(self):
        for k, v in self.film_list.films.items():
            print(f"{k} - {v.screening}")
        print()

class Customer_Choice:
    def __init__(self):
        self.menu = Film_Menu.menu()
        self.rant = Choice()
        self.customer_choice()

    def customer_choice(self):
        while True:
            customer_input = Valid_input.valid_input("입력 (1~5): ", ['1', '2', '3', '4', '5'])

            if customer_input == '1':
                self.rant.rant_choice()

            elif customer_input == '2':
                self.rant.return_choice()

            elif customer_input == '3':
                self.rant.search_film()

            elif customer_input == '4':
                self.rant.films_list()

            elif customer_input == '5':
                print("프로그램을 종료하겠습니다.")
                exit()

            else:
                print("예기치 않은 입력입니다.")
                print()

class Valid_input:
    @classmethod
    def valid_input(cls, prompt, valid = None):
        while True:
            customer_input = input(prompt).strip()

            if not customer_input:
                print("공백이 입력되었습니다.")
                print()
            elif valid and customer_input not in valid:
                print(f"{valid}외에 입력을 받을 수 없습니다.")
                print()
            else:
                return customer_input

class Film_List:
    def __init__(self):
        self.films = {
            "Titanic": Film("Titanic", "Available"),
            "Inception": Film("Inception", "Available"),
            "Interstellar": Film("Interstellar", "Rented"),
            "Avatar": Film("Avatar", "Available")
        }

    def get_film_title(self, film_title):
        return self.films.get(film_title) # 찾는 것만 반환

    def get_all_films(self): # 전체 반환
        return self.films

if __name__ == "__main__":
    Customer_Choice()