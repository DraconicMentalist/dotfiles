sudo pacman -S git python python-sh python-termcolor rustup hwinfo choose ripgrep fd gum fzf yazi zoxide btop vim ghostty rofi dolphin keepassxc xdg-desktop-portal-gtk xdg-desktop-portal-gnome gnome-keyring zsh yadm lazygit lsd wl-clipboard ouch
rustup default stable
rustup target add x86_64-pc-windows-msvc
sudo pacman -S --needed base-devel
cd /tmp
mkdir repos
cd repos
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
paru -S niri-git xwayland-satellite-gi gyr zen-browser-bin discord-canary dropbox-cli ttf-maplemono
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
curl -sS https://starship.rs/install.sh | sh

rm ~/.zshrc
cd ~/
wget https://raw.githubusercontent.com/DraconicMentalist/dotfiles/refs/heads/main/.zshrc 
