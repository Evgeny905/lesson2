class User:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.password = hash(self.nickname)
        self.age = age
        print (f"В классе User имя {self.nickname}, пароль {self.password}, возраст {self.age}")
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.videos_adult_mode = False
        self.current_user = None
    def log_in(self, nickname, password):
        self.nickname = nickname
        self.password = password
        for key, value in self.users.items():
            if self.nickname == key and self.password == value:
                self.current_user = self.nickname
            elif self.nickname != key:
                continue
            else:
                print(f'Пользователь {self.nickname} не найден')
    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        if self.users == {}:
            self.users[self.nickname] = self.password
            UrTube.log_out(self)
            UrTube.log_in(self, nickname, password)
        else:
            Flag = True
            for key, value in self.users.items():
                if self.nickname == key:
                    Flag = False
            if Flag:
                self.users[self.nickname] = self.password
                UrTube.log_out(self)
                UrTube.log_in(self, nickname, password)
            else:
                print(f"Пользователь {self.nickname} уже существует")


    def log_out(self):
        self.current_user = None
    def add(self, *video):
        for i in video:
            for key, value in self.videos.items():
                if i.title == key:
                    print(f"Видео {i.title} уже существует")
                else:
                    continue
            self.videos[i.title] = i.duration
            self.videos_adult_mode = i.adult_mode
        return self.videos
    def get_videos(self, Poisk):
        self.Poisk = Poisk
        Result_Poisk = []
        for key, value in self.videos.items():
            if key.lower().find(self.Poisk.lower()) == -1:
                continue
            else:
                Result_Poisk.append(key)
        return Result_Poisk
    def watch_video(self,title):
        self.title = title
        if self.current_user == None:
            print(f'Войдите в аккаунт, чтобы смотреть видео')
        elif self.videos_adult_mode == True and self.age < 18:
            print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            for key, value in self.videos.items():
                if key != self.title:
                    continue
                elif key == self.title:
                    import time, sys
                    for i in range(value + 1):
                        print(i, end=' ', )
                        sys.stdout.flush()
                        time.sleep(1)
                    print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
