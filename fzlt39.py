# This is an interview question asked by Snapchat.
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


def max_overlapping(intervals):
    starts = sorted(start for start, end in intervals)
    ends = sorted(end for start, end in intervals)
    current_max = 0
    current_overlap = 0
    i, j = 0, 0
    while i < len(intervals) and j < len(intervals):
        if starts[i] < ends[j]:
            current_overlap += 1
            current_max = max(current_max, current_overlap)
            i += 1
        else:
            current_overlap -= 1
            j += 1
    return current_max


def max_overlapping2(lst):
    maxrooms = 1
    for i in range(len(lst)-1):
        overlap_left, overlap_right = 1, 1
        for j in range(i+1, len(lst)):
            if (lst[i][0] in range(lst[j][0], lst[j][1])):
                overlap_left += 1
            if (lst[i][1] in range(lst[j][0], lst[j][1])):
                overlap_right += 1
        if max(overlap_left, overlap_right) > maxrooms:
            maxrooms = max(overlap_left, overlap_right)
    return maxrooms
