import calendar
import statistics

#(Direct = hard enforcement | Indirect = soft penalties for optimization)

def venue_availability(venue_name, day, timeslot, venue_time_slots):
    # Direct (hard constraint) - enforce feasibility
    if (venue_name, day, timeslot) in venue_time_slots:
        return 100  # large penalty if the venue is already booked
    return 0


def no_team_overlap(team1, team2, day, timeslot, team_time_slots):
    # Direct (hard constraint) - enforce feasibility
    if (team1, day, timeslot) in team_time_slots or (team2, day, timeslot) in team_time_slots:
        return 100  # large penalty for team overlap
    return 0


def venue_usage_balance(venue_usage):
    # Indirect (soft constraint) - optimize for balance
    # Calculate variance to measure uneven usage
    return int(statistics.variance(venue_usage) * 5)  # scaled soft penalty


def fair_rest_periods(team1, team2, team_time):
    days = dict(zip(calendar.day_name, range(7)))

    def get_rest(team):
        match_days = [days[match["day"]] for match in team_time.get(team, [])]
        if len(match_days) < 2:
            return None
        match_day_nums = sorted(match_days)
        return min((match_day_nums[-1] - match_day_nums[-2]) % 7, 7 - (match_day_nums[-1] - match_day_nums[-2]) % 7)

    rest1 = get_rest(team1)
    rest2 = get_rest(team2)

    penalty = 0
    for rest in [rest1, rest2]:
        if rest is not None and rest < 2:
            penalty += (2 - rest) * 5  # linear penalty for rest days < 2

    return penalty
