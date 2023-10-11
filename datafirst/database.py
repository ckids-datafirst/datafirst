import sqlite3
from pathlib import Path

from datafirst.models.database import (
    Advisor,
    Award,
    Project,
    SkillOrSoftware,
    Student,
    Topic,
)


def open_database(database_file: Path) -> sqlite3.Connection:
    """Open the database"""
    conn = sqlite3.connect(database_file)
    return conn


def get_cursor(conn: sqlite3.Connection) -> sqlite3.Cursor:
    """Get a cursor for the database"""
    return conn.cursor()


def close_database(conn: sqlite3.Connection):
    """Close the database"""
    conn.close()


def get_projects(cursor: sqlite3.Cursor) -> list[Project]:
    projects: list[Project] = []
    cursor.execute("SELECT * FROM project")
    for row in cursor.fetchall():
        project = Project(
            id=row[0],
            name=row[1],
            semester=row[2],
            year=row[3],
            project_overview=row[4],
            final_presentation=row[5],
            student_learning=row[6],
        )
        if project.id is None:
            raise ValueError("Project id is None")
        students = get_students_by_project_id(cursor, project.id)
        advisors = get_advisors_by_project_id(cursor, project.id)
        topics = get_topics_by_project_id(cursor, project.id)
        awards = get_awards_by_project_id(cursor, project.id)
        skills = get_skills_by_project_id(cursor, project.id)
        project.topics = topics
        project.skill_required = skills
        project.awards = awards
        project.advisors = advisors
        project.students = students
        projects.append(project)
    return projects


def get_skills_by_project_id(
    cursor: sqlite3.Cursor, project_id: str
) -> list[SkillOrSoftware]:
    skills: list[SkillOrSoftware] = []
    cursor.execute(
        "SELECT name, type FROM skill_or_software WHERE project_id = ?",
        (project_id,),
    )
    for row in cursor.fetchall():
        skill = SkillOrSoftware(name=row[0], type=row[1])
        skills.append(skill)
    return skills


def get_topics_by_project_id(cursor: sqlite3.Cursor, project_id: str) -> list[Topic]:
    topics: list[Topic] = []
    cursor.execute(
        "SELECT name FROM project_has_topic INNER JOIN topic ON topic.id = project_has_topic.topic_id WHERE project_id = ? ",
        (project_id,),
    )
    for row in cursor.fetchall():
        topic = Topic(name=row[0])
        topics.append(topic)
    return topics


def get_awards_by_project_id(cursor: sqlite3.Cursor, project_id: str) -> list[Award]:
    awards: list[Award] = []
    cursor.execute(
        "SELECT project_id, award FROM project_has_award WHERE project_id = ?",
        (project_id,),
    )
    for row in cursor.fetchall():
        award = Award(name=row[1])
        awards.append(award)
    return awards


def get_students_by_project_id(
    cursor: sqlite3.Cursor, project_id: str
) -> list[Student]:
    students: list[Student] = []
    cursor.execute(
        "SELECT * FROM student WHERE student.id IN (SELECT student_id FROM project_has_student WHERE project_id = ?)",
        (project_id,),
    )
    for row in cursor.fetchall():
        semesters_participated = get_semesters_by_student_id(cursor, row[0])
        student = Student(
            id=row[0],
            name=row[1],
            email=row[2],
            degree_program=row[3],
            school=row[4],
            semesters_participated=semesters_participated,
        )
        students.append(student)
    return students


def get_semesters_by_student_id(cursor: sqlite3.Cursor, student_id: int):
    if student_id:
        semester_participated: list[str] = []
        for project in get_projects_by_student_id(cursor, student_id):
            semester = f"{project.semester} {project.year}"
            if semester not in semester_participated:
                semester_participated.append(semester)

        return semester_participated


def get_semester_advisor_by_id(cursor: sqlite3.Cursor, advisor_id: str):
    if advisor_id:
        semester_participated: list[str] = []
        for project in get_projects_by_advisor_id(cursor, advisor_id):
            semester = f"{project.semester} {project.year}"
            if semester not in semester_participated:
                semester_participated.append(semester)

        return semester_participated


def get_advisors_by_project_id(
    cursor: sqlite3.Cursor, project_id: str
) -> list[Advisor]:
    advisors: list[Advisor] = []
    cursor.execute(
        "SELECT * FROM advisor WHERE advisor.id IN (SELECT advisor_id FROM project_has_advisor WHERE project_id = ?)",
        (project_id,),
    )
    for row in cursor.fetchall():
        advisor = Advisor(
            id=row[0],
            name=row[1],
            email=row[2],
            organization=row[3],
            primary_school=row[4],
        )
        if advisor.id is None:
            raise ValueError("Advisor id is None")
        advisor.semesters_participated = get_semester_advisor_by_id(cursor, advisor.id)
        advisors.append(advisor)
    return advisors


def get_advisors(cursor: sqlite3.Cursor) -> list[Advisor]:
    advisors: list[Advisor] = []
    cursor.execute("SELECT * FROM advisor")
    for row in cursor.fetchall():
        advisor = Advisor(
            id=row[0],
            name=row[1],
            email=row[2],
            organization=row[3],
            primary_school=row[4],
        )
        if advisor.id is None:
            raise ValueError("Advisor id is None")
        advisor.semesters_participated = get_semester_advisor_by_id(cursor, advisor.id)
        advisors.append(advisor)

    return advisors


def get_students(cursor: sqlite3.Cursor) -> list[Student]:
    students: list[Student] = []
    cursor.execute("SELECT * FROM student")
    for row in cursor.fetchall():
        semesters_participated = get_semesters_by_student_id(cursor, row[0])
        student = Student(
            id=row[0],
            name=row[1],
            email=row[2],
            degree_program=row[3],
            school=row[4],
            semesters_participated=semesters_participated,
        )
        students.append(student)
    return students


def get_projects_by_student_id(
    cursor: sqlite3.Cursor, student_id: int
) -> list[Project]:
    projects: list[Project] = []
    cursor.execute(
        "SELECT * FROM project WHERE project.id IN (SELECT project_id FROM project_has_student WHERE student_id = ?)",
        (student_id,),
    )

    for row in cursor.fetchall():
        project = Project(
            id=row[0],
            name=row[1],
            semester=row[2],
            year=row[3],
            project_overview=row[4],
            final_presentation=row[5],
            student_learning=row[6],
        )
        projects.append(project)
    return projects


def get_projects_by_advisor_id(
    cursor: sqlite3.Cursor, advisor_id: str
) -> list[Project]:
    projects: list[Project] = []
    cursor.execute(
        "SELECT * FROM project WHERE project.id IN (SELECT project_id FROM project_has_advisor WHERE advisor_id = ?)",
        (advisor_id,),
    )

    for row in cursor.fetchall():
        project = Project(
            id=row[0],
            name=row[1],
            semester=row[2],
            year=row[3],
            project_overview=row[4],
            final_presentation=row[5],
            student_learning=row[6],
        )
        projects.append(project)
    return projects
