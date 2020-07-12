import errno
import pickle

from courses import Courses


class Students:
    def __init__(self):

        try:
            with open("./Students.pkl", 'rb') as f:
                self.students: dict = pickle.load(f)
        except OSError as e:
            if e.errno == errno.ENOENT:
                self.students = {}
                with open("./Students.pkl", 'wb') as f:
                    pickle.dump(self.students, f)

    def enroll(self, **detail):
        c = Courses()
        c.enroll(detail["courses"])
        id = len(self.students) + 1
        self.students.update({f"{id}": {"id": str(id), **detail}})
        with open("./Students.pkl", 'wb') as f:
            pickle.dump(self.students, f)

    def addcourse(self, id, courses):
        if isinstance(courses, tuple):
            pass
        else:
            courses = [courses]

        c = Courses()
        c.enroll(courses)
        self.students[id]['courses'].update(courses)
        with open("./Students.pkl", 'wb') as f:
            pickle.dump(self.students, f)

    def update(self, **detail):
        id = detail['id']
        detail = {k: v for k, v in detail.items() if v}
        try:
            self.students.update({id: {**self.students[id], **detail}})
        except KeyError:
            print(f"id: {id} not found")
            exit(1)
        with open("./Students.pkl", 'wb') as f:
            pickle.dump(self.students, f)

    def detail(self):
        return [i.values() for i in self.students.values()]

    def getStudentsName(self):

        return [i["name"] for i in self.students.values()]

    def delete(self, id: str):
        try:
            data = self.students.pop(str(id))
        except KeyError:
            print(f"id: {id} not found")
            exit(1)
        with open("./Students.pkl", 'wb') as f:
            pickle.dump(self.students, f)

        return data['name']
