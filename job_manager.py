from Job import Job


class JobManager:
    def __init__(self, jobs=None):
        if jobs is None:
            self._jobs = []
        else:
            if not isinstance(jobs, list):
                raise TypeError("jobs must be a list of Job objects or None")
            for j in jobs:
                if not isinstance(j, Job):
                    raise TypeError("All items in jobs must be Job objects")
            self._jobs = jobs

    def get_jobs(self):
        return self._jobs

    def __str__(self):
        return f"JobManager({len(self._jobs)} jobs)"

    def __repr__(self):
        return f"JobManager(jobs={self._jobs!r})"

    def add_job(self, job):
        raise NotImplementedError

    def remove_job(self, job):
        raise NotImplementedError

    def edit_job(self, old_job, new_job):
        raise NotImplementedError

    def search_by_category(self, category):
        raise NotImplementedError

    def search_by_rate(self, rate):
        raise NotImplementedError

    def search_by_name_and_date(self, name, date):
        raise NotImplementedError

    def get_total_cost_per_name(self, names):
        raise NotImplementedError

    def get_category_count_per_name(self):
        raise NotImplementedError

    def load_from_file(self, file_name):
        raise NotImplementedError

    def save_to_file(self, file_name):
        raise NotImplementedError
