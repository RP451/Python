arrivals = ['corum', 'elric', 'jerry', 'baron', 'helsing', 'sauron', 'pippin', 'frodo']
name = 'sauron'

def fashionably_late(arrivals, name):
  
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1

