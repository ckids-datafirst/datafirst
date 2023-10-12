from datafirst.database import Database
from datafirst.models.database import School

advisor_id = "advisor1@usc.edu"
advisor_name = "Advisor One"
advisor_email = advisor_id
advisor_organization = "USC"
advisor_semesters_participated = ["Fall 2023", "Fall 2022"]
advisor_school = School(
    name="Viterbi School of Engineering", url="https://viterbischool.usc.edu/", id=12
)


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
