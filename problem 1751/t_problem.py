from typing import List
import bisect

# Alternative solution using memoization (often more intuitive)
class SolutionMemo:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        Alternative solution using memoization (top-down DP)
        """
        events.sort(key=lambda x: x[1])  # Sort by end time
        n = len(events)
        import ipdb;ipdb.set_trace(context=15)
        # Memoization cache
        memo = {}
        
        def find_next_event(current_end, start_idx):
            """Find the next event that starts after current_end"""
            for i in range(start_idx, n):
                if events[i][0] > current_end:
                    return i
            return n
        
        def dp(idx, remaining_events):
            """
            Return max value starting from event idx with remaining_events left
            """
            if idx >= n or remaining_events == 0:
                return 0
            
            if (idx, remaining_events) in memo:
                return memo[(idx, remaining_events)]
            
            # Option 1: Skip current event
            result = dp(idx + 1, remaining_events)
            
            # Option 2: Take current event
            next_idx = find_next_event(events[idx][1], idx + 1)
            result = max(result, events[idx][2] + dp(next_idx, remaining_events - 1))
            
            memo[(idx, remaining_events)] = result
            return result
        
        return dp(0, k)

# Test cases
def test_solution():
    sol = SolutionMemo()
    
    # Test case 1
    events1 = [[1,2,4],[3,4,3],[2,3,1]]
    k1 = 2
    print(f"Test 1: {sol.maxValue(events1, k1)}")  # Expected: 7
    
    # Test case 2
    events2 = [[1,2,4],[3,4,3],[2,3,10]]
    k2 = 2
    print(f"Test 2: {sol.maxValue(events2, k2)}")  # Expected: 10
    
    # Test case 3
    events3 = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
    k3 = 3
    print(f"Test 3: {sol.maxValue(events3, k3)}")  # Expected: 9

if __name__ == "__main__":
    test_solution()