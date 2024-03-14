-- 1-create_user.sql
-- Create user_0d_1 with all privileges and a specific password. Do not fail if the user already exists.

-- Attempt to grant all privileges to the user, which will create the user if it doesn't exist
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd' WITH GRANT OPTION;

-- Ensure the password is set for the user (redundant if the user was just created above, but necessary if the user already existed)
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Apply changes immediately
FLUSH PRIVILEGES;
