CREATE TABLE links (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    url VARCHAR(250),
    description VARCHAR(1000),
    views NUMERIC
);

INSERT INTO links (name, url, description, views)
VALUES
('fb', 'https://facebook.com', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel.', 5000),
('yt', 'https://youtube.com', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel..', 100),
('argocd', 'https://argoproj.github.io/cd', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel.', 250),
('twitch', 'https://twitch.tv', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel.', 1200);
