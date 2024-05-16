from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Pesho")
        self.student_with_courses = Student("Gosho", {"math": ["math is cool"]})

    def test_class_student_correct_initiation_without_courses(self):
        self.assertEqual("Pesho", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_class_student_correct_initiation_with_courses(self):
        self.assertEqual("Gosho", self.student_with_courses.name)
        self.assertEqual({"math": ["math is cool"]}, self.student_with_courses.courses)

    def test_enroll_method_course_already_enrolled_update_notes(self):
        result = self.student_with_courses.enroll("math", ["just joking", "it is a torture"])
        self.assertEqual('Course already added. Notes have been updated.', result)
        self.assertEqual(["math is cool", "just joking", "it is a torture"], self.student_with_courses.courses['math'])

    def test_enroll_method_add_course_and_notes(self):
        result = self.student.enroll("math", ["just joking", "it is a torture"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"math": ["just joking", "it is a torture"]}, self.student.courses)

    def test_enroll_method_add_course_and_notes_with_empty_add_course_notes_arg(self):
        result = self.student.enroll("math", ["just joking", "it is a torture"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"math": ["just joking", "it is a torture"]}, self.student.courses)

    def test_enroll_method_add_course_without_notes(self):
        result = self.student.enroll("math", ["just joking", "it is a torture"], '12')
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"math": []}, self.student.courses)

    def test_add_notes_method_course_not_found_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "math is boring")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({}, self.student.courses)

    def test_add_notes_method_update_notes_for_course(self):
        result = self.student_with_courses.add_notes("math", "some note")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["math is cool", "some note"], self.student_with_courses.courses['math'])

    def test_leave_course_method_course_not_found_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("math")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual({}, self.student.courses)

    def test_leave_course_method_update_courses_for_student(self):
        result = self.student_with_courses.leave_course("math")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student_with_courses.courses)


if __name__ == '__main__':
    main()
