# INCOMPLETE (wtf)
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_a = times[targetFriend][0]
        times.sort()
        chairs = [False] * len(times) # True = full, False = empty

        departure_times = {} # key = time, val = list of indices to clear at this time

        last_departure = times[0][1]
        next_arrival = times[0][0]
        departure_times[last_departure] = [0]
        next_chairs = [1]
        chairs[0] = True

        time = next_arrival
        while time <= last_departure:
            # clear chairs that depart at this time
            departures = departure_times.get(time)
            if departures is not None:
                for chair in departures:
                    next_chairs.append(chair)
                    chairs[chair] = False


            # seat someone if they arrive at this time
            arrival = times(time)
            if time == next_arrival:
                chair = next_chairs.pop(0)
                chairs[chair] = True

                if arrival[0] == target_a:
                    return chair

                if chairs[chair+1] == False:
                    next_chairs.insert(chair+1)

                departure = departure_times.get(arrival[1])
                if departure is None:
                    depature_times[arrival[1]] = [chair]
                else:
                    departure_times[arrival[1]].append(chair)

                last_departure = max(last_departure, arrival[1])
                next_arrival =

            i += 1

        return target_chair
