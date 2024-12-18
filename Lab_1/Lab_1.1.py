import doctest


class Table:
    def __init__(self, material: str, height: float, length: float):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал стола (например, "дерево", "металл")
        :param height: Высота стола в сантиметрах
        :param length: Длина стола в сантиметрах

        Примеры:
        >>> table = Table("дерево", 75, 120)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not material:
            raise ValueError("Материал не может быть пустым")
        self.material = material

        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length

    def move_table(self, new_position: str) -> None:
        """
        Перемещение стола в новую позицию.

        :param new_position: Новая позиция стола (например, "гостиная", "кухня")

        Примеры:
        >>> table = Table("дерево", 75, 120)
        >>> table.move_table("гостиная")
        """
        ...

    def adjust_height(self, new_height: float) -> None:
        """
        Регулировка высоты стола.

        :param new_height: Новая высота стола в сантиметрах
        :raise ValueError: Если новая высота меньше или равна нулю

        Примеры:
        >>> table = Table("металл", 75, 120)
        >>> table.adjust_height(80)
        """
        ...


class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева (например, "дуб", "береза")
        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах

        Примеры:
        >>> tree = Tree("дуб", 5.5, 10)
        """
        if not isinstance(species, str) or not species:
            raise ValueError("Вид дерева должен быть непустой строкой")
        self.species = species

        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст дерева должен быть неотрицательным целым числом")
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст и высоту дерева.

        :param years: Количество лет роста
        :raise ValueError: Если количество лет роста отрицательное

        Примеры:
        >>> tree = Tree("береза", 5, 7)
        >>> tree.grow(3)
        """
        ...

    def shed_leaves(self) -> None:
        """
        Симулирует опадание листьев у дерева.

        Примеры:
        >>> tree = Tree("дуб", 8, 15)
        >>> tree.shed_leaves()
        """
        ...


class FacebookAccount:
    def __init__(self, username: str, age: int, friends_count: int):
        """
        Создание и подготовка к работе объекта "FacebookAccount"

        :param username: Имя пользователя
        :param age: Возраст пользователя
        :param friends_count: Количество друзей

        Примеры:
        >>> account = FacebookAccount("user123", 25, 150)
        """
        if not isinstance(username, str) or not username:
            raise ValueError("Имя пользователя должно быть непустой строкой")
        self.username = username

        if not isinstance(age, int) or age <= 0:
            raise ValueError("Возраст должен быть положительным целым числом")
        self.age = age

        if not isinstance(friends_count, int) or friends_count < 0:
            raise ValueError("Количество друзей должно быть неотрицательным целым числом")
        self.friends_count = friends_count

    def add_friend(self, friend_name: str) -> None:
        """
        Добавляет друга в список друзей.

        :param friend_name: Имя друга
        :raise ValueError: Если имя друга пустое

        Примеры:
        >>> account = FacebookAccount("user123", 25, 150)
        >>> account.add_friend("new_friend")
        """
        ...

    def post_status(self, status: str) -> None:
        """
        Публикует статус.

        :param status: Текст статуса
        :raise ValueError: Если статус пустой

        Примеры:
        >>> account = FacebookAccount("user123", 25, 150)
        >>> account.post_status("Hello, world!")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
