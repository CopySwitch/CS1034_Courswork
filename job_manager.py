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
            self._jobs = []
            for j in jobs:
                self.add_job(j)

    def get_jobs(self):
        return self._jobs

    def __str__(self):
        return f"JobManager({len(self._jobs)} jobs)"

    def __repr__(self):
        return f"JobManager(jobs={self._jobs!r})"

    def add_job(self, job):
        if not isinstance(job, Job):
            raise TypeError("job must be a Job object")

        if not self._is_worker_available(job.get_name(), job.get_date(), job.get_hours()):
            raise ValueError("Worker is not available (would exceed 8 hours on that date)")

        self._jobs.append(job)

    def remove_job(self, job):
        if not isinstance(job, Job):
            raise TypeError("job must be a Job object")
        try:
            self._jobs.remove(job)
        except ValueError as e:
            raise ValueError("Job not found; cannot remove") from e

    def edit_job(self, old_job, new_job):
        if not isinstance(old_job, Job) or not isinstance(new_job, Job):
            raise TypeError("old_job and new_job must be Job objects")

        try:
            index = self._jobs.index(old_job)
        except ValueError as e:
            raise ValueError("Old job not found; cannot edit") from e

        hours_without_old = self._total_hours_for_name_date(
            new_job.get_name(),
            new_job.get_date(),
            exclude_job=old_job
        )

        if hours_without_old + new_job.get_hours() > 8:
            raise ValueError("Worker is not available (would exceed 8 hours on that date)")

        self._jobs[index] = new_job

    def search_by_category(self, category):
        if not isinstance(category, str):
            raise TypeError("category must be a string")
        return [j for j in self._jobs if j.get_category() == category]

    def search_by_rate(self, rate):
        if not isinstance(rate, (int, float)):
            raise TypeError("rate must be a number")
        r = float(rate)
        return [j for j in self._jobs if j.get_rate() == r]

    def search_by_name_and_date(self, name, date):
        if not isinstance(name, str) or not isinstance(date, str):
            raise TypeError("name and date must be strings")
        return [j for j in self._jobs if j.get_name() == name and j.get_date() == date]

    def get_total_cost_per_name(self, names):
        if not isinstance(names, list):
            raise TypeError("names must be a list of strings")
        for n in names:
            if not isinstance(n, str):
                raise TypeError("names must contain only strings")

        totals = {}
        for n in names:
            total_cost = 0.0
            for j in self._jobs:
                if j.get_name() == n:
                    total_cost += j.get_rate() * j.get_hours()
            totals[n] = float(total_cost)
        return totals

    def get_category_count_per_name(self):
        raise NotImplementedError

    def load_from_file(self, file_name):
        raise NotImplementedError

    def save_to_file(self, file_name):
        raise NotImplementedError

    # ---- helper methods ----
    def _total_hours_for_name_date(self, name, date, exclude_job=None):
        total = 0
        for j in self._jobs:
            if exclude_job is not None and j == exclude_job:
                continue
            if j.get_name() == name and j.get_date() == date:
                total += j.get_hours()
        return total

    def _is_worker_available(self, name, date, hours_to_add):
        return self._total_hours_for_name_date(name, date) + hours_to_add <= 8
