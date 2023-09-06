import json
import subprocess

# Fonction pour charger la configuration depuis le fichier JSON
def load_config(file_path):
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        print(f"Le fichier de configuration {file_path} n'a pas été trouvé.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erreur lors de la lecture du fichier JSON : {e}")
        return None


# Fonction pour générer les fichiers Dockerfile pour chaque service
def generate_dockerfiles(services):
    for service_name in services:
        dockerfile_content = f'''
# Utilisez une image de base appropriée pour l'application {service_name}
FROM node:alpine

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers nécessaires de votre projet dans le conteneur
COPY . .

# Installez les dépendances de l'application
RUN npm install

# Exposez le port sur lequel l'application va écouter
EXPOSE 4005

# Commande pour démarrer l'application
CMD ["npm", "start"]
'''
        # Écrivez le contenu du Dockerfile dans un fichier
        dockerfile_name = f"{service_name}/Dockerfile"
        with open(dockerfile_name, 'w') as dockerfile:
            dockerfile.write(dockerfile_content)
        print(f"Fichier Dockerfile créé pour {service_name}.")

# Fonction pour construire et pousser une image Docker
def build_and_push_docker_image(service_name, user_docker_hub):
    docker_build_command = f"docker build -t {service_name} ./{service_name}"
    docker_tag_command = f"docker tag {service_name} {user_docker_hub}/{service_name}:latest"
    docker_push_command = f"docker push {user_docker_hub}/{service_name}:latest"

    try:
        subprocess.run(docker_build_command, shell=True, check=True)
        subprocess.run(docker_tag_command, shell=True, check=True)
        subprocess.run(docker_push_command, shell=True, check=True)
        print(f"Image Docker pour {service_name} construite et poussée avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la construction et de la poussée de l'image Docker pour {service_name}: {e}")

if __name__ == "__main__":
    config_path = "config.json"
    config = load_config(config_path)

    if config:
        user_docker_hub = config.get("userdockerhub")
        services = config.get("services")

        if user_docker_hub and services:
            for service_name in services:
                build_and_push_docker_image(service_name, user_docker_hub)
        else:
            print("Configuration incomplète. Assurez-vous que 'userdockerhub' et 'services' sont définis dans le fichier config.json.")
