"""
Excercise 11.7

Question 1: You are organizing a series of meetings and need to find which time slots
are free for two participants in the meeting. Given three sets: one with
all possible time slots and other two with time slots already booked by
the two individual participants, write a Python function to determine the
time slots that are still available. Also, determine the time slots during
which only one of the participants is available.

Example Input:
all_time_slots = {"9:00-10:00", "10:00-11:00", "11:00-12:00",
"12:00-1:00", "1:00-2:00", "2:00-3:00"}
booked_slots_1 = {"10:00-11:00", "1:00-2:00"}
booked_slots_2 = {"12:00-1:00", "2:00-3:00"}

Expected Output:
Available Slots: {'9:00-10:00', '11:00-12:00'}
Slots Where Only One Participant is Available: {'2:00-3:00',
'10:00-11:00','12:00-1:00', '1:00-2:00',}
"""

def find_slots(all: set, booked_1: set, booked_2: set):
    avail = all.difference(booked_1.union(booked_2))
    single_slots = booked_1.union(booked_2).difference(booked_1.intersection(booked_2))
    print(f"Available slots: {avail}\nSlots Where Only One Participant is Available: {single_slots}")
