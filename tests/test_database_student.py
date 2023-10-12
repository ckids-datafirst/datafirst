from datafirst.database import Database
from datafirst.models.database import Student

student = Student(
    id="1",
    name="Fake User",
    email="fake@usc.edu",
    degree_program="Computer Science",
    school="Viterbi School of Engineering",
    github_username="mosoriobnew",
    last_participation=None,
    semesters_participated=["Fall 2023"],
)


def test_get_student_by_id(database: Database) -> None:
    actual = database.get_student_by_id("1")
    assert actual == student


def test_get_students(database: Database) -> None:
    actual = database.get_students()
    assert len(actual) == 2
    assert actual[0] == student
