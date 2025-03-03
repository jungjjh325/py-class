import re

class Library_Main_Menu: # 선택 화면 띄워주는 클래스
    @staticmethod
    def library_main_menu():
        print("=-= [도서관 프로그램] =-=")
        print("1. 책 추가")
        print("2. 책 삭제")
        print("3. 책 조회(검색)")
        print("4. 카테고리 별 책 조회")
        print("5. 전체 카테고리 책 조회")
        print("6. 종료")
        print("=-=-=-=-=-=-=-=-=-=-=-=")
        print()

class Valid_Input: # 입력 필터 클래스
    @classmethod
    def get_valid_input(cls, prompt, valid = None):
        while True:
            user_input = input(prompt).strip()

            if not user_input:
                print("오류: 공백이 입력되었습니다.")
                print()
            elif valid and user_input not in valid:
                print(f"오류: {valid}외에 다른 것은 입력될 수 없습니다.")
                print()
            else:
                return user_input

class Library_Books: # 기존에 만들어져 있는 딕셔너리가 있는 클래스 (상속 해줘야함)
    @classmethod
    def library_books(cls):
        return {
            "국어": [
                {"title": "국어의 정석", "author": "김민수", "year": 2010},
                {"title": "문법의 이해", "author": "박지현", "year": 2015},
                {"title": "현대문학 강의", "author": "이정훈", "year": 2018},
                {"title": "작문과 독서", "author": "최지우", "year": 2020},
            ],
            "과학": [
                {"title": "과학의 원리", "author": "이수민", "year": 2012},
                {"title": "물리학의 기초", "author": "한영수", "year": 2016},
                {"title": "생명의 신비", "author": "김나연", "year": 2019},
                {"title": "지구과학 탐구", "author": "박준형", "year": 2021},
            ],
            "동화": [
                {"title": "어린 왕자", "author": "앙투안 드 생텍쥐페리", "year": 1943},
                {"title": "피터 팬", "author": "제임스 배리", "year": 1911},
                {"title": "이상한 나라의 앨리스", "author": "루이스 캐럴", "year": 1865},
                {"title": "호두까기 인형", "author": "E.T.A. 호프만", "year": 1816},
            ]
        }

