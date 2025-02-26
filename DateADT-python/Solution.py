class DateADT:
    def __init__(self, *args) -> None:
        if len(args) == 3:
            self.year = int(args[0])
            self.month = int(args[1])
            self.day = int(args[2])
            self.hrs = 0
            self.min = 0
            self.sec = 0
            self.validate_month()
            self.validate_day()
            self.validate_time()

        elif len(args) == 6:
            self.year = int(args[0])
            self.month = int(args[1])
            self.day = int(args[2])
            self.hrs = int(args[3])
            self.min = int(args[4])
            self.sec = int(args[5])
            self.validate_month()
            self.validate_day()
            self.validate_time()
        

        elif isinstance(args[0], str):
            date_string = args[0]
            x = date_string.split()

            date_part = x[0]
            time_part = x[1]

            y = date_part.split('-')
            year = int(y[0])
            month = int(y[1])
            day = int(y[2])

            z = time_part.split(':')
            hours = int(z[0])
            minutes = int(z[1])
            seconds = int(z[2])

            self.year = year
            self.month = month
            self.day = day
            self.hrs = hours
            self.min = minutes
            self.sec = seconds

            self.validate_month()
            self.validate_day()
            self.validate_time()


    def validate_month(self):
        if self.month < 0 or self.month > 11:
            raise ValueError()


    def validate_day(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
        if self.is_leap_year():
            days_in_month[1] = 29
        
        if self.day < 1 or self.day > days_in_month[self.month]:
            raise ValueError()
        

    def validate_time(self):
        if self.hrs < 0 or self.hrs > 23:
            raise ValueError()
        
        if self.min < 0 or self.min > 59:
            raise ValueError()
        
        if self.sec < 0 or self.sec > 60:
            raise ValueError()
        
    def is_leap_year(self):
        if self.year%100==0:
            if self.year%400==0:
                return True
            else:
                return False
        elif self.year%4==0:
            return True
        else:
            return False
        

    def getYear(self):
        return self.year
    
    def getMonth(self):
        return self.month
    
    def getDay(self):
        return self.day
    
    def getMinutes(self):
        return self.min
    
    def getSeconds(self):
        return self.sec
    
    def getHours(self):
        return self.hrs


    def getTime(self):
        millisec_per_day = 86400000
        millisec = (self.year - 1970) * 365 * millisec_per_day
        
        millisec += self.month * 30 * millisec_per_day
        millisec += (self.day - 1) * millisec_per_day
        
        millisec += self.hrs * 3600000
        millisec += self.min * 60000
        millisec += self.sec * 1000
        return millisec
    
    def setTime(self, ms):
        millisec_per_day = 86400000

        total_days = ms // millisec_per_day
        remaining_millisic = ms % millisec_per_day

        self.year = 1970 + total_days // 365
        total_days %= 365

        self.month = total_days // 30
        total_days %= 30

        self.day = total_days + 1
        
        remaining_seconds = remaining_millisic // 1000
        self.hrs = remaining_seconds // 3600

        remaining_seconds %= 3600
        self.min = remaining_seconds // 60
        self.sec = remaining_seconds % 60


    def before(self,other):
        if self.getYear() < other.getYear():
            return True
        elif self.getYear() == other.getYear():
            if self.getMonth() < other.getMonth():
                return True
            elif self.getDay() < other.getDay():
                return True
        return False
    

    def after(self,other):
        return not self.before(other)

    def setYear(self, year):
        self.year = year

    def setMonth(self, m):
        self.month = m

    def setDay(self,d):
        self.day = d

    def setHours(self,hrs):
        self.hrs = hrs
    
    def setMinutes(self,min):
        self.min = min
    
    def setSeconds(self,sec):
        self.sec = sec
    

    def toString(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d} {self.hrs:02d}:{self.min:02d}:{self.sec:02d}"

        