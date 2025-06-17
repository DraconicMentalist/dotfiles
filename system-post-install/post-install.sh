sudo pacman -S git python python-sh python-termcolor rustup hwinfo choose ripgrep fd gum fzf yazi zoxide btop vim ghostty rofi dolphin keepassxc xdg-desktop-portal-gtk xdg-desktop-portal-gnome gnome-keyring zsh yadm lazygit lsd wl-clipboard
rustup default stable
sudo pacman -S --needed base-devel
cd /tmp
mkdir repos
cd repos
git clone https://aur.archlinux.org/paru.git
cd paru
mkpkg -si
paru -S niri-git xwayland-satellite-gi gyr zen-browser-bin discord-canary dropbox-cli
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

rm ~/.zshrc
wget https://raw.githubusercontent.com/DraconicMentalist/dotfiles/refs/heads/main/.zshrc 

# still needed:
# - [ ] install nerd fonts
# - [ ] auto-install dotfiles
# - [ ] auto-install portable neovim
# - [ ] install terminal theme
# - [ ] auto-apply themes
