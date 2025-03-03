from unicodedata import category


class Book_Menu:
    @classmethod
    def book_menu(cls):
        print("=-= [책 추천 시스템] =-=")
        print("1. 책 추천")
        print("2. 특정 책 조회")
        print("3. 전체 책 조회")
        print("4. 종료")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print()

class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

class Valid_Input:
    @classmethod
    def valid_input(cls, prompt, valid_input = None):
        while True:
            user_input = input(prompt).strip()

            if not user_input:
                print("공백이 입력되었습니다.")
                print()
            elif valid_input and user_input not in valid_input:
                print(f"{valid_input}외에 다른 것은 입력될 수 없습니다.")
                print()
            else:
                return user_input

class User_Choice:
    def __init__(self):
        self.book = Book_List()
        self.cate = Category_Input()

    def run(self):
        while True:
            self.menu = Book_Menu.book_menu()

            user_input = Valid_Input.valid_input("입력: ", ['1', '2', '3', '4'])
            self.user_choice(user_input)


    def user_choice(self, user_input):
        if user_input == '1':
            self.cate.recommend_category_input()

        elif user_input == '2':
            self.cate.scarch_title()

        elif user_input == '3':
            self.cate.all_books()

        elif user_input == '4':
            print("=-= 프로그램을 종료합니다 =-=")
            exit()

        else:
            print("1~4번을 제외한 숫자는 입력할 수 없습니다.")
            print()

class Category_Input:
    def __init__(self):
        self.book = Book_List()
        self.book_recommend = {}

    def recommend_category_input(self):
        recommend_input = Valid_Input.valid_input("추천을 원하는 키워드를 입력하세요: ")

        category_book = self.book.get_book_category(recommend_input)

        if category_book:
            for i, book in enumerate(category_book, 1):
                print(f"{i}. 책 제목: {book.title} / 저자: {book.author} / 카테고리: {book.category}")
            print()
        else:
            print(f"{recommend_input} 키워드가 존재하지 않습니다.")
            print()

    def scarch_title(self):
        title_input = Valid_Input.valid_input("조회할 책 제목을 입력하세요: ")

        for key, value in self.book.books.items():
            if isinstance(value, list):
                for book in value:  # 각 책에 대한 접근 , 복귀해야함
                    if title_input == book.title:
                        category_book = self.book.get_book_category(book.category)

                        print(f"{title_input}은(는) {book.category}에 존재합니다.")
                        print()
                        print("해당 카테고리의 책: ")

                        for b in category_book:
                            print(f"책 제목: {b.title} / 저자: {b.author}")
                        print()

                        break
            else:
                if title_input == value.title:
                    category_book = self.book.get_book_category(value.category)

                    print(f"{title_input}은(는) {value.category}에 존재합니다.")
                    print()
                    print("해당 카테고리의 책: ")

                    for b in category_book:
                        print(f"책 제목: {b.title} / 저자: {b.author}")
                    print()

                    break

        else:
            print(f"{title_input}은(는) 목록에 존재하지 않습니다.")

    def all_books(self):
        all_book = self.book.get_all_book()

        for k, v in self.book.books.items():
            if isinstance(v, list):
                for book in v:
                    print(f"{k} / 책 제목: {book.title} / 책 저자: {book.author}")
            print()

class Book_List:
    def __init__(self):
        self.books = {
            "과학": [
                Book("과학의 역사", "김철수", "과학"),
                Book("우주 탐험", "이영희", "과학"),
                Book("과학으로 보는 세상", "윤지혜", "과학")
            ],
            "기술": [
                Book("인공지능의 미래", "박지훈", "기술"),
                Book("데이터 분석 기법", "최민준", "기술"),
                Book("프로그래밍 실무", "김현우", "기술")
            ],
            "문학": [
                Book("문학과 철학", "한수진", "문학"),
                Book("문학적 상상력", "오지훈", "문학")
            ]
        }

    def get_book_category(self, category):
        return self.books.get(category, [])

    def get_all_book(self):
        return self.books

if __name__ == "__main__":
    User_Choice().run()