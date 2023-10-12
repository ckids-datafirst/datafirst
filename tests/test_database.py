from datafirst.database import Database

advisor_id = "advisor1@usc.edu"
project_id = "2023-test-project1"
student_id = 1
school_id = 1
topic_id = 1


def test_get_skills_by_project_id(database: Database) -> None:
    database.get_skills_by_project_id(project_id=project_id)


def test_get_topics_by_project_id(database: Database) -> None:
    database.get_topics_by_project_id(project_id=project_id)


def test_get_awards_by_project_id(database: Database) -> None:
    database.get_awards_by_project_id(project_id=project_id)


def test_get_students_by_project_id(database: Database) -> None:
    database.get_students_by_project_id(project_id=project_id)


def test_get_advisors_by_project_id(database: Database) -> None:
    database.get_advisors_by_project_id(project_id=project_id)


def test_get_projects(database: Database) -> None:
    database.get_projects()


def test_get_projects_by_student_id(database: Database) -> None:
    database.get_projects_by_student_id(1)


def test_get_projects_by_advisor_id(database: Database) -> None:
    database.get_projects_by_advisor_id(advisor_id)


def test_get_advisors(database: Database) -> None:
    database.get_advisors()


def test_get_students(database: Database) -> None:
    database.get_students()


def test_get_semester_advisor(database: Database) -> None:
    database.get_semester_advisor_by_id(advisor_id)
