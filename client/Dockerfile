# Utilisez une image de base appropriée pour l'application Node.js
FROM node:alpine

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers nécessaires de votre projet dans le conteneur
COPY . .

# Installez les dépendances de l'application
RUN npm install

# Construit l'application
RUN npm run build

# Exposez le port sur lequel l'application va écouter
EXPOSE 3000

# Commande pour démarrer l'application
CMD ["npm", "start"]