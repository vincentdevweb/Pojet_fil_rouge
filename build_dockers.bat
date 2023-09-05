@echo off

rem Liste des services que vous souhaitez construire
set services=client posts comments event-bus moderation query
set userdockerhub=vincentdevweb

rem Parcours de la liste des services et construction de chaque image Docker
for %%service in (%services%) do (
    docker build -t %%service .\%%service
    docker tag %%service %%userdockerhub\%%service:latest
    docker push %%userdockerhub\%%service:latest
)
