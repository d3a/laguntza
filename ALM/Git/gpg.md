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
**Obetner ID**
```bash
gpg --list-secret-keys --keyid-format=long
sec   ed25519/4D0F4326F8988D97 fecha [SC]
      BBBD0572D1FD7D42BC8752B54D0F4326F8988D97
uid              [  absoluta ] nombre (alias) <email>
ssb   cv25519/F26FAD8EBB5B3E0A fecha [E]
```
* sec   ed25519/**4D0F4326F8988D97** fecha [SC]


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

**Configurar Git para que use la glave gpg (Windows)**
```powershell
git config --global user.signingkey <gpg-key-ID>
git config --global gpg.program "c:/Program Files (x86)/GnuPG/bin/gpg.exe"
```
