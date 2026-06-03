def mineatspeed(piles,h):
    left = 1
    right = max(piles)
    answer = right
    def caneat(speed):
        total_hour = 0
        for pile in piles:
            hours = (pile + speed - 1)//speed
            total_hour += hours
        return total_hour <= h
    while left <= right:
        mid = (left + right)//2
        if caneat(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

piles = [3,6,7,11]
h = 8

print(mineatspeed(piles,h))
