# Написать платформу для прослушивания музыки
'''
1) Класс Пользователь с юзернеймом, возраст, эл. почтой и подпиской(по дефолту - Без подписки, если подписка не оформлена, то с каждым прослушиванием появялется реклама, спам), плейлист(по дефолту - пустой список). Можно дополнительно еще пароль сделать, с валидацией, вся информация должна быть приватной.
Нужно провалидировать все данные(почту на наличие @, пароль, возраст)

- Метод для оформления подписки, для добавления в пейлист песни, 
- метод для прослушивания песни, 
- метод который прослушивает весь плейлист по очередно
'''
class User:
    def __init__(self, username, age, email, password=None):
        self.__username = username
        self.__age = self.__validate_age(age)
        self.__email = self.__validate_email(email)
        self.__password = self.__validate_password(password) if password else None
        self.__subscription = "Без подписки"
        self.__playlist = []
        self.status = True

    def __validate_age(self, age):
        try:
            age = int(age)
            if age < 0:
                raise ValueError("Возраст не может быть отрицательным")
            return age
        except ValueError:
            raise ValueError("Неверный формат возраста")

    def __validate_email(self, email):
        if "@" not in email:
            raise ValueError("Некорректный адрес электронной почты")
        return email

    def __validate_password(self, password):
        if len(password) <= 8:
            raise ValueError('Некорректный пароль')
        else:
            return password

    def subscribe(self, subscription):
        if self.status:
            self.__subscription = subscription
        else:
            return 'Ты в черном списке!'

    def add_to_playlist(self, song):
        if self.status:
            self.__playlist.append(song)
        else:
            return 'Ты в черном списке!'
        

    def listen_to_song(self, song):
        if self.status:
        
            print(f"Прослушивается песня: {song}")
        else:
            return 'Ты в черном списке!'
    def listen_to_playlist(self):
        if self.status:
            
            if not self.__playlist:
                print("Плейлист пустой")
            else:
                for song in self.__playlist:
                    self.listen_to_song(song)
        else:
            return 'Ты в черном списке!'


'''
2) Класс жанр c названием
'''
class Genre:
    def __init__(self, name) -> None:
        self.name = name



'''
3) Класс музыка с названием, автором, жанром, длительностью
'''
class Music:
    def __init__(self, name, autor, genre, duration) -> None:
        self.name = name
        self.autor = autor
        self.genre = genre
        self.duration = duration
'''
4) Класс работник, который наследуется от Пользователя, но у него есть доп атрибут - роль (например админ), и платформа где он работает
'''

class Warker(User):
    def __init__(self, username, age, email, password, platform):
        super().__init__(username, age, email, password)
        self.role = 'admin'
        self.platform = platform


'''
5) Класс платформа для прослушивания музыки, например - Spotify, у которого должны быть списки песен, жанры, список пользователей с полпиской и без

- методы для  просмотра всех песен,
- методы для просмотра песен по определенному жанру,
- метод для оформления подписки у пользователя, если
- метод для поиска песни по названию
- метод для добавления определенной песни в плейлист пользователя
- метод удаления, добавления песни, жанра из списка Платформы, которую может сделать только админ этой платформы
- метод блокировки, удаления пользователя, если это потребуется
'''

class Spotify:
    def __init__(self, ls_music=[], ls_genre=[], ls_users=[], black_lict = []):
        self.ls_music = ls_music
        self.ls_genre = ls_genre
        self.ls_users = ls_users
        self.black_list = black_lict


    def search_music(self):
        for i in self.ls_music:
            print(i.name, i.genre, i.autor)

    def search_misuc_genre(self, genre):
        for i in self.ls_music:
            if genre == i.genre:
                print(i.name)

    def add_subsc(self, user):
        user.subscribe('Подписка оформлена!')
        return f'У {user.name} подписка оформлена'
    
    def search_music_by_name(self, name):
        for i in self.ls_music:
            if name in i.name:
                print(i.name, i.autor)

    def add_music_to_playlist_user(self, music, user):
        user.add_to_playlist(music)


    def add_delete_music(self, music, admin):
        if admin.role == 'admin':
            if music in self.ls_music:
                self.ls_music.remove(music)
                return f'{music} is removed'

            else:
                self.ls_music.apppend(music)
                return f'{music} is appended'
        else:
            return 'permission is denied!'

    def block_or_delete_user(self, comand, user, admin):
        if admin.role == 'admin':
            if comand == 'block':
                user.status = False
                self.black_list.append(user)
            else:
                self.ls_users.remove(user)


  



    

    

