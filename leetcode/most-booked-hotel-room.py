import collections

def most_booked_room(bookings: list[str]) -> str:
    max_bookings = 0
    most_booked = ''
    booking_freqs = {}

    for booking in bookings:
        if booking[0] == '+':
            floor_idx, floor_char = booking[1], booking[2]
            if floor_idx in booking_freqs:
                floor = booking_freqs[floor_idx]
                if floor_char in floor:
                    floor[floor_char] += 1
                    if floor[floor_char] > max_bookings:
                        most_booked = floor_idx + floor_char 
                        max_bookings = floor[floor_char]
                else:
                    floor[floor_char] = 1
            else:
                booking_freqs[floor_idx] = { floor_char: 1 }

    return most_booked

if __name__ == '__main__':
    input = [(["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"], "1A")]
    for case, expected in input:
        if most_booked_room(case) == expected:
            print("PASS")
        else:
            print("FAIL")
            print("OUTPUT: ", most_booked_room(case))
            print("EXPECTED: ", expected)

