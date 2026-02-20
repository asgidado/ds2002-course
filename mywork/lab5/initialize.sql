CREATE TABLE soccer_players (
    id INT PRIMARY KEY, -- Primary key for soccer_players
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    team VARCHAR(50),
    goals VARCHAR(20)
);


CREATE TABLE goals (
    goal_id INT PRIMARY KEY, -- Primary key for goals table
    player_id INT,           -- Foreign key referencing soccer_players
    match_date DATE,
    goal_time TIME,
    FOREIGN KEY (player_id) REFERENCES soccer_players(id) -- Foreign key constraint
);

-- Insert data into soccer_players table
INSERT INTO soccer_players (id, first_name, last_name, team, goals) VALUES (1, 'Lionel', 'Messi', 'PSG', '30');
INSERT INTO soccer_players (id, first_name, last_name, team, goals) VALUES (2, 'Cristiano', 'Ronaldo', 'Al-Nassr', '25');
INSERT INTO soccer_players (id, first_name, last_name, team, goals) VALUES (3, 'Kylian', 'Mbappe', 'PSG', '28');
INSERT INTO soccer_players (id, first_name, last_name, team, goals) VALUES (4, 'Neymar', 'Junior', 'PSG', '20');
INSERT INTO soccer_players (id, first_name, last_name, team, goals) VALUES (5, 'Robert', 'Lewandowski', 'Barcelona', '35');
INSERT INTO soccer_players (id, first_name, last_name, team, goals) VALUES (6, 'Erling', 'Haaland', 'Man City', '40');
INSERT INTO soccer_players (id, first_name, last_name, team, goals) VALUES (7, 'Kevin', 'De Bruyne', 'Man City', '15');
INSERT INTO soccer_players (id, first_name, last_name, team, goals) VALUES (8, 'Mohamed', 'Salah', 'Liverpool', '25');
INSERT INTO soccer_players (id, first_name, last_name, team, goals) VALUES (9, 'Harry', 'Kane', 'Tottenham', '27');
INSERT INTO soccer_players (id, first_name, last_name, team, goals) VALUES (10, 'Karim', 'Benzema', 'Real Madrid', '30');

-- Insert data into goals table
INSERT INTO goals (goal_id, player_id, match_date, goal_time) VALUES (1, 1, '2026-02-01', '15:30:00');
INSERT INTO goals (goal_id, player_id, match_date, goal_time) VALUES (2, 2, '2026-02-02', '20:15:00');
INSERT INTO goals (goal_id, player_id, match_date, goal_time) VALUES (3, 3, '2026-02-03', '18:45:00');
INSERT INTO goals (goal_id, player_id, match_date, goal_time) VALUES (4, 4, '2026-02-04', '19:00:00');
INSERT INTO goals (goal_id, player_id, match_date, goal_time) VALUES (5, 5, '2026-02-05', '21:10:00');
INSERT INTO goals (goal_id, player_id, match_date, goal_time) VALUES (6, 6, '2026-02-06', '16:20:00');
INSERT INTO goals (goal_id, player_id, match_date, goal_time) VALUES (7, 7, '2026-02-07', '17:50:00');
INSERT INTO goals (goal_id, player_id, match_date, goal_time) VALUES (8, 8, '2026-02-08', '14:30:00');
INSERT INTO goals (goal_id, player_id, match_date, goal_time) VALUES (9, 9, '2026-02-09', '13:45:00');
INSERT INTO goals (goal_id, player_id, match_date, goal_time) VALUES (10, 10, '2026-02-10', '12:15:00');

