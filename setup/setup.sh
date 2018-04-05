#sudo apt update
#sudo apt upgrade

#sudo apt install nginx

sudo cp hello-world.service /etc/systemd/system/hello-world.service

printf "[Unit]\n" | sudo tee /etc/systemd/system/hello-world.service > /dev/null
printf "Description=uWSGI instance to serve hello-world\n" | sudo tee -a /etc/systemd/system/hello-world.service > /dev/null
printf "After=network.target\n" | sudo tee -a /etc/systemd/system/hello-world.service > /dev/null
printf "\n" | sudo tee -a /etc/systemd/system/hello-world.service > /dev/null
printf "[Service]\n" | sudo tee -a /etc/systemd/system/hello-world.service > /dev/null
printf "User=ubuntu\n" | sudo tee -a /etc/systemd/system/hello-world.service > /dev/null
printf "Group=www-data\n" | sudo tee -a /etc/systemd/system/hello-world.service > /dev/null
printf "WorkingDirectory=/home/ubuntu/hello-world/hello-world\n" | sudo tee -a /etc/systemd/system/hello-world.service > /dev/null
printf "Environment=\"PATH=/home/ubuntu/hello-world/env/bin\"\n" | sudo tee -a /etc/systemd/system/hello-world.service > /dev/null
printf "ExecStart=/home/ubuntu/hello-world/env/bin/uwsgi --ini hello-world.ini\n" | sudo tee -a /etc/systemd/system/hello-world.service > /dev/null
printf "\n" | sudo tee -a /etc/systemd/system/hello-world.service > /dev/null
printf "[Install]\n" | sudo tee -a /etc/systemd/system/hello-world.service > /dev/null
printf "WantedBy=multi-user.target\n" | sudo tee -a /etc/systemd/system/hello-world.service > /dev/null

sudo systemctl daemon-reload
sudo systemctl start hello-world
sudo systemctl enable hello-world

printf "server {\n" | sudo tee /etc/nginx/sites-available/hello-world > /dev/null
printf "    listen 80;\n" | sudo tee -a /etc/nginx/sites-available/hello-world > /dev/null
printf "    server_name $(dig +short myip.opendns.com @resolver1.opendns.com);\n" | sudo tee -a /etc/nginx/sites-available/hello-world > /dev/null
printf "\n" | sudo tee -a /etc/nginx/sites-available/hello-world > /dev/null
printf "    location / {\n" | sudo tee -a /etc/nginx/sites-available/hello-world > /dev/null
printf "        include uwsgi_params;\n" | sudo tee -a /etc/nginx/sites-available/hello-world > /dev/null
printf "        uwsgi_pass unix:///home/$(whoami)/hello-world/hello-world/hello-world.sock;\n" | sudo tee -a /etc/nginx/sites-available/hello-world > /dev/null
printf "    }\n" | sudo tee -a /etc/nginx/sites-available/hello-world > /dev/null
printf "}\n" | sudo tee -a /etc/nginx/sites-available/hello-world > /dev/null

if ! [[ -L /etc/nginx/sites-enabled/hello-world ]]
then
    sudo ln -s /etc/nginx/sites-available/hello-world /etc/nginx/sites-enabled
fi

sudo systemctl restart hello-world
sudo systemctl restart nginx

if ! sudo ufw show added | grep -q "Nginx Full"
then
    sudo ufw allow "Nginx Full"
fi

