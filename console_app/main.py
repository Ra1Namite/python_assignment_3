from typing import List

import typer

from courses import Courses
from students import Students

app = typer.Typer()


@app.command()
def getcourses():
    c = Courses()
    for index, Cname in enumerate(c.getCoursesName()):
        typer.echo(f"{index + 1}. {Cname}")


@app.command()
def getstudents():
    s = Students()
    for index, Cname in enumerate(s.getStudentsName()):
        typer.echo(f"{index + 1}. {Cname}")


@app.command()
def enroll(name: str, deposit: int, courses: str):
    s = Students()
    c = Courses()
    if deposit != 20000 and deposit != 10000:
        raise typer.BadParameter("Deposit can only be 20000 or on installments of 10000")
    if courses.title() not in c.getCoursesName():
        raise typer.BadParameter("Course not found")
    s.enroll(name=name, deposit=deposit, courses={courses})
    typer.echo("Your Enrolled")


@app.command()
def update(id: str, name: str = None, deposit: int = None):
    s = Students()
    if deposit != 20000 and deposit != 10000:
        raise typer.BadParameter("Deposit can only be 20000 or on installments of 10000")
    s.update(id=str(id), name=name, deposit=deposit)
    typer.echo("Your Enrolled")


@app.command()
def addcourse(id: str, courses: List[str]):
    s = Students()
    c = Courses()
    for course in courses:
        if course.title() not in c.getCoursesName():
            raise typer.BadParameter("Course not found")
    s.addcourse(id=str(id), courses=courses)
    typer.echo("Your Enrolled")


@app.command()
def getstudentsdetail():
    s = Students()
    print("id   name   deposit   courses   remaining")
    for detail_list in s.detail():
        print(*[*detail_list,
                10000])  # 10000 hardcoded cause installments is with 10000 so remaining will always be 10000


@app.command()
def getcoursesdetail(course: str = None):
    c = Courses()
    print("Course    Enrolled     Description")
    for i in c.getCoursesDetail(course):
        print(*i)


@app.command()
def delete(id: int):
    s = Students()
    name = s.delete(id)
    print(f"{name} deleted")


def main():
    app()


if __name__ == "__main__":
    main()
