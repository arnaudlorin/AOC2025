class Intervals:
    def __init__(self):
        self.intervals = []
        
    def add(self, mini_new, maxi_new):
        self.intervals.append([mini_new, maxi_new])
        
    def simplify(self):
        intervals_union_disjonct = []
        while True:
            if self.intervals == []:
                break
            minimal = self.intervals[0][0]
            minimal_index = 0
            for i, (mini, maxi) in enumerate(self.intervals):
                if mini < minimal:   
                    minimal = mini
                    minimal_index = i
            mini, maxi = self.intervals.pop(minimal_index)
            if intervals_union_disjonct == [] or mini > intervals_union_disjonct[-1][1]:
                intervals_union_disjonct.append([mini, maxi])
            elif maxi > intervals_union_disjonct[-1][1]:
                intervals_union_disjonct[-1][1] = maxi
                
        self.intervals = intervals_union_disjonct
            
    def lenght_intervals(self):
        count = 0
        for mini, maxi in self.intervals:
            count += maxi - mini + 1
        return count
    
    def is_inside(self, n):
        for (mini, maxi) in self.intervals:
            if n >= mini and n <= maxi:
                return True
        return False
        
    
count = 0
intervals = Intervals()
with open("input.txt") as f:
    for l in f:
        if l == '\n':
            break
        l = l.split('-')
        mini = l[0]
        maxi = l[1]
        intervals.add(int(mini), int(maxi))
    intervals.simplify()
    print(intervals.lenght_intervals())
    for l in f:
        count += intervals.is_inside(int(l))
        
print(count)