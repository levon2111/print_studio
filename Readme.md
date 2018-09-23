Print Studio Development Guide


##Database creation
###For psql
    sudo su - postgres
    psql
    DROP DATABASE IF EXISTS print;
    CREATE DATABASE print;
    CREATE USER print_user WITH password 'root';
    GRANT ALL privileges ON DATABASE print TO print_user;
    ALTER USER print_user CREATEDB;


Configure rabbitmq-server to run workers.
Add virtual host, and set permissions.

    $ sudo rabbitmqctl add_vhost print
    $ sudo rabbitmqctl add_user print_user root
    $ sudo rabbitmqctl set_permissions -p print print_user ".*" ".*" ".*"


Set up supervisor (pm2)

    $ sudo apt-get install python-software-properties
    $ curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
    $ sudo apt-get install nodejs
    $ cd /var/www/subdomains/codebnb/companify_api/public_html
    $ pm2 startup ubuntu14
    $ pm2 start scripts/manage_codebnb_init_default_consumer.sh --name print_api_init_default_consumer
    $ pm2 save
