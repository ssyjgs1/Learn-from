# 09번 파일 연계 내용

class Video :

    def __init__(self, title, description) :
        self.title = title
        self.description = description
        self.likes = 0 # 초기화

    def increase_like(self) :
        self.likes += 1 # self.likes = self.likes + 1
        print(self.title, "likes : ", self.likes)