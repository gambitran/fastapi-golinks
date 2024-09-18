CREATE TABLE links (
    id SERIAL,
    name VARCHAR(100),
    url VARCHAR(250),
    description VARCHAR(1000),
    views NUMERIC,
    PRIMARY KEY (id, name)
);

INSERT INTO links (name, url, description, views)
VALUES
('fb', 'https://facebook.com', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel. Curabitur iaculis malesuada est, et tempus justo sollicitudin id. Suspendisse dapibus justo ut sem malesuada, et tempus ipsum condimentum. Integer dictum risus arcu, efficitur elementum ipsum posuere ac.', 5000),
('yt', 'https://youtube.com', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel. Curabitur iaculis malesuada est, et tempus justo sollicitudin id. Suspendisse dapibus justo ut sem malesuada, et tempus ipsum condimentum. Integer dictum risus arcu, efficitur elementum ipsum posuere ac.', 100),
('argocd', 'https://argoproj.github.io/cd', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel. Curabitur iaculis malesuada est, et tempus justo sollicitudin id. Suspendisse dapibus justo ut sem malesuada, et tempus ipsum condimentum. Integer dictum risus arcu, efficitur elementum ipsum posuere ac.', 250),
('twitch', 'https://twitch.tv', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel. Curabitur iaculis malesuada est, et tempus justo sollicitudin id. Suspendisse dapibus justo ut sem malesuada, et tempus ipsum condimentum. Integer dictum risus arcu, efficitur elementum ipsum posuere ac.', 1200);
