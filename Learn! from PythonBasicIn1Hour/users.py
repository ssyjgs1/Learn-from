# 09번 파일 연계 내용

class User :
    def __init__(self, name) :
        self.name = name
        self.likes = 0 # 좋아요를 한 번도 누르지 않았기 때문에 초기화

    def hit_like(self, video) :
        self.likes += 1
        video.increase_like()

        print(self.name, "liked : ", self.likes, "videos.")