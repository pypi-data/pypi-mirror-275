# d2cd
> **Note:** This project is currently under active development.

<p align="center">
  <img src="https://i.ibb.co/8b7SMTH/d2cd1.png" width="400"/>
</p>

**D**ocker **C**ompose **C**ontinuous **D**elivery (`d2cd`) is a GitOps agent designed to maintain the state of your Docker Compose projects on your server by continuously applying changes from a Git repository.

## Install
Docker Compose is the recomended way
```bash
# download docker-compose.yml
$ wget https://raw.githubusercontent.com/veerendra2/d2cd/main/docker-compose.yml

# configure `config.yml` and run
$ docker compose up -d
```
From source
> **Note:** This tool is currently in beta stage, and daemonization is not yet implemented.
```
$ git clone git@github.com:veerendra2/d2cd.git
$ cd d2cd
$ pip3 install .
```

## Configuration
Below is a sample `config.yml` file to help you get started:

```yaml
---
sync_interval_seconds: 600
repos:
  - name: d2cd-test
    url: git@github.com:veerendra2/d2cd-test-repo.git
    branch: main
    auth:
      ssh_key_location: "~/.ssh/id_rsa"
    docker_compose_paths:
      - python/docker-compose.yml
```
You can also use `username` and `password`(`token`) for authentication

```yaml
sync_interval_seconds: 600
repos:
  - name: d2cd-test
    url: git@github.com:veerendra2/d2cd-test-repo.git
    branch: main
    auth:
      username: "USERNAME"
      password: "PASSWORD"
    docker_compose_paths:
      - python/docker-compose.yml
```
