# Submitter: haodoz4(Zhang, Haodong)
# Partner  : yuxuez2(Zhou, Yuxue)
# We certify that we worked cooperatively on this programming
#   assignments, according to the rules for pair programming

from goody import type_as_str
from math import sqrt

class Interval:
    
    def __init__(self, min_num, max_num):
        self.max = max_num
        self.min = min_num
    
    @staticmethod    
    def min_max(min_num, max_num=None):
        assert type(min_num) == int or type(min_num) == float, "The first argument is not an int or float numeric type"
        assert type(max_num) == int or type(max_num) == float or max_num == None, "The second argument is not a numeric type or None"
        if max_num == None:
            return Interval(min_num, min_num)
        else:
            assert min_num <= max_num, "The first argument is greater than the second"
            return Interval(min_num, max_num)
    
    @staticmethod 
    def mid_err(middle, error=0):
        assert type(middle) == int or type(middle) == float, "The first argument is not an int or float numeric type"
        assert type(error) == int or type(error) == float, "The second argument is not a numeric type"
        assert error >= 0, "The second argument is negative"
        return Interval(middle - error, middle + error)
    
    def best(self):
        return (self.max + self.min) / 2
    
    def error(self):
        return self.max - (self.max + self.min) / 2
    
    def relative_error(self):
        return abs(self.error() / self.best()) * 100
    
    def __repr__(self):
        return "Interval({},{})".format(self.min, self.max)
    
    def __str__(self):
        return "{}(+/-{})".format((self.max + self.min) / 2, (self.max - ((self.max + self.min) / 2)))
    
    def __bool__(self):
        if self.error() != 0:
            return True
        else:
            return False
        
    def __pos__(self):
        return self
    
    def __neg__(self):
        return Interval.min_max(-self.max, -self.min)
    
    def __add__(self, right):
        if type(right) == Interval:
            new_min = self.min + right.min
            new_max = self.max + right.max
            return Interval.min_max(new_min, new_max)
        elif type(right) == int or type(right) == float:
            new_min = self.min + right
            new_max = self.max + right
            return Interval.min_max(new_min, new_max)
        else:
            return NotImplemented
        
    def __radd__(self, left):
        if type(left) == Interval:
            new_min = self.min + left.min
            new_max = self.max + left.max
            return Interval.min_max(new_min, new_max)
        elif type(left) == int or type(left) == float:
            new_min = self.min + left
            new_max = self.max + left
            return Interval.min_max(new_min, new_max)
        else:
            return NotImplemented
        
    def __sub__(self, right):
        if type(right) == Interval:
            new_min = self.min - right.max
            new_max = self.max - right.min
            return Interval.min_max(new_min, new_max)
        elif type(right) == int or type(right) == float:
            new_min = self.min - right
            new_max = self.max - right
            return Interval.min_max(new_min, new_max)
        else:
            return NotImplemented
        
    def __rsub__(self, left):
        if type(left) == Interval:
            new_min = left.min - self.max
            new_max = left.max - self.min
            return Interval.min_max(new_min, new_max)
        elif type(left) == int or type(left) == float:
            new_min = left - self.max
            new_max = left - self.min
            return Interval.min_max(new_min, new_max)
        else:
            return NotImplemented
        
    def __mul__(self, right):
        if type(right) == Interval:
            lis1 = [self.min, self.max]
            lis2 = [right.min, right.max]
            lis_new = []
            for i in lis1:
                for j in lis2:
                    lis_new.append(i * j)
            new_min = min(lis_new)
            new_max = max(lis_new)
            return Interval.min_max(new_min, new_max)
        elif type(right) == int or type(right) == float:
            a = self.min * right
            b = self.max * right
            if a > b:
                return Interval.min_max(b, a)
            else:
                return Interval.min_max(a, b)
        else:
            return NotImplemented

        
    def __rmul__(self, left):
        if type(left) == Interval:
            lis1 = [self.min, self.max]
            lis2 = [left.min, left.max]
            lis_new = []
            for i in lis1:
                for j in lis2:
                    lis_new.append(i * j)
            new_min = min(lis_new)
            new_max = max(lis_new)
            return Interval.min_max(new_min, new_max)
        elif type(left) == int or type(left) == float:
            a = self.min * left
            b = self.max * left
            if a > b:
                return Interval.min_max(b, a)
            else:
                return Interval.min_max(a, b)
        else:
            return NotImplemented
        
    def __truediv__(self, right): 
        if type(right) == Interval:
            if right.min< 0 and right.max > 0:
                raise ZeroDivisionError
            else:
                lis1 = [self.min, self.max]
                lis2 = [right.min, right.max]
                lis_new = []
                for i in lis1:
                    for j in lis2:
                        lis_new.append(i / j)
                new_min = min(lis_new)
                new_max = max(lis_new)
                return Interval.min_max(new_min, new_max)
        elif type(right) == int or type(right) == float:
            a = self.min / right
            b = self.max / right
            if a > b:
                return Interval.min_max(b, a)
            else:
                return Interval.min_max(a, b)
        else:
            return NotImplemented

    def __rtruediv__(self, left):
        if type(left) == Interval:
            if left.min< 0 and left.max > 0:
                raise ZeroDivisionError
            else:
                lis1 = [self.min, self.max]
                lis2 = [left.min, left.max]
                lis_new = []
                for i in lis2:
                    for j in lis1:
                        lis_new.append(i / j)
                new_min = min(lis_new)
                new_max = max(lis_new)
                return Interval.min_max(new_min, new_max)
        elif type(left) == int or type(left) == float:
            if self.min < 0 and self.max > 0:
                raise ZeroDivisionError
            else:
                a = left / self.min
                b = left / self.max
                if a > b:
                    return Interval.min_max(b, a)
                else:
                    return Interval.min_max(a, b)
        else:
            return NotImplemented
        
    def __pow__(self, right):
        if type(right) == int:
            if right >= 0:
                new_min = self.min**right
                new_max = self.max**right
                return Interval.min_max(new_min, new_max)
            else:
                new_min = (1 / self.max)**(-right)
                new_max = (1 / self.min)**(-right)
                return Interval.min_max(new_min, new_max)
        else:
            return NotImplemented
    
    def __eq__(self, right):
        if type(right) == Interval:
            if self.min == right.min and self.max == right.max:
                return True
            else:
                return False
        elif type(right) == int or type(right) == float:
            if right == self.min and right == self.max:
                return True
            else:
                return False
        else:
            return NotImplemented
        
    def __ne__(self, right):
        if type(right) == Interval:
            if self.min != right.min or self.max != right.max:
                return True
            else:
                return False
        elif type(right) == int or type(right) == float:
            if right != self.min or right != self.max:
                return True
            else:
                return False
        else:
            return NotImplemented
        
    
    def __lt__(self, right):
        try:
            assert Interval.compare_mode == 'liberal' or Interval.compare_mode == 'conservative', "Compare_mode should exist, and should bind to liberal or conservative"
            if Interval.compare_mode == 'liberal':
                if type(right) == int or type(right) == float:
                    right = Interval.min_max(right, right)
                if self.best() < right.best():
                    return True
                else:
                    return False
            else:
                if type(right) == int or type(right) == float:
                    right = Interval.min_max(right, right)
                if self.max < right.min:
                    return True
                else:
                    return False
        except AttributeError:
            raise AssertionError

    def __gt__(self, right):
        try:
            assert Interval.compare_mode == 'liberal' or Interval.compare_mode == 'conservative', "Compare_mode should exist, and should bind to liberal or conservative"
            if Interval.compare_mode == 'liberal':
                if type(right) == int or type(right) == float:
                    right = Interval.min_max(right, right)
                if self.best() > right.best():
                    return True
                else:
                    return False
            else:
                if type(right) == int or type(right) == float:
                    right = Interval.min_max(right, right)
                if self.min > right.max:
                    return True
                else:
                    return False
        except AttributeError:
            raise AssertionError
            
    def __le__(self, right):
        try:
            assert Interval.compare_mode == 'liberal' or Interval.compare_mode == 'conservative', "Compare_mode should exist, and should bind to liberal or conservative"
            if Interval.compare_mode == 'liberal':
                if type(right) == int or type(right) == float:
                    right = Interval.min_max(right, right)
                if self.best() <= right.best():
                    return True
                else:
                    return False
            else:
                if type(right) == int or type(right) == float:
                    right = Interval.min_max(right, right)
                if self.max <= right.min:
                    return True
                else:
                    return False
        except AttributeError:
            raise AssertionError
        
    def __ge__(self, right):
        try:
            assert Interval.compare_mode == 'liberal' or Interval.compare_mode == 'conservative', "Compare_mode should exist, and should bind to liberal or conservative"
            if Interval.compare_mode == 'liberal':
                if type(right) == int or type(right) == float:
                    right = Interval.min_max(right, right)
                if self.best() >= right.best():
                    return True
                else:
                    return False
            else:
                if type(right) == int or type(right) == float:
                    right = Interval.min_max(right, right)
                if self.min >= right.max:
                    return True
                else:
                    return False
        except AttributeError:
            raise AssertionError
        
    def __abs__(self):
        if self.min < 0 and self.max > 0:
            new_min = 0.0
            new_max = abs(self.max)
            return Interval.min_max(new_min, new_max)
        else:
            a = abs(self.min)
            b = abs(self.max)
            if a > b:
                return Interval.min_max(b, a)
            else:
                return Interval.min_max(a, b)
            
    def sqrt(self):
        if self.min < 0 or self.max < 0:
            raise ValueError
        else:
            new_min = sqrt(self.min)
            new_max = sqrt(self.max)
            return Interval.min_max(new_min, new_max)
    
    def __setattr__(self, name, value):
        if name not in self.__dict__ and (name == 'max' or name == 'min'):
            self.__dict__[name] = value
        else:
            assert None, "The object is immutable"
        
if __name__ == '__main__':

    g = Interval.mid_err(9.8,.05)
    print(repr(g))
    g = Interval.min_max(9.75,9.85)
    print(repr(g))
    d = Interval.mid_err(100,1)
    t = (d/(2*g)).sqrt()
    print(t,repr(t),t.relative_error())    

    import driver    
    driver.default_file_name = 'bscp22F21.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
