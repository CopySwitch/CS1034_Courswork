import pytest

from Job import Job
from job_manager import JobManager


# -----------------------
# Job tests (Task 1)
# -----------------------

def test_job_constructor_and_getters():
    j = Job("Mahdieh Zaker", "Teaching and Learning Activities", 13.45, "21/10/2025", 2)
    assert j.get_name() == "Mahdieh Zaker"
    assert j.get_category() == "Teaching and Learning Activities"
    assert j.get_rate() == 13.45
    assert j.get_date() == "21/10/2025"
    assert j.get_hours() == 2


def test_job_str_and_repr_format():
    j = Job("A", "Cat", 10.0, "21/10/2025", 2)
    expected = 'Job("A", "Cat", 10.0, "21/10/2025", 2)'
    assert str(j) == expected
    assert repr(j) == expected


def test_job_equality_and_hash():
    j1 = Job("A", "Cat", 10.0, "21/10/2025", 2)
    j2 = Job("A", "Cat", 10.0, "21/10/2025", 2)
    j3 = Job("A", "Cat", 10.0, "21/10/2025", 3)

    assert j1 == j2
    assert j1 != j3
    assert hash(j1) == hash(j2)


def test_job_validation_positive_rate_and_hours():
    with pytest.raises(ValueError):
        Job("A", "Cat", 0, "21/10/2025", 2)
    with pytest.raises(ValueError):
        Job("A", "Cat", -1, "21/10/2025", 2)
    with pytest.raises(ValueError):
        Job("A", "Cat", 10.0, "21/10/2025", 0)
    with pytest.raises(ValueError):
        Job("A", "Cat", 10.0, "21/10/2025", -2)


def test_job_validation_hours_max_6_boundary():
    # boundary: 6 is allowed
    j = Job("A", "Cat", 10.0, "21/10/2025", 6)
    assert j.get_hours() == 6

    # 7 is not allowed
    with pytest.raises(ValueError):
        Job("A", "Cat", 10.0, "21/10/2025", 7)


def test_job_type_validation():
    with pytest.raises(TypeError):
        Job(123, "Cat", 10.0, "21/10/2025", 2)  # name must be str
    with pytest.raises(TypeError):
        Job("A", 999, 10.0, "21/10/2025", 2)    # category must be str
    with pytest.raises(TypeError):
        Job("A", "Cat", "ten", "21/10/2025", 2) # rate must be numeric
    with pytest.raises(TypeError):
        Job("A", "Cat", 10.0, 20251021, 2)      # date must be str
    with pytest.raises(TypeError):
        Job("A", "Cat", 10.0, "21/10/2025", 2.5)  # hours must be int


# -----------------------
# JobManager tests (Task 2)
# -----------------------

def test_job_manager_init_default_empty():
    jm = JobManager()
    assert jm.get_jobs() == []


def test_job_manager_add_job_normal():
    jm = JobManager()
    j1 = Job("A", "Cat", 10.0, "21/10/2025", 2)
    jm.add_job(j1)
    assert jm.get_jobs() == [j1]


def test_job_manager_add_job_enforces_8_hours_per_day_boundary():
    jm = JobManager()
    jm.add_job(Job("A", "Cat", 10.0, "21/10/2025", 6))
    jm.add_job(Job("A", "Cat", 10.0, "21/10/2025", 2))  # total 8 OK

    with pytest.raises(ValueError):
        jm.add_job(Job("A", "Cat", 10.0, "21/10/2025", 1))  # would make 9


def test_job_manager_remove_job_normal_and_missing():
    jm = JobManager()
    j = Job("A", "Cat", 10.0, "21/10/2025", 2)
    jm.add_job(j)
    jm.remove_job(j)
    assert jm.get_jobs() == []

    with pytest.raises(ValueError):
        jm.remove_job(j)  # already removed


def test_job_manager_edit_job_normal():
    jm = JobManager()
    old = Job("A", "Cat", 10.0, "21/10/2025", 6)
    jm.add_job(old)

    new = Job("A", "Cat", 10.0, "21/10/2025", 5)
    jm.edit_job(old, new)
    assert jm.get_jobs() == [new]


def test_job_manager_edit_job_enforces_8_hours_rule():
    jm = JobManager()
    j1 = Job("A", "Cat", 10.0, "21/10/2025", 6)
    j2 = Job("A", "Cat", 10.0, "21/10/2025", 2)
    jm.add_job(j1)
    jm.add_job(j2)

    # try to edit j2 into 6 hours -> would make 12 total, should fail
    with pytest.raises(ValueError):
        jm.edit_job(j2, Job("A", "Cat", 10.0, "21/10/2025", 6))


