


def maximize_profit(n, possible_locations, possible_profits, k):
    
    total_profit = 0
    placed_locations = 0
    current_location = 1

    while current_location < len(possible_locations):
        if placed_locations >= n:
            break

        if (possible_profits[current_location] < possible_profits[current_location-1]):
            total_profit += possible_profits[current_location-1]
            store_location = possible_locations[current_location-1]
            print(store_location)
            placed_locations += 1
            while (current_location < len(possible_locations)) and (store_location + k < possible_locations[current_location-1]):
                current_location += 1
        
        while (current_location < len(possible_locations) and (n - placed_locations == (len(possible_locations) - current_location)/k)):
            total_profit += possible_profits[current_location]
            print(possible_locations[current_location])
            placed_locations += 1
            current_location += 1

        current_location += 1

    return total_profit

possible_locations = [0, 1, 2, 3, 4, 5, 6, 7, 8]
possible_profits =   [4, 10, 2, 5, 3, 5, 8, 100, 2]

print(maximize_profit(4, possible_locations, possible_profits, 1))