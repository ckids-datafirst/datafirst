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
project_overview = "Lots of personal data can be obtained from wearable devices such as smart watches.  This data can be used to improve health, for example to learn to detect health problems and to check whether people adhere to doctor’s exercise recommendations.  This project will conduct a thorough study of the ethical issues in using AI systems in this domain, with recommendations of how AI systems for smart health should be designed with ethical considerations in mind."
student_learning = "What kinds of health-related data can be captured through wearable devices, what kinds of analyses are possible, privacy and ethical aspects of personal applications for smart health."
student_id = 1
school_id = 1
website = "website1.com"
topic_id = 1


def test_get_project_by_id(database: Database) -> None:
    actual = database.get_project_by_id(project_id)
    assert actual.id == project_id
    if actual.advisors:
        assert len(actual.advisors) == 2
    if actual.students:
        assert len(actual.students) == 1
    if actual.skill_required:
        assert len(actual.skill_required) == 1
    if actual.awards:
        assert len(actual.awards) == 1
    if actual.topics:
        assert len(actual.topics) == 1
    assert actual.website == website
    assert actual.name == "Project Test 1"


def test_get_projects(database: Database) -> None:
    actual = database.get_projects()
    assert len(actual) == 3


def test_get_projects_by_student_id(database: Database) -> None:
    projects = database.get_projects_by_student_id(1)
    assert len(projects) == 1
    assert projects[0].id == project_id
    assert projects[0].name == "Project Test 1"
