# Problem name: CCC '20 J2 - Epidemiology
# Code: ccc20j2
# Link: https://dmoj.ca/problem/ccc20j2

people_limit = int(input())
n_people_infected = int(input())
r_new_infected = int(input())
days = 0
new_infected_people = n_people_infected

while people_limit >= n_people_infected:
    new_infected_people =  new_infected_people * r_new_infected
    n_people_infected = n_people_infected + new_infected_people
    days = days + 1

print(days)