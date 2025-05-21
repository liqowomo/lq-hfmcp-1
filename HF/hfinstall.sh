#!/usr/bin/bash
# This bash srcript is for installing the KL docker image here
clear

# Colors
export RED='\033[0;31m'
export GREEN='\033[0;32m'
export YELLOW='\033[0;33m'
export BLUE='\033[0;34m'
export PURPLE='\033[0;35m'
export CYAN='\033[0;36m'
export WHITE='\033[0;37m'
export NC='\033[0m' # No Color

# Commands

he1() {
    echo -e "${CYAN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${NC}"
    echo -e "${PURPLE}$1${NC}"
    echo -e "${CYAN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${NC}"
}

# --- HF install Command ---

# Installs the HF CLI
hf_in() {
    h1 "HF Pip Install"
    co1='pip install -U "huggingface_hub[cli]"'
    echo -e "--- Executing ${co1} ---"
    eval "$co1"
}

# Repo Creation Commands
hf_repo() {
    h1 "HF Repo Creation"
    co2='huggingface-cli repo create myrepo1'
    echo -e "--- Executing ${co2} ---"
    eval "$co2"
}

# Execution
hf_repo
