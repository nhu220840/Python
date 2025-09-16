distance_between_house_and_shop1, distance_between_house_and_shop2, distance_between_two_shops = map(int, input().split())

method1 = distance_between_house_and_shop1 * 2 + distance_between_house_and_shop2 * 2
method2 = distance_between_house_and_shop1 + distance_between_two_shops + distance_between_house_and_shop2
method3 = distance_between_house_and_shop1 * 2 + distance_between_two_shops * 2
method4 = distance_between_house_and_shop2 * 2 + distance_between_two_shops * 2

minimum_distance = min(method1, method2, method3, method4)

print(minimum_distance)