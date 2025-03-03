'''
1. 프로그램 기능
책을 관리하기 위해 Book 클래스를 생성하세요.
책의 제목, 저자, 출판년도를 저장하세요.
딕셔너리를 사용하여 책의 제목을 키(key), Book 객체를 값(value)으로 저장하세요.
아래의 기능을 구현하세요.
책 추가: 새로운 책을 추가하세요.
책 삭제: 제목을 입력받아 해당 책을 삭제하세요.
책 검색: 제목을 입력받아 해당 책의 정보를 출력하세요.
전체 목록 출력: 저장된 모든 책의 정보를 출력하세요.
'''
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class bookmanager:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, year):
        if title in self.books:
            print(f"{title}의 책은 이미 존재합니다.")
            print()
        else:
            self.books[title] = Book(title, author, year)

            print(f"{title} 책이 추가 되었습니다.")
            print()

    def del_book(self, title):
        if title not in self.books:
            print(f"{title}의 책이 존재하지 않습니다")
            print()
        else:
            del self.books[title]

            print(f"{title}이 삭제되었습니다.")
            print()

    def search_book(self, title):
        if title in self.books:
            book = self.books[title]

            print(f"제목: {book.title}, 저자: {book.author}, 출판년도: {book.year}")
            print()
        else:
            print(f"{title}의 책이 존재하지 않습니다.")
            print()

    def list_book(self):
        if not self.books:
            print("책 목록이 비어 있습니다.")
            print()
        else:
            for key, value in self.books.items():
                print(f"제목: {value.title}, 저자: {value.author}, 출판년도: {value.year}")
            print()

class book_list_manager(bookmanager):
    def __init__(self):
        super().__init__()
        self.book_list()

    def book_list(self):
        # 딕셔너리 키는 책 제목, 값은 Book 객체
        self.books = {
            "해리포터": Book(title="해리포터", author="J.K. 롤링", year=1997),
            "반지의 제왕": Book(title="반지의 제왕", author="J.R.R. 톨킨", year=1954),
            "어린 왕자": Book(title="어린 왕자", author="앙투안 드 생텍쥐페리", year=1943)
        }


class lib:
    def __init__(self, manager):
        self.manager = manager

    def menu(self):
        print("[도서 관리 시스템]")
        print("1. 책 추가")
        print("2. 책 삭제")
        print("3. 책 검색")
        print("4. 전체 목록 출력")
        print("5. 종료")
        print()

    def choice_user(self):
        while True:
            self.menu()

            self.int_modifying = self.get_int_valid_input("숫자 입력: ", ['1', '2', '3', '4'])

            if self.int_modifying == '1':
                title = input("추가할 책 제목: ").strip()
                author = input("추가할 책 저자: ").strip()
                year = int(input("추가할 책 출판년도: ").strip())
                self.manager.add_book(title, author, year)
            elif self.int_modifying == '2':
                title = input("삭제할 책 제목: ").strip()
                self.manager.del_book(title)
            elif self.int_modifying == '3':
                title = input("조회할 책 검색: ").strip()
                self.manager.search_book(title)
            elif self.int_modifying == '4':
                self.manager.list_book()
            elif self.int_modifying == '5':
                break
            else:
                print("잘못된 입력")


    @staticmethod
    def get_int_valid_input(prompt, valid_input = None):
        while True:
            user_input = input(prompt).strip()

            if not user_input:
                print("공백이 입력되었습니다.")
                print()
            elif valid_input and user_input not in valid_input:
                print(f"{valid_input} 외에 다른 것은 입력될 수 없습니다.")
                print()
            elif user_input.isdigit():
                return user_input
            else:
                print("유효한 입력값이 아닙니다.")
                print()

if __name__ == "__main__":
    manager = book_list_manager()
    library = lib(manager)
    library.choice_user()