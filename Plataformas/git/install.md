# Instalación

## Ubuntu 
Git & GitHub Client
```bash
apt install git
apt install gh
```

Inicializamos Git
```bash
git config --global user.email "email@server.mail"
git config --global user.name "userName"
gh auth login
# ? What account do you want to log into? GitHub.com
# ? What is your preferred protocol for Git operations? HTTPS
# ? Authenticate Git with your GitHub credentials? Yes
# ? How would you like to authenticate GitHub CLI? Login with a web browser
```

Clonar Proyecto
```bash
mkdir ${carpeta_base}
cd ${carpeta_base}
gh repo clone ${gitUser}/${repositorio}
carpeta_proyecto=${carpeta_base}/${repositorio}
```

Crear Proyecto
```bash
${repositorio}="laguntza-git"
${carpeta_base}="Proyerctos/laguntza"
${carpeta_repo}="git"
${carpeta_proyecto}="${carpeta_base}/${carpeta_repo}"

cd ${carpeta_proyecto}
git init
#git remote ${gitUser}/${repositorio}
```

