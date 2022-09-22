# type: ignore
import pytest
from . import factories
from students.models import Student


@pytest.mark.django_db
def test_create_student():
    """
    Test to ensure that creating a student works.
    """

    student1 = factories.StudentFactory(
        first_name="Gabriel",
        last_name="Rockson",
        student_id="20594513",
        index_number="3558018",
        level="400",
    )
    student2 = factories.StudentFactory(
        first_name="Gabriel",
        last_name="Rockson",
        other_names="Abeiku",
        student_id="23892342",
        index_number="38232837",
        level="300",
    )

    assert Student.objects.count() == 2

    assert Student.objects.first().first_name == student1.first_name
    assert (
        str(Student.objects.get(student_id="20594513"))
        == f"{student1.first_name} {student1.last_name}"
    )

    assert Student.objects.last().first_name == student2.first_name
    assert (
        str(Student.objects.get(student_id="23892342"))
        == f"{student2.first_name} {student2.other_names} {student2.last_name}"
    )
