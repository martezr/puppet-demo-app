# Puppet Demo App

A simple microservice architecture for demonstration purposes.

| name | function |
|------|----------|
|frontend|Python flask web application for displaying the web page|
|name|The name service that generates random names|
|password|The password service that generates random passwords|

## Getting Started

The application comes with a docker-compose file for running the application locally.

Clone the Github repository

```bash
git clone https://github.com/martezr/puppet-demo-app.git
```

Change current working directory to the Github repository

```bash
cd puppet-demo-app
```

Start the application by using docker-compose

```bash
docker-compose up -d
```

The web page can based access by opening a web browser to the following address.

http://localhost
