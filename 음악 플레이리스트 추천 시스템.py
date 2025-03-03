class Music_Menu:
    def __init__(self):
        self.music_menu()

    def music_menu(self):
        print("=-= [힙합 장르 추천 리스트] =-=")
        print("1. 장르 추천")
        print("2. 종료")
        print()

class Start_Menu:
    def __init__(self):
        self.menu = Music_Menu()
        self.station = Music_Station()
        self.run()

    def run(self):
        while True:
            number = Valid_Input.valid_input("입력: ", ['1', '2'])

            self.sequence(number)

    def sequence(self, number):
        if number == '1':
            self.station.recommend_music()
        elif number == '2':
            print("=-= 프로그램 종료 =-=")
            exit()
        else:
            print("1, 2를 제외한 숫자는 입력할 수 없습니다.")

class Music_Station:
    def __init__(self):
        self.music = Music_List()

    def recommend_music(self):
        recommend_input = Valid_Input.valid_input("추천을 원하는 키워드를 입력: ")
        recommend_input = recommend_input.strip().lower()

        if recommend_input in self.music.music_list:
            print(f"{recommend_input} 장르 추천 리스트")
            for i, music in enumerate(self.music.music_list[recommend_input], 1):
                print(f"{i}. 제목: {music['title']} / 아티스트: {music['artist']} / genre: {music['genre']}")
                #category = self.music[recommend_input]




class Valid_Input:
    @classmethod
    def valid_input(cls, prompt, valid = None):
        user_input = input(prompt).strip()

        if not user_input:
            print("오류: 공백이 입력되었습니다.")
            print()
        elif valid and user_input not in valid:
            print(f"오류: {valid}이외에는 입력할 수 없습니다.")
            print()
        else:
            return user_input

class Music_List:
    def __init__(self):
        self.music_list = {
            "힙합": [
                {"title": "Sicko Mode", "artist": "Travis Scott", "genre": "힙합"},
                {"title": "God's Plan", "artist": "Drake", "genre": "힙합"},
            ],
            "팝": [
                {"title": "Shape of You", "artist": "Ed Sheeran", "genre": "팝"},
                {"title": "Bad Guy", "artist": "Billie Eilish", "genre": "팝"},
            ],
            "록": [
                {"title": "Bohemian Rhapsody", "artist": "Queen", "genre": "록"},
                {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "genre": "록"},
            ],
            "클래식": [
                {"title": "Canon in D", "artist": "Pachelbel", "genre": "클래식"},
                {"title": "Für Elise", "artist": "Beethoven", "genre": "클래식"},
            ],
        }

if __name__ == "__main__":
    Start_Menu()