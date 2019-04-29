#!/bin/bash
# So you don't have to put sudo in front of your commands if needed
set -e
# so you don't have to place sudo in front of all commands
if [ "$(id -u)" != "0" ]; then
 	exec sudo "$0" "$@" 
fi


if ! brew_loc="$(type -p "$brew")" || [[ -z $brew_loc ]]; then
	printf "brew is already installed.\n"
else
	# install brew here
	printf "Installing brew...\n"
	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	printf "brew is installed\n"
  exit
fi

if ! ruby_loc="$(type -p "$ruby")" || [[ -z $ruby_loc ]]; then
	printf "ruby is already installed.\n"
else
	# install ruby here
	printf "Now installing ruby...\n"
	brew install postgres
	printf "Ruby is installed\n"
fi

if ! psql_loc="$(type -p "$psql")" || [[ -z $psql_loc ]]; then
  printf "Postgres is already installed\n"
else
	# install Postgres here
	printf "Now installing postgres...\n"
	brew install postgres
	pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
	createdb restapi
	psql restapi
	printf "Postgres is installed, created \"restapi\" database and started the server...\n"
fi

python3 -m venv env
source env/bin/activate