def test_job_manager_edit_job_missing_old_job():
    jm = JobManager()
    old = Job("A", "Cat", 10.0, "21/10/2025", 2)
    new = Job("A", "Cat", 10.0, "21/10/2025", 2)
    with pytest.raises(ValueError):
        jm.edit_job(old, new)


def test_search_by_category_exact_match():
    jm = JobManager()
    j1 = Job("A", "Cat1", 10.0, "21/10/2025", 2)
    j2 = Job("B", "Cat1", 12.0, "21/10/2025", 3)
    j3 = Job("A", "Cat2", 10.0, "22/10/2025", 1)
    jm.add_job(j1)
    jm.add_job(j2)
    jm.add_job(j3)

    assert jm.search_by_category("Cat1") == [j1, j2]
    assert jm.search_by_category("Cat2") == [j3]
    assert jm.search_by_category("Missing") == []


def test_search_by_rate_exact_match():
    jm = JobManager()
    j1 = Job("A", "Cat", 10.0, "21/10/2025", 2)
    j2 = Job("B", "Cat", 10.0, "22/10/2025", 1)
    j3 = Job("C", "Cat", 12.0, "22/10/2025", 1)
    jm.add_job(j1)
    jm.add_job(j2)
    jm.add_job(j3)

    assert jm.search_by_rate(10.0) == [j1, j2]
    assert jm.search_by_rate(12.0) == [j3]
    assert jm.search_by_rate(99.0) == []


def test_search_by_name_and_date_exact_match():
    jm = JobManager()
    j1 = Job("A", "Cat", 10.0, "21/10/2025", 2)
    j2 = Job("A", "Cat", 10.0, "22/10/2025", 2)
    j3 = Job("B", "Cat", 10.0, "21/10/2025", 2)
    jm.add_job(j1)
    jm.add_job(j2)
    jm.add_job(j3)

    assert jm.search_by_name_and_date("A", "21/10/2025") == [j1]
    assert jm.search_by_name_and_date("A", "22/10/2025") == [j2]
    assert jm.search_by_name_and_date("A", "01/01/2000") == []


def test_get_total_cost_per_name():
    jm = JobManager()
    jm.add_job(Job("A", "Cat", 10.0, "21/10/2025", 2))  # 20
    jm.add_job(Job("A", "Cat", 5.0, "22/10/2025", 1))   # 5
    jm.add_job(Job("B", "Cat", 7.0, "21/10/2025", 3))   # 21

    totals = jm.get_total_cost_per_name(["A", "B", "C"])
    assert totals["A"] == 25.0
    assert totals["B"] == 21.0
    assert totals["C"] == 0.0


def test_get_category_count_per_name_dict_of_dicts():
    jm = JobManager()
    jm.add_job(Job("A", "X", 10.0, "21/10/2025", 2))
    jm.add_job(Job("A", "X", 10.0, "22/10/2025", 2))
    jm.add_job(Job("A", "Y", 10.0, "22/10/2025", 1))
    jm.add_job(Job("B", "X", 10.0, "21/10/2025", 3))

    counts = jm.get_category_count_per_name()
    assert counts["A"]["X"] == 2
    assert counts["A"]["Y"] == 1
    assert counts["B"]["X"] == 1


# -----------------------
# CSV tests (Task 2 load/save)
# -----------------------

def test_save_and_load_csv_round_trip(tmp_path):
    jm = JobManager()
    jm.add_job(Job("A", "Cat", 10.0, "21/10/2025", 2))
    jm.add_job(Job("B", "Cat", 12.0, "21/10/2025", 3))

    file_path = tmp_path / "jobs.csv"
    jm.save_to_file(str(file_path))

    jm2 = JobManager()
    jm2.load_from_file(str(file_path))

    assert jm2.get_jobs() == jm.get_jobs()


def test_load_from_file_missing_file_raises():
    jm = JobManager()
    with pytest.raises(FileNotFoundError):
        jm.load_from_file("this_file_should_not_exist_12345.csv")


def test_load_from_file_bad_header_raises(tmp_path):
    bad_csv = tmp_path / "bad.csv"
    bad_csv.write_text("wrong,header\nx,y\n", encoding="utf-8")

    jm = JobManager()
    with pytest.raises(ValueError):
        jm.load_from_file(str(bad_csv))
