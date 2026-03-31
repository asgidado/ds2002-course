SELECT 
    s.first_name, 
    s.last_name, 
    s.team, 
    g.match_date, 
    g.goal_time
FROM soccer_players s
JOIN goals g ON s.id = g.player_id
WHERE s.team = 'PSG';

