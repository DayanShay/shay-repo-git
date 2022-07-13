class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        """
        Function __init__ initiates parameters
        :param day: int
        :param month: int
        :param year: int
        """
        self.day = day
        self.month = month
        self.year = year
        Date.isvalid(self)

    def __str__(self) -> str:
        """
        function __str__ gets a parameter self: Date
        return a format string as "day.month.year"
        :param self: Date
        :return: str
        """
        if self.month >= 10 and self.day >= 10:
            return f"{self.day}.{self.month}.{self.year}"
        else:
            if not self.month >= 10 and self.day >= 10:
                return f"{self.day}." + "0%a" % self.month + f".{self.year}"
            else:
                if not self.month >= 10 and not self.day >= 10:
                    return "0%a" % self.day+"." + "0%a" % self.month + f".{self.year}"
                else:
                    return "0%a" % self.day + f".{self.month}.{self.year}"

    def __eq__(self, other_eq) -> bool:
        """ Function __eq__ gets self : Date, other_eq : Date .
        Function Returns if self == other_eq.
        :param self: Date
        :param other_eq: Date
        :return: bool"""
        equal_flag = (self.year == other_eq.year) and (self.month == other_eq.month) and (self.day == other_eq.day)
        return equal_flag

    def __ne__(self, other_ne) -> bool:
        """ Function __ne__ gets self : Date, other_ne : Date .
        Function Returns if self != other_eq.
        :param self: Date
        :param other_ne: Date
        :return: bool"""
        equal_flag = (self.year != other_ne.year) or (self.month != other_ne.month) or (self.day != other_ne.day)
        return equal_flag

    def __sub__(self, other_date) -> int:
        """
        Function __sub__ gets self : Date, other_date : Date .
        Function returns how many days separates between self and other_date.
        example .__sub__(Date1(1,1,1999),Date2(5,1,1999)) -> 4
        :return: int
        """
        if self.year > other_date.year or self.month > other_date.month and self.day < other_date.day:
            temp_date_sub = other_date
            self_sub = self
        else:
            temp_date_sub = self
            self_sub = other_date
        counter = 0
        flag_sub = True
        while flag_sub:
            if temp_date_sub.year == self_sub.year:
                if temp_date_sub.month == self_sub.month:
                    if temp_date_sub.day == self_sub.day:
                        flag_sub = False
            temp_date_sub = Date.getNextDay(temp_date_sub)
            counter += 1
        return counter

    def __lt__(self, other_lt) -> bool:
        """ Function __lt__ gets self : Date, other_gt : Date .
        Function Returns if self < other_le.
        :param self: Date
        :param other_lt: Date
        :return: bool
        """
        if self.year < other_lt.year or self.month < other_lt.month \
                or self.day < other_lt.day:
            return True
        else:
            return False

    def __le__(self, other_le) -> bool:
        """ Function __le__ gets self : Date, other_le : Date .
        Function Returns if self <= other_le.
        :param self: Date
        :param other_le: Date
        :return: bool
        """
        little_flag = self.year > other_le.year or self.month > other_le.month and self.day > other_le.day
        equal_flag = (self.year == other_le.year) and (self.month == other_le.month) and (self.day == other_le.day)
        if equal_flag or not little_flag:
            return True
        else:
            return False

    def __ge__(self, other_ge) -> bool:
        """
        Function __ge__ except 2 parameters
        self : Date, other_ge : Date.
        Returns if self >= other_ge.
        :param self: Date
        :param other_ge: Date
        :return: Bool
        """
        great_flag = self.year > other_ge.year or self.month > other_ge.month and self.day > other_ge.day
        equal_flag = (self.year == other_ge.year) and (self.month == other_ge.month) and (self.day == other_ge.day)
        if equal_flag or great_flag:
            return True
        else:
            return False

    def __gt__(self, other_gt) -> bool:
        """ Function __gt__ gets self : Date, other_gt : Date .
        Function Returns if self > other_le.
        :param self: Date
        :param other_gt: Date
        :return: bool
        """
        if self.year > other_gt.year or self.month > other_gt.month \
                and self.day > other_gt.day:
            return True
        else:
            return False

    def isvalid(self) -> TypeError:
        """Function isvalid except parameter self : Date
        and check if isValid , if invalid raise TypeError
        requirements:
            1) Leap year, february has 29 days else hase 28 days.
            2) months 4,6,9,11 has 30 days during the month
            3) months 1,3,7,8,10,12 has 31 Days during the month
        :param self: Date
        :return: TypeError
        """
        if not isinstance(self.day, int) or not (1 <= self.day <= 31):
            raise TypeError("Day must be between 1 - 31 ")
        if not isinstance(self.month, int) or not (1 <= self.month <= 12):
            raise TypeError("Month must be between 1 - 12 ")
        if not isinstance(self.year, int) or not 1000 <= self.year <= 9999:
            raise TypeError("Year must be between 1000 - 9999 ")
        if self.month == 2:
            if self.year % 4 == 0 or self.year % 4 == 0 \
                    and self.year % 100 == 0 \
                    and self.year % 400 != 0:
                if self.day > 29:
                    raise TypeError(f"Invalid Date - Day {self.day} Can't be at Month {self.month} on Year {self.year}.")
            else:
                if self.day > 28:
                    raise TypeError(f"Invalid Date - Day {self.day} Can't be at Month {self.month} on Year {self.year}.")
        if self.month == 4 or self.month == 6 \
                or self.month == 9 or self.month == 11:
            if self.day > 30:
                raise TypeError(f"Invalid Date - Day {self.day} Can't be at Month {self.month} on Year {self.year}.")
        if self.month == 1 or self.month == 3 or \
                self.month == 5 or self.month == 7 \
                or self.month == 8 or self.month == 10 \
                or self.month == 12:
            if self.day > 31:
                raise TypeError(f"Invalid Date - Day {self.day} Can't be at Month {self.month} on Year {self.year}.")

    def getNextDay(self) -> "Date":
        """Function getNextDay gets a parameter self: date
        and returns the next day.
        example getNextDays(Date(1,1,1999)) ->  Date(2,1,1999)
        :param self: Date
        :return: Date
        """
        try:
            return Date(self.day + 1, self.month, self.year)
        except :
            try:
                return Date(1, self.month + 1, self.year)
            except :
                try:
                    return Date(1, 1, self.year + 1)
                except :
                    return TypeError(f"Date out of Range")

    def getNextDays(self, daysToAdd: int) -> "Date":
        """Function getNextDays gets parameters self: date daysToAdd: int,
        and returns the future Date after x amount of days.
        example getNextDays(Date(1,1,1999) ,daysToAdd = 2) ->  Date(3,1,1999)
        :param self: Date
        :param daysToAdd: int
        :return: Date
        """
        temp_date = self
        for i in range(daysToAdd):
            try:
                temp_date = Date.getNextDay(temp_date)
            except TypeError:
                return TypeError(f"Date out of Range")
        return temp_date