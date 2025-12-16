class Job:
    def __init__(self, name, category, rate, date, hours):
        # Privacy via "private" instance variables (underscore convention)
        self._name = self._validate_non_empty_string(name, "name")
        self._category = self._validate_non_empty_string(category, "category")
        self._date = self._validate_non_empty_string(date, "date")

        self._rate = self._validate_positive_float(rate, "rate")
        self._hours = self._validate_positive_int(hours, "hours")

        # Rule: no more than 6 hours per job
        if self._hours > 6:
            raise ValueError("hours cannot exceed 6 for a single job")

    def get_name(self):
        return self._name

    def get_category(self):
        return self._category

    def get_rate(self):
        return self._rate

    def get_date(self):
        return self._date

    def get_hours(self):
        return self._hours

    def __eq__(self, other):
        if not isinstance(other, Job):
            return False
        return (
            self._name == other._name
            and self._category == other._category
            and self._rate == other._rate
            and self._date == other._date
            and self._hours == other._hours
        )

    def __hash__(self):
        return hash((self._name, self._category, self._rate, self._date, self._hours))

    def __str__(self):
        # Required example format:
        # Job("Mahdieh Zaker", "Teaching and Learning Activities", 13.45, "21/10/2025", 2)
        return f'Job("{self._name}", "{self._category}", {self._rate}, "{self._date}", {self._hours})'

    def __repr__(self):
        return self.__str__()

    # -----------------------
    # Extra helper methods (allowed)
    # -----------------------
    @staticmethod
    def _validate_non_empty_string(value, field_name):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        cleaned = value.strip()
        if cleaned == "":
            raise ValueError(f"{field_name} cannot be empty")
        return cleaned

    @staticmethod
    def _validate_positive_float(value, field_name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{field_name} must be a number")
        f = float(value)
        if f <= 0:
            raise ValueError(f"{field_name} must be positive")
        return f

    @staticmethod
    def _validate_positive_int(value, field_name):
        if not isinstance(value, int):
            raise TypeError(f"{field_name} must be an int")
        if value <= 0:
            raise ValueError(f"{field_name} must be positive")
        return value
a