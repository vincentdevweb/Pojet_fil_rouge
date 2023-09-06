# Projet fil rouge
```
 _______   ______  __       __        ______   ______  
|       \ /      \|  \     |  \      /      \ /      \ 
| ▓▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓     | ▓▓     |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\
| ▓▓__/ ▓▓ ▓▓__| ▓▓ ▓▓     | ▓▓     | ▓▓__| ▓▓ ▓▓___\▓▓
| ▓▓    ▓▓ ▓▓    ▓▓ ▓▓     | ▓▓     | ▓▓    ▓▓\▓▓    \ 
| ▓▓▓▓▓▓▓| ▓▓▓▓▓▓▓▓ ▓▓     | ▓▓     | ▓▓▓▓▓▓▓▓_\▓▓▓▓▓▓\
| ▓▓     | ▓▓  | ▓▓ ▓▓_____| ▓▓_____| ▓▓  | ▓▓  \__| ▓▓
| ▓▓     | ▓▓  | ▓▓ ▓▓     \ ▓▓     \ ▓▓  | ▓▓\▓▓    ▓▓
 \▓▓      \▓▓   \▓▓\▓▓▓▓▓▓▓▓\▓▓▓▓▓▓▓▓\▓▓   \▓▓ \▓▓▓▓▓▓ 
                                                       
```
## Introduction

Ce projet est une application microservices construite avec Node.js et React. Il est conçu pour être déployé sur Kubernetes.

## Table des matières

- [Introduction](#introduction)
- [Table des matières](#table-des-matières)
- [Architecture](#architecture)
- [Chemins d'Ingress](#chemins-dingress)
- [Noms de Services Kubernetes](#noms-de-services-kubernetes)
- [Ports des Services](#ports-des-services)
- [Prérequis](#prérequis)
- [Quick Start](#quick-start)
- [Installation with docker hub image](#installation-with-docker-hub-image)
- [Déploiement](#déploiement)
- [Auteur](#auteur)

## Architecture

L'application est composée des services suivants :

- **Client** : Interface utilisateur construite avec React.
- **Posts** : Service pour la gestion des posts.
- **Comments** : Service pour la gestion des commentaires.
- **Query** : Service pour la gestion des requêtes.
- **Moderation** : Service pour la modération des commentaires.
- **Event Bus** : Service pour la gestion des événements entre les services.

### Chemins d'Ingress

- `/posts/create` : Dirigé vers le service `posts-clusterip-srv` sur le port 4000.
  - Utilisé pour créer de nouveaux posts.
  
- `/posts` : Dirigé vers le service `query-srv` sur le port 4002.
  - Utilisé pour récupérer la liste des posts existants.
  
- `/posts/?(.*)/comments` : Dirigé vers le service `comments-srv` sur le port 4001.
  - Utilisé pour créer ou récupérer les commentaires associés à un post spécifique.
  
- `/?(.*)` : Dirigé vers le service `client-srv` sur le port 3000.
  - Utilisé pour accéder à l'interface utilisateur.
 


### Noms de Services Kubernetes

Assurez-vous que les noms de services dans vos fichiers de déploiement Kubernetes correspondent aux noms de services utilisés dans le code de l'application. Voici les noms de services attendus :

- **client-srv**: Service pour l'interface utilisateur.
- **posts-clusterip-srv**: Service pour la gestion des posts.
- **query-srv**: Service pour la gestion des requêtes.
- **comments-srv**: Service pour la gestion des commentaires.
- **moderation-srv**: Service pour la modération des commentaires.
- **event-bus-srv**: Service pour la gestion des événements entre les services.

Si vous modifiez ces noms, assurez-vous également de mettre à jour les références correspondantes dans le code de l'application.


### Ports des Services

Chaque service écoute sur un port spécifique. Assurez-vous que ces ports sont correctement configurés dans vos fichiers de déploiement Kubernetes et dans tout autre outil de gestion des conteneurs que vous pourriez utiliser. Voici les ports attendus pour chaque service :

- **client-srv**: Écoute sur le port 3000.
- **posts-clusterip-srv**: Écoute sur le port 4000.
- **query-srv**: Écoute sur le port 4002.
- **comments-srv**: Écoute sur le port 4001.
- **moderation-srv**: Écoute sur le port 4003.
- **event-bus-srv**: Écoute sur le port 4005.

Si vous modifiez ces ports, assurez-vous également de mettre à jour les références correspondantes dans le code de l'application et les fichiers de configuration Kubernetes.


## Prérequis

- Node.js
- Docker / Docker Desktop
- Kubernetes

## Quick Start

Clonez ce dépôt :
```sh
git clone https://github.com/vincentdevweb/Pojet_fil_rouge.git
```

Puis allez a la section [Deploiement](#déploiement) pour avoir une installation rapide sinon pour plus de configuration allez à [Installation with docker hub image](#installation-with-docker-hub-image)
## Installation with docker hub image

1. Verifier que vous êtes log sur docker hub :
    ```bash
    docker login
    ```

2. Changer le nom de l'utilisateur dans les fichiers suivant :
    ```bash
    build_dockers.bat ou build_dockers.sh
    ```
    Puis dans le dossier k8s les fichiers
    ```bash
    *-depl.yml
    >>>>> modifier la cible dans les fichiers
    image: <my-username-dockerhub>/*
    ```

3. Installez les conteneurs depuis le dossier racine:
    
    ```bash
    Windows :
    ./build_dockers.bat

    ou Linux : 
    ./build_dockers.sh 
    ```

Maintenant rendez-vous à l'étape [Deploiement](#déploiement)

## Déploiement

Déployez les services sur Kubernetes :

```sh
kubectl apply -f k8s/
```

## Auteur

**_PALLAS_**
