# Instalación Git

**Git & GitHub Client**
```bash
apt install git
apt install gh
```

**Inicializamos Git**
```bash
git config --global user.name "userName"
git config --global user.email "email@server.mail"
gh auth login
# ? What account do you want to log into? GitHub.com
# ? What is your preferred protocol for Git operations? HTTPS
# ? Authenticate Git with your GitHub credentials? Yes
# ? How would you like to authenticate GitHub CLI? Login with a web browser
git config --global user.signingkey <gpg-key-ID>
git config --global commit.gpgsign true
```
Para las gestión de claves GPG ver [gpg.md](gpg.md)

**Clonar Proyecto**
```bash
repositorio="laguntza"
carpeta_base="Proyectos"
carpeta_repo="laguntza"
carpeta_proyecto="${carpeta_base}/${carpeta_repo}"

mkdir ${carpeta_base}
cd ${carpeta_base}
gh repo clone ${gitUser}/${repositorio}
cd ${carpeta_proyecto}
```

**Crear Proyecto**
```bash
repositorio="laguntza"
carpeta_base="Proyectos"
carpeta_repo="laguntza"
carpeta_proyecto="${carpeta_base}/${carpeta_repo}"

mkdir ${carpeta_proyecto}
cd ${carpeta_proyecto}
git init
touch .gitignore
git add *
git commit -S -m "Version inicial"
git branch -M main
git remote add origin https://github.com/d3a/laguntza-ansible.git
git push -u origin main
```
[gitignore.md](gitignore.md)
