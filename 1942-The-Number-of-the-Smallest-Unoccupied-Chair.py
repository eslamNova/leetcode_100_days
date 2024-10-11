import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Step 1: Create a sorted list of times, but we need to remember the original friend index
        # times_with_indices will store tuples of (arrival_time, leaving_time, friend_index)
        times_with_indices = [(times[i][0], times[i][1], i) for i in range(len(times))]
        # Sort friends by their arrival times
        times_with_indices.sort(key=lambda x: x[0])
        
        # Step 2: Min-heap to store available (free) chairs
        free_chairs = []
        
        # Step 3: Min-heap to store currently occupied chairs (release them based on leaving time)
        # Each entry in occupied_chairs heap will be (leaving_time, chair_number)
        occupied_chairs = []
        
        # Step 4: Keep track of the next new chair number (if all existing chairs are occupied)
        chair_counter = 0
        
        # Step 5: Process each friend in the sorted order of their arrival
        for arrival, leaving, friend in times_with_indices:
            # Release all the chairs of friends who have already left before the current friend's arrival
            # We use the occupied_chairs heap to know who is leaving and when
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                # Pop the earliest leaving friend and free their chair
                _, freed_chair = heapq.heappop(occupied_chairs)
                heapq.heappush(free_chairs, freed_chair)  # Add their chair back to the free_chairs heap
            
            # Assign the smallest available chair to the current friend
            if free_chairs:
                # If there's a free chair, we pop the smallest one
                assigned_chair = heapq.heappop(free_chairs)
            else:
                # If no free chair, we use the next new chair
                assigned_chair = chair_counter
                chair_counter += 1
            
            # Add this friend's leaving time and chair to the occupied_chairs heap
            heapq.heappush(occupied_chairs, (leaving, assigned_chair))
            
            # Check if the current friend is the targetFriend
            if friend == targetFriend:
                return assigned_chair  # Return the chair assigned to the target friend

