from datafirst.database import Database
from datafirst.models.database import Advisor, School

advisor_id = "advisor1@usc.edu"
advisor_name = "Advisor One"
advisor_email = advisor_id
advisor_organization = "USC"
advisor_semesters_participated = ["Fall 2023", "Fall 2022"]
advisor_semesters_parti = ["Fall 2023"]
advisor_school = School(
    name="Viterbi School of Engineering", url="https://viterbischool.usc.edu/", id=12
)
project_id = "2023-test-project1"

expected = Advisor(
    id=advisor_id,
    name=advisor_name,
    email=advisor_email,
    organization=advisor_organization,
    primary_school=advisor_school,
    is_formerly_primary_school=1,
    semesters_participated=advisor_semesters_participated,
    semesters_participated_as_chair=advisor_semesters_parti,
)


def test_get_advisor_by_id(database: Database) -> None:
    actual = database.get_advisor_by_id(advisor_id)
    assert actual == expected


def test_get_projects_by_advisor_id(database: Database) -> None:
    actual = database.get_projects_by_advisor_id(advisor_id)
    assert len(actual) == 3


def test_get_advisors(database: Database) -> None:
    actual = database.get_advisors()
    assert len(actual) == 2


def test_get_advisors_by_project_id(database: Database) -> None:
    actual = database.get_advisors_by_project_id(project_id=project_id)
    assert expected in actual
