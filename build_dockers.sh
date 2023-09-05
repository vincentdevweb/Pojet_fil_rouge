#!/bin/bash

# Liste des services
services=("client" "posts" "comments" "event-bus" "moderation" "query")
userdockerhub="vincentdevweb"

# Parcours de la liste des services et construction de chaque image Docker
for service in "${services[@]}"; do
    docker build -t "$userdockerhub/$service" "./$service"
    docker tag "$userdockerhub" "$userdockerhub/$service:latest"
    docker push "$userdockerhub/$service:latest"
done

# Si besoin : chmod +x build_dockers.sh && ./nom_du_script.sh

