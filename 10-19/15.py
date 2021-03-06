# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

cache = {}

def get_route_count(grid_width, grid_height, x, y):
    key = "{},{}".format(x,y)

    if key in cache:
        return cache[key]

    if x == grid_width:
        cache[key] = 1
        return 1

    if y == grid_height:
        cache[key] = 1
        return 1

    route_count = 0
    
    route_count += get_route_count(grid_width, grid_height, x + 1, y)        
    route_count += get_route_count(grid_width, grid_height, x, y + 1)        

    cache[key] = route_count
    return route_count

print(get_route_count(20, 20, 0, 0))