class Library_Manager:
    def __init__(self):
        self.books = Library_Books.library_books()  # 딕셔너리 클래스 참조

    def one_choice(self):
        print("책 추가 페이지입니다.")
        category_choice = Valid_Input.get_valid_input("카테고리 입력: ", ["국어", "과학", "동화"])  # 카테고리별 분류

        if category_choice in self.books: # 카테고리가 books 딕셔너리에 존재하는지 확인
            self.one_choice_repetition(self.books, category_choice) # 책 제목, 저자, 출판년도 판별 반복 클래스

        else:
            print(f"{category_choice}가 존재하지 않습니다.")
            print()

    def two_choice(self):
        print("책 삭제 페이지입니다.")
        category_choice = Valid_Input.get_valid_input("카테고리 입력: ", ["국어", "과학", "동화"])  # 카테고리별 분류

        if category_choice in self.books: # 카테고리가 books 딕셔너리에 존재하는지 확인
            print(f"=-= {category_choice} 카테고리 =-=")

            for book in self.books[category_choice]:
                print(f"제목: {book['title']} | 저자: {book['author']} | 출판년도: {book['year']}")
            print()

            self.two_choice_repetition(self.books, category_choice)

        else:
            print(f"{category_choice} 카테고리가 존재하지 않습니다.")
            print()

    def three_choice(self):
        print("책 조회(검색) 페이지입니다.")
        search_book = Valid_Input.get_valid_input("책 제목: ")

        book_name = [] # 빈 리스트 생성

        for category, all_books in self.books.items(): # 딕셔너리를 키랑 값으로 나눔

            if isinstance(all_books, list): # all_books가 리스트형인지 확인

                for book in all_books: # book이 방금 나눠진 값에 존재하는지 확인

                    if isinstance(book, dict) and 'title' in book: # 리스트가 각 요소가 딕셔너리 인지 확인, 딕셔너리일 경우 title키가 있는지도 추가 적으로 확인

                        if search_book in book['title']: # 책의 제목이 검색한 결과랑 같을 경우
                            book_name.append((category, book)) # 빈 리스트에 카테고리와 book을 추가

        if book_name:
            print("검색 결과")

            for category, book in book_name:
                print(f"카테고리: {category} - 제목: {book['title']} | 저자: {book['author']} | 출판년도: {book['year']} 이(가) 존재합니다.")
                print()

        else:
            print("검색 결과가 존재하지 않습니다.")
            print()

    def four_choice(self):
        print("카테고리 별 조회 페이지입니다.")
        category_choice = Valid_Input.get_valid_input("카테고리 입력: ", ["국어", "과학", "동화"])  # 카테고리별 분류

        if category_choice in self.books:
            print(f"카테고리: {category_choice}")
            for category, all_books in self.books.items():
                if category == category_choice:
                    for book in all_books:
                        print(f"제목: {book['title']} | 저자: {book['author']} | 출판년도: {book['year']}")
                    print()

        else:
            print("카테고리가 존재하지 않습니다.")
            print()

    def five_choice(self):
        print("전체 카테고리 조회 페이지입니다.")

        for categoty in self.books.keys():
            print(f"카테고리: {categoty}")
            for kind, all_books in self.books.items():
                for book in all_books:
                    if kind == categoty:
                        print(f"제목: {book['title']} | 저자: {book['author']} | 출판년도: {book['year']}")
            print()


    @staticmethod
    def one_choice_repetition(books, category_choice): # 책 제목, 저자, 출판년도 판별 반복 클래스
        title = Valid_Input.get_valid_input("책 제목 입력: ")
        author = Valid_Input.get_valid_input("책 저자 입력: ")

        if re.fullmatch(r"[a-zA-Z가-힣\s]+", author):  # import re로 받아줘야함, 패턴을 인식하면 저 패턴 외에는 다 걸러줌, 유연하지못함
            year = Valid_Input.get_valid_input("출판년도 입력: ")

            if year.isdigit():  # 출판년도는 숫자외에 아무것도 들어올 수 없음
                new_book = {"title": title, "author": author, "year": int(year)}  # 추가할 책 딕셔너리 화
                books[category_choice].append(new_book)  # category_choice에 국어, 과학, 동화중 하나임으로 카테고리 별로 책을 추가
                print(f"[{title} / {author} / {year}] {category_choice} 카테고리에 책이 추가되었습니다,")
                print()

            else:
                print("출판년도는 숫자만 입력가능합니다.")
                print()

        else:
            print("저자는 한글, 영어, 띄어쓰기만 작성할 수 있습니다.")
            print()

    @staticmethod
    def two_choice_repetition(books, category_choice):
        title = Valid_Input.get_valid_input("삭제할 책 제목 입력: ")
        author = Valid_Input.get_valid_input("삭제할 책 저자 입력: ")

        if re.fullmatch(r"[a-zA-z가-힣\s]+", author): # 저자는 한글, 영어, 띄어쓰기만 사용할 수 있다
            for book in books[category_choice]: # book이 딕셔너리에 존재하는지 확인
                if title == book['title'] and author == book['author']: # title과 book['title'] 그리고 author와 book['author']가 같다
                    books[category_choice].remove(book) # 카테고리에 있는 책을 삭제한다
                    print(f"카테고리: {category_choice} - 제목: {book['title']} | 저자: {book['author']} 책을 삭제하였습니다.")
                    print()
                    return

            print(f"{category_choice} - {title} | {author} 책이 존재하지 않습니다.")
            print()

        else:
            print("저자는 한글, 영어, 띄어쓰기만 작성할 수 있습니다.")
            print()

class User_Choice: # 유저가 선택하는 클래스
    def __init__(self):
        self.manager = Library_Manager() # 책 추가, 삭제 등을 맡은 클래스 참조

    def run(self):
        while True:
            Library_Main_Menu.library_main_menu()
            int_choice = Valid_Input.get_valid_input("입력: ", ['1', '2', '3', '4', '5', '6'])  # 필터 클래스 참조
            self.choice(int_choice)


    def choice(self, int_choice):

        if int_choice == '1':
            self.manager.one_choice()

        elif int_choice == '2':
            self.manager.two_choice()

        elif int_choice == '3':
            self.manager.three_choice()

        elif int_choice == '4':
            self.manager.four_choice()

        elif int_choice == '5':
            self.manager.five_choice()

        elif int_choice == '6':
            print("프로그램을 종료합니다.")
            exit()

        else:
            print("입력이 잘못 되었습니다.")
            print()

if __name__ == "__main__":
    choice = User_Choice() # 메뉴 입력 클래스
    choice.run() # 메뉴 입력 클래스의 메뉴 확인 및 입력란