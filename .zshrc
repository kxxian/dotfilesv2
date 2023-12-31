# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# Alias use for git to store my dotfiles
alias dotfiles="/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME"

# Alias for adapt commands to rewritten in rust commands 
alias ps="procs"
alias ls="exa --icons"

# Git alias 
alias g="git"

# Sail alias
alias sail="bash vendor/bin/sail"

# Fix lockscreen wallpaper 
alias blr="betterlockscreen -u ~/.lockscreen"

# Alias for lazyness
alias cc="clear"
alias sbg="feh --bg-fill --randomize /$HOME/.wallpapers/*"
alias archm=". $HOME/shell_scripts/archm.sh"
alias snaps=". $HOME/shell_scripts/snaps.sh"
alias snapl=". $HOME/shell_scripts/snapl.sh"
alias snapr=". $HOME/shell_scripts/snapr.sh"
alias snapd=". $HOME/shell_scripts/snapd.sh"


# Flutter 
export PATH="/$HOME/.flutter/flutter/bin:$PATH"

# .local
export PATH="$HOME/.local/bin:$PATH"


# Get fastest mirrors in your neighborhood 
alias mirror="sudo reflector -c 'Hong Kong' -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
alias mirrord="sudo reflector -c 'Hong Kong' --latest 50 --number 20 --sort delay --save /etc/pacman.d/mirrorlist"
alias mirrors="sudo reflector -c 'Hong Kong' --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist"
alias mirrora="sudo reflector -c 'Hong Kong' --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist"

# Load autosuggestions 
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh

# Load zsh theme
source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme

# Load fuzzy finder 
source /usr/share/fzf/key-bindings.zsh
source /usr/share/fzf/completion.zsh
