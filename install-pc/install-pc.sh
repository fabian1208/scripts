#!/bin/bash

## Installiamo i pacchetti che ci servono
# Pacman
sudo pacman -Syyu && sudo pacman -S rclone rsync ranger variety flatpak snap-pac neovim npm ttf-jetbrains-mono-nerd


# Yay

Yay -S librewolf-bin portmaster-stub-bin btrfs-assistant

# flatpak

flatpak install io.github.vikdevelop.SaveDesktop 

## Configurazione neovim

# Importiamo lo script per configurare neovim e lo eseguiamo

git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim

# impostiamo neovim come editor di default per il terminale


