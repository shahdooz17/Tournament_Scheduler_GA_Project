from scheduler import constraints as c
from data import load_data as ld

teams = ld.load_teams()
venues = ld.load_venues()

def fitness(schedule):
    penalty = 0

    venue_time_slots = set() 
    team_time_slots = set()  
    venue_usage = {venue["name"]: 0 for venue in venues} 
    team_time = {team["name"]: [] for team in teams} 

    for match in schedule:
        team1 = match["team1"]
        team2 = match["team2"]
        day = match["day"]
        timeslot = match["time"]
        venue_name = match["venue"]

        venue_avail = c.venue_availability(venue_name, day, timeslot, venue_time_slots)
        team_overlap = c.no_team_overlap(team1, team2, day, timeslot, team_time_slots)
        fair_rest = c.fair_rest_periods(team1, team2, team_time)

        penalty += (venue_avail + team_overlap + fair_rest)

        venue_time_slots.add((venue_name, day, timeslot))
        team_time_slots.add((team1, day, timeslot))
        team_time_slots.add((team2, day, timeslot))
        
        venue_usage[venue_name] += 1
        team_time[team1].append(match)
        team_time[team2].append(match)

    penalty += c.venue_usage_balance(list(venue_usage.values()))
    
    return penalty
