# Docker Command Cheat Sheet

Covering the essential commands you will use daily.

## Building Images (The blueprint)
Before you can run an app, you need to build the image from your Dockerfile.

- docker build -t <~ name ~> . 
    <br> Builds an image from the Dockerfile in the current directory (.). 
    <br> -t: tags (names) the image so you can find it later.

- docker build -f <~ file ~> -t <~ name ~> .
    <br> Builds using a specific filename.

- docker images
    <br> Lists all the images downloaded or built on your machine.

- docker rmi <~ image_name ~>
    <br> Removes image. Deletes an image from your hard drive.


## Running Containers (The action)
Turning an image (blueprint) into a running container (house).

- docker run <~ image_name ~>
    <br> - Starts a container. Outputs logs onto your screen and dies when you hit ctrl + c.

- docker run -d <~ image_name ~>
    <br>-  Detatched mode.Runs the container in the background (Silently). It gives you the terminal back instantly.

- docker run -p 8080:80 <~ image_name ~>
    <br> - Port mapping. Connects port 8080 on your computer to port 80 inside the container.

- docker run -v $(pwd):/app <~ image_name ~>
    <br> - Volume mapping. Syncs your current folder (pwd) to /app inside the container.

- docker ps
    <br> - Process status. Lists all currently running containers.

- docker ps -a
    <br> - Lists All containers, including stopped or scrashed containers.

- docker stop <~ container id ~>
    <br> - Gracefully stops running a container.

- docker rm <~ container_id ~>
    <br> - Remove. Deletes a stopped container. (Cannot remove a running container).

## Debugging and inspecting
Commands to help look inside a container when something goes wrong.

- docker logs <~ container_id ~>
    <br> - Shows the output/print statements of a running container.
    <br> ~ To follow a container in real time use 'docker logs -f <~ id ~>'

- docker exec -it <~ id ~> sh 
    <br> - Execute. Creates a 'tunnel' into a running container so you can look inside.
    <br> ~ -it is an interactive terminal that lets you type
    <br> ~ sh is the shell command.

- docker inspect <~ id ~>
    <br> - Returns a huge JSON file with every detail about the container (IP address, volumes, environmental vars).

## Docker compose (The Orchestrator)
Managing multiple settings or contaienrs using docker-compose.yml.

- docker-compose up
    <br> - Builds images ad starts all services defined in docker-compose.yml.

- docker compose up -d
    <br> - Starts everything in Detached mode / in the background.

- docker-compose up --build
    <br> - Forces a rebuild of the images before starting (If you have made changes to the ENV or Dockerfile).

- docker-compose down
    <br> - Stops all containers and removes the networks created by up.

- docker-compose logs -f
    <br> - Follows the logs of all the services at once.

## System cleanup (Housekeeping)
Docker uses a lot of disk space. Some commands to help you clean up your system include:

- docker system prune
    <br> - The "Nuclear" option. Deletes all stopped containers, unused networks, and dangling images/images without a name.

- docker volume prune
    <br> - Deletes all unused volumes (This WILL delete persisten database data!).

## TIPS

- When typing in an image ID, you don't have to write the whole ID, you just need to type the first few characters.

- Sudo: When on linux you often have to write 'sudo docker', but not on windows or mac.

- Naming: you can name containers to make life easier i.e. docker run --name cat
<br> Now you can write docker stop cat.
