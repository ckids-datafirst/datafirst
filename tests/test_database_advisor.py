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


second_advisor_id = "advisor2@usc.edu"
second_advisor_name = "Advisor Two"
second_advisor_email = second_advisor_id
second_advisor_organization = "USC"
second_advisor_semesters_participated = ["Fall 2023", "Fall 2022"]
second_advisor_semesters_parti = ["Fall 2023"]
second_advisor_school = None

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

expected2 = Advisor(
    id=second_advisor_id,
    name=second_advisor_name,
    email=second_advisor_email,
    organization=second_advisor_organization,
    primary_school=second_advisor_school,
    is_formerly_primary_school=1,
    semesters_participated=second_advisor_semesters_participated,
    semesters_participated_as_chair=second_advisor_semesters_parti,
)


def test_get_advisor_by_id(database: Database) -> None:
    actual = database.get_advisor_by_id(advisor_id)
    assert actual == expected
    actual2 = database.get_advisor_by_id(second_advisor_id)
    assert actual2 == expected2


def test_get_projects_by_advisor_id(database: Database) -> None:
    actual = database.get_projects_by_advisor_id(advisor_id)
    assert len(actual) == 3
    actual2 = database.get_projects_by_advisor_id(second_advisor_id)
    assert len(actual2) == 2


def test_get_advisors(database: Database) -> None:
    actual = database.get_advisors()
    assert len(actual) == 2


def test_get_advisors_by_project_id(database: Database) -> None:
    actual = database.get_advisors_by_project_id(project_id=project_id)
    assert expected in actual
