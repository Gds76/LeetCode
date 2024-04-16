class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        
        flights = [0] * (n + 1)
        for i in range(len(bookings)):
            flights[bookings[i][0]] += bookings[i][2]
            if bookings[i][1] + 1 < len(flights):
                flights[bookings[i][1] + 1] -= bookings[i][2]
        for i in range(1, len(flights)):
            flights[i] += flights[i - 1]
        return flights[1:]


        