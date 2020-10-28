# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs,
# and a starting airport, compute the person's itinerary. If no such itinerary exists, return null.
# If there are multiple possible itineraries, return the lexicographically smallest one.
# All flights must be used in the itinerary.
# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
# and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.
# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
# and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C']
# even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
# However, the first one is lexicographically smaller.


def itinerary(flights, myItinerary):
    if isinstance(myItinerary, str):
        myItinerary = list(myItinerary)

    if not flights:
        return myItinerary
    last_destination = myItinerary[-1]
    for i, (first, destination) in enumerate(flights):
        flights_updated = flights[:i] + flights[i + 1:]
        myItinerary.append(destination)
        if first == last_destination:
            return itinerary(flights_updated, myItinerary)
        myItinerary.pop()
    return None


x = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]

print(itinerary(x, "A"))


def compute_itenary(lst, start):
    r = [[i] for i in lst if i[0] == start]
    for _ in range(len(lst)-1):
        r = [i + [j]
             for i in r for j in lst if (lst.count(j) != i.count(j)) and (i[-1][1] == j[0])]
    r = sorted(r)[0]
    return [i[0] for i in r] + [r[-1][1]] if r else None
