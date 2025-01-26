#!/bin/bash
set -e

# Neuste Version von Hugo abrufen
VERSION=$(curl -s https://api.github.com/repos/gohugoio/hugo/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')
VERSION_CLEANED=${VERSION#v} # Entferne 'v' aus der Version

# Hugo herunterladen
wget https://github.com/gohugoio/hugo/releases/download/${VERSION}/hugo_extended_${VERSION_CLEANED}_Linux-64bit.tar.gz

# Entpacken und verschieben
tar -xzf hugo_extended_${VERSION_CLEANED}_Linux-64bit.tar.gz
sudo mv hugo /usr/local/bin/

# Bereinigen
rm -f hugo_extended_${VERSION_CLEANED}_Linux-64bit.tar.gz

# Erfolgsmeldung
echo "Hugo $VERSION installiert!"
 
