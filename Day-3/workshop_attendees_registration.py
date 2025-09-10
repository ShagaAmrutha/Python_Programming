day1 = ["Alice@mail.com", "bob@Mail.com", "charlie@mail.com", "alice@mail.com"]
day2 = ["BOB@mail.com", "david@mail.com", "charlie@mail.com", "eve@mail.com"]
day3 = ["alice@mail.com", "eve@mail.com", "Frank@mail.com", "charlie@mail.com"]
d1=set(i.lower() for i in day1)
d2=set(i.lower() for i in day2)
d3=set(i.lower() for i in day3)
unq_attendees=d1|d2|d3
all_three_days=d1&d2&d3
only_one = (d1 ^ d2 ^ d3) - all_three_days
print("Total unique:", len(unq_attendees), sorted(unq_attendees))
print("All 3 days:", len(all_three_days), sorted(all_three_days))
print("Exactly 1 day:", len(only_one), sorted(only_one))
print("Day1 & Day2:", len(d1 & d2), sorted(d1 & d2))
print("Day2 & Day3:", len(d2 & d3), sorted(d2 & d3))
print("Day1 & Day3:", len(d1 & d3), sorted(d1 & d3))