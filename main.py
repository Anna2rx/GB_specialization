import json
from datetime import datetime

notes = []


class Note:
    LAST_ID = 1

    def __init__(self, title, body, id=None, date=None):
        self.__title = title
        self.__body = body
        self.__last_date = str(datetime.now()) if date is None else date
        self.__id = Note.LAST_ID if id is None else id
        Note.LAST_ID += 1

    @property
    def date(self):
        return self.__last_date

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def body(self):
        return self.__body

    @title.setter
    def title(self, title):
        self.__title = title

    @body.setter
    def body(self, body):
        self.__body = body

    @date.setter
    def date(self, date):
        self.__last_date = str(date)

    @staticmethod
    def input_body():
        print("Введите текст заметки. Для окончания ввода нажмите клавишу Enter дважды.")
        body = []

        while True:
            inp = input()
            if not inp:
                break
            body.append(inp)

        body_text = '\n'.join(body)
        return body_text

    @staticmethod
    def get_last_id():
        pass

    def to_dict(self):
        return {"id": self.id, "date": self.date, "title": self.title,
                "body": self.body}

    def __str__(self):
        return f"""ID: {self.id}, LAST MODIFIED DATE: {self.date}
TITLE: {self.title}
BODY:
{self.body}"""


FILE_NAME = 'notes.json'


def save():
    notes_json = [note.to_dict() for note in notes]
    notes_json.sort(key=lambda note: note["id"])
    data = json.dumps(notes_json)
    with open('notes.json', 'w') as f:
        json.dump(data, f)


def load():
    try:
        with open(FILE_NAME, ) as json_data:
            data = json.loads(json.load(json_data))

            print("Список заметок, импортированный из JSON:\n")
            for note in data:
                new_note = Note(**note)
                print(new_note, '\n')
                notes.append(new_note)
            input("Нажмите клавишу Enter для начала работы приложения.")
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        print("Список заметок пуст!")


def main():
    EXIT, ADD, EDIT, REMOVE, SAVE, READ, READ_DATE = map(str, range(7))

    load()

    choice = None
    while choice != EXIT:
        print \
            ("""
                Заметки

                0 - Выйти
                1 - Создать заметку
                2 - Редактировать заметку
                3 - Удалить заметку
                4 - Сохранить заметки в json
                5 - Посмотреть весь список заметок
                6 - Посмотреть все заметки за конкретную дату
                """)
        choice = input("Ваш выбор: ")

        if choice == EXIT:
            if notes:
                save()
                print("Заметки сохранены в JSON. До свидания!")
            else:
                print("До свидания!")
            break

        elif choice == ADD:
            title = input("Введите заголовок заметки в одну строку: ")
            while not title:
                title = input("Заголовок не может быть пустым! Введите заголовок заметки в одну строку: ")

            # при этом тело может быть пустым
            body = Note.input_body()

            notes.append(Note(title, body))
            print("Заметка успешно добавлена")

        elif choice == EDIT:
            if not notes:
                print("Список заметок пуст!")
                continue
            print()
            print(*notes, sep='\n' * 2)
            note_id = input("\nВведите ID заметки, которую хотите редактировать: ")
            for note in notes:
                if str(note.id) == note_id:
                    title = input("Введите новый заголовок или нажмите Enter, если хотите оставить его прежним: ")
                    if title:
                        note.title = title
                    body = Note.input_body()
                    note.body = body
                    note.date = datetime.now()
                    print("Заметка успешно отредактирована!")
                    break
            else:
                print("Заметка с таким ID не найдена!")

        elif choice == REMOVE:
            if not notes:
                print("Список заметок пуст!")
                continue
            print()
            print(*notes, sep='\n' * 2)
            note_id = input("\nВведите ID заметки, которую хотите удалить: ")
            for note in notes:
                if str(note.id) == note_id:
                    notes.remove(note)
                    print("Заметка успешно удалена!")
                    break
            else:
                print("Заметка с таким ID не найдена!")

        elif choice == SAVE:
            save()
            print("Заметки успешно сохранены!")

        elif choice == READ:
            if not notes:
                print("Список заметок пуст!")
                continue
            print()
            print(*notes, sep='\n' * 2)

            note_id = input("\nВведите ID заметки, которую хотите посмотреть подробнее или нажмите клавишу Enter для "
                            "возврата в меню: ")
            if note_id:
                for note in notes:
                    if str(note.id) == note_id:
                        print()
                        print(note)
                        break
                else:
                    print("Заметка с таким ID не найдена!")

        elif choice == READ_DATE:
            date = input("Введите дату в формате YYYY-MM-DD: ")
            notes_for_date = list(filter(lambda note: date in note.date, notes))

            print()
            if notes_for_date:
                print(*notes_for_date, sep='\n' * 2)
            else:
                print("За данную дату нет заметок!")
            print()

        else:
            print("\nВ меню нет пункта", choice)

        input("\nНажмите клавишу Enter для возврата в меню.")


if __name__ == '__main__':
    main()
