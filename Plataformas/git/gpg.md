# GPG

[Referencia](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification)
- [Generar Clave GPG](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key)
- [Añadir clave en GitHub](https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-gpg-key-to-your-github-account)
- [Añadir clave a Git](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key)

**Instalar**
```bash
apt get gnupg
```
**Revisar claves existentes**
```bash
gpg --list-secret-keys --keyid-format=long
```
**Generar una nueva clave**
```bash
gpg --full-generate-key
```
**Exportar clave púiblica** para añadir a GitHub
```bash
gpg --armor --export <gpg-key-ID>
```
**Configurar Git para que use la glave gpg**
```bash
git config --global user.signingkey <gpg-key-ID>
# Para que por defecto se firmen todos los commits
git config --global commit.gpgsign true
# (¿?)To add your GPG key to your .bashrc startup file, run the following command
[ -f ~/.bashrc ] && echo 'export GPG_TTY=$(tty)' >> ~/.bashrc
```
