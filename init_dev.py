#!/usr/bin/env python3
"""
a script to quickly setup my termux devlopment env
"""
import os
import sys
import logging
from pathlib import Path
from typing import List, Set, Dict, Any

from logger import setup_logger
logger = logging.Logger(__name__)
setup_logger(logger)

def install():
    os.system("pkg update && pkg upgrade")
    pkg_to_install = ("mandoc", "vim", "net-tools",
                    "git", "golang", "rust", "fastfetch")
    pkgs_str = ""
    for pkg in pkg_to_install:
        pkgs_str = pkgs_str + pkg + " "

    os.system(f"pkg install {pkgs_str} -y")
    logger.info(f"auto installed: {pkgs_str}")

def setup_vim():
    os.system("curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim")
    vim_config = """\
syntax on
let g:airline_theme='onedark'
colorscheme onedark
call plug#begin()

" List your plugins here
Plug 'colors/onedark.vim'
Plug 'vim-airline/vim-airline'
Plug 'sheerun/vim-polyglot'

call plug#end()"""
    with open(Path.home().joinpath(".vimrc").as_posix(), "w") as f:
        f.write(vim_config)

if __name__ == '__main__':
    install()
    setup_vim()
