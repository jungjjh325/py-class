class Student:
    def __init__(self, student_name, student_id, scores):
        self.student_name = student_name
        self.student_id = student_id
        self.scores = scores

    def __str__(self):
        avg = self.avgrage()
        return f"=> 이름: {self.student_name}, 학번: {self.student_id}, 점수: {self.scores}, 평균: {avg}"

    def avgrage(self):
        return round(sum(self.scores.values()) / len(self.scores), 2)

class Main_Menu:
    def __init__(self):
        self.main_menu()

    def main_menu(self):
        print("[학생 성적 관리 시스템]")
        print("1. 학생 추가")
        print("2. 학생 삭제")
        print("3. 학생 검색")
        print("4. 전체 학생 출력")
        print("5. 종료")
        print()

class Choice_User(Main_Menu):
    def __init__(self, manager):
        self.manager = manager # Student_Manager(딕셔너리 클래스) 객체 참조
        super().__init__()
        self.choice_user()

    def choice_user(self):
        while True:
            user_input = self.valid_user("메뉴를 선택하세요: ", ['1', '2', '3', '4', '5'])

            if user_input.isdigit():
                if user_input == '1':
                    student_name = self.valid_user("학생 이름: ")

                    if student_name.isalpha():
                        student_id = self.valid_user("학번: ")

                        if student_id.isdigit and student_name not in self.manager.students and student_id not in self.manager.students:
                            student_score = self.valid_user("과목별 점수 (수학, 과학, 영어): ")
                            math_score, science_score, english_score = student_score.split()

                            if math_score.isdigit() and science_score.isdigit() and english_score.isdigit():
                                self.manager.add_student(student_name, student_id, math_score, science_score, english_score)

                        else:
                            print(f"{student_id}인 {student_name}의 학생은 이미 존재합니다.")
                            print()

                    else:
                        print("== 메뉴를 다시 선택해주세요 ==")
                        print()

                elif user_input == '2': # 삭제할 학생의 학번에 이상이 없는지 확인만 하고 넘기기
                    student_id = self.valid_user("삭제할 학생의 학번: ")

                    if student_id.isdigit(): # 학번에 숫자가 들어있으면 참

                        if student_id in self.manager.students: # 학번이 딕셔너리에 존재하면 참
                            self.manager.del_student(student_id)

                        else:
                            print(f"== {student_id} 학번이 존재하지 않습니다. ==")
                            print()
                    else:
                        print("== 메뉴를 다시 선택해주세요 ==")
                        print()

                elif user_input == '3': # 검색할 학번에 이상이 없는지만 판별
                    student_id = self.valid_user("검색할 학생의 학번: ")

                    if student_id.isdigit(): # 학번이 숫자면 참

                        if student_id in self.manager.students: # 학생이 딕셔너리에 존재하면 참
                            self.manager.search_student(student_id)

                    else:
                        print("== 메뉴를 다시 선택해주세요 ==")
                        print()
                
                elif user_input == '4': # 판별할게 없으므로 바로 넘기기
                    self.manager.all_student()

                elif user_input == '5': # 종료이므로 바로 넘김
                    self.manager.stop_menu()

                else: # 혹여 다른게 들어올 경우
                    print("잘못된 입력입니다.")
                    print()

    @staticmethod
    def valid_user(prompt, valid = None):
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

class Calculation:
    def __init__(self):
        self.students = {}

    def add_student(self, student_name, student_id, math_score, science_score, english_score):
        if student_id in self.students:
            print(f"{student_name}학생 이름이 이미 존재합니다.")
            print()
        else:
            scores = {"수학": math_score, "과학": science_score, "영어": english_score}
            self.students[student_id] = Student(student_name, student_id, scores)

            print(f"=> {student_name} 학생이 추가 되었습니다.")
            print()

    def del_student(self, student_id):
        student = self.students[student_id]  # 학번으로 학생 이름 파악

        print(f"{student_id} 학번 학생의 이름은 {student.student_name}입니다.")

        y_or_n = Choice_User.valid_user("삭제하시겠습니까? (y/n) ", ['y', 'Y', 'n', 'N'])

        if y_or_n in ['y', 'Y']:
            del self.students[student_id]

            print(f"=> {student_id} 학번 {student.student_name} 학생이 삭제되었습니다.")
            print()

        else:
            print("=> 삭제하기를 취소합니다.")
            print()

    def search_student(self, student_id):
        print(f"{self.students[student_id]}")
        print()

    def all_student(self):
        if not self.students:
            print("학생 목록이 비어있습니다.")
            print()
        else:
            for student_id, student in self.students.items():
                print(f"{self.students[student_id]}")
            print()

    def stop_menu(self):
        print("== 프로그램을 종료합니다. ==")
        print()
        exit()

class Student_Manager(Calculation, Choice_User):
    def __init__(self):
        super().__init__()
        super().__init__()
        self.student_manager()

    def student_manager(self):
        self.students = {
            "202301": Student(student_name="홍길동", student_id="202301", scores={"수학": 80, "과학": 90, "영어": 85}),
            "202302": Student(student_name="김영희", student_id="202302", scores={"수학": 70, "과학": 75, "영어": 80}),
            "202303": Student(student_name="이철수", student_id="202303", scores={"수학": 95, "과학": 85, "영어": 88}),
        }

if __name__ == "__main__":
    manager = Student_Manager()
    Choice_User(manager)