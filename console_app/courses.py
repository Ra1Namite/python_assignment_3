import pickle


class Courses:
    def __init__(self):
        with open("./Courses.pkl", 'rb') as f:
            self.courses: dict = pickle.load(f)

    def getCoursesName(self):
        return self.courses.keys()

    def getCoursesDetail(self, course):
        if course and course.title() in self.courses:
            return [self.courses[course.title()].values()]
        elif course:
            print(f"Course:{course} not found")
        return [i.values() for i in self.courses.values()]

    def enroll(self, courses):
        for c in courses:
            self.courses[c.title()]["Enrolled"] += 1
        with open("./Courses.pkl", 'wb') as f:
            pickle.dump(self.courses, f)
