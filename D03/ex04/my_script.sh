#!/bin/bash

BANNER="$(
  cat <<-EOF
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_script.sh                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kimkwanho <kkim@student.42seoul.kr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    INIT Django Project !                             #+#    #+#              #
#                                                     ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
EOF
)"

LOG_FILE="pip_install.log"
PYTHON_PATH="/usr/bin/python3"
VENE_DIR="django_venv"

# print 42_HEADER
echo "$BANNER"

# setup venv
$PYTHON_PATH -m venv $VENE_DIR
source $VENE_DIR/bin/activate

# pip version
python -m pip --version

# pip install
python -m pip install --force-reinstall -r requirement.txt
