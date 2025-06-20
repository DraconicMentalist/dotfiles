sudo pacman -S --needed base-devel
cd /tmp
mkdir repos
cd repos
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
