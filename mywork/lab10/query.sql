USE eby2ch_db;
SELECT sp.id, sp.first_name, sp.last_name, sp.team, sp.goals, g.match_date, g.goal_time
FROM soccer_players sp
JOIN goals g ON sp.id = g.player_id;
