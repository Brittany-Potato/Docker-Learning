# What is Docker?

Docker is a platform that allows you to seperate your application from your infrastructure so you can deliver software quickly.

## What does it solve?

It eliminates the 'It works on my machine' problem. If it works in a Docker container on your laptop, it will work on your friends laptop, the company server, or the cloud, because the environment is identical. 

### Analogy

Think of it like a shipping container. Before shipping containers, goods were loaded onto ships hapazardly (Barrels, sacks, boxes). It was slow and hard to stack.

- Docker Containers are standard boxes for software. It doesn't matter what is inside (Python, Node.js, Java) or what ship carries it (Linux, Windows, macOS) the box is always handled the same way.

# Containers vs. Virtual machines (VMs)

- Virtual machines: Virtualize the Hardware. Each VM has a full operating system (OS). They are heavy (GBs in size) and slow to boot.
- Docker containers: Virtualize the Operating System. They share the host machine's OS kernel but keep processes isolated. They are light weight (MBs in size) and start instantly.

# Key terminology

### Dockerfile (The Recipe)

A text file containing instructions on how to build a Docker image. It is like a recipe card.

- Example: "Start with Python, copy my files here, and install these libraries"

### Image (The blueprint)

The read-only template built from a Dockerfile.

- An image is the "frozen" state of an application.
- You cannot edit an image once its built, you have to rebuild it when you make changes.

### Container (The house)

A runnable instance of an image.

- You can create, start, stop, move, or delete a container.
- If an image is a "Class" in programming, a Container is an "Object" (An instance of that class).

### Docker Hub (The store)

A cloud-based registry service. It is like "Github for docker images".

- You can pull official images (like node, python, mysql) created by others to base your project on.

# How to use Docker

### 1 Docker CLI (Command line Interface)

The primary way to interact with Docker using commands in your terminal (e.g. docker run, docker build)

### 2. Docker Desktop

A visual application (GUI) for mac, windows, and linux that lets you see your running containers, view logs, and manage settings without typing commands.

### 3. Docker Compose

A tool for defining and running multi-container Docker applications.

- Instead of running one manual command to start a database and another to start a web server, you can use a docker-compose.yml file to start them all at the same time using one command.

# What does 'Containerizing' mean?

Containerizing an app (or script) involves bundling the code with all its depedencies (libraries, configuration files, environment variables) so it can run anywhere.

### The work flow:

1. Code: You write your script.
2. Dockerfile: You write a file telling Docker what OS to use and what dependencies to install.
3. Build: You tell Docker to turn that Dockerfile into an image.
4. Run: You tell Docker to run that image as a Container.