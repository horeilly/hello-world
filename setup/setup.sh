#sudo apt update
#sudo apt upgrade

#sudo apt install nginx

sudo cp hello-world.service /etc/systemd/system/hello-world.service

sudo systemctl daemon-reload
sudo systemctl start hello-world
sudo systemctl enable hello-world

printf "server {\n    listen 80;\n    server_name $(dig +short myip.opendns.com @resolver1.opendns.com);\n\n    location / {\n        include uwsgi_params;\n        uwsgi_pass unix:///home/$(whoami)/hello-world/hello-world/hello-world.sock;\n    }\n}\n" | sudo tee /etc/nginx/sites-available/hello-world > /dev/null

if ! [[ -L /etc/nginx/sites-enabled/hello-world ]]
then
    sudo ln -s /etc/nginx/sites-available/hello-world /etc/nginx/sites-enabled
fi

sudo systemctl restart nginx

if ! sudo ufw show added | grep -q "Nginx Full"
then
    sudo ufw allow "Nginx Full"
fi

