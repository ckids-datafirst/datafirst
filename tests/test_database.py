import sqlite3

import pytest

from datafirst.database import (
    get_advisors,
    get_advisors_by_project_id,
    get_awards_by_project_id,
    get_projects,
    get_projects_by_advisor_id,
    get_projects_by_student_id,
    get_semester_advisor_by_id,
    get_skills_by_project_id,
    get_students,
    get_students_by_project_id,
    get_topics_by_project_id,
)

advisor_id = "advisor1@usc.edu"
project_id = "2023-test-project1"
student_id = 1
school_id = 1
topic_id = 1


def test_get_skills_by_project_id(cursor: sqlite3.Cursor):
    get_skills_by_project_id(cursor, project_id=project_id)


def test_get_topics_by_project_id(cursor: sqlite3.Cursor):
    get_topics_by_project_id(cursor, project_id=project_id)


def test_get_awards_by_project_id(cursor: sqlite3.Cursor):
    get_awards_by_project_id(cursor, project_id=project_id)


def test_get_students_by_project_id(cursor: sqlite3.Cursor):
    get_students_by_project_id(cursor, project_id=project_id)


def test_get_advisors_by_project_id(cursor: sqlite3.Cursor):
    get_advisors_by_project_id(cursor, project_id=project_id)


def test_get_projects(cursor: sqlite3.Cursor):
    get_projects(cursor)


def test_get_projects_by_student_id(cursor: sqlite3.Cursor):
    get_projects_by_student_id(cursor, 1)


def test_get_projects_by_advisor_id(cursor: sqlite3.Cursor):
    get_projects_by_advisor_id(cursor, advisor_id)


def test_get_advisors(cursor: sqlite3.Cursor):
    get_advisors(cursor)


def test_get_students(cursor: sqlite3.Cursor):
    get_students(cursor)


def test_get_semester_advisor(cursor: sqlite3.Cursor):
    get_semester_advisor_by_id(cursor, advisor_id)
