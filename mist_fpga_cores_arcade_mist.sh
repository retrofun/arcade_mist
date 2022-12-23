#!/bin/bash

# arcade_id
# arcade_name
# genre_id
# year
# manufacturer_hardware
# arcade_mist_url
# arcade_museum_id
# core_name
# note

# 1
# Arkanoid
# Ball and Paddle
# 1986
# Taito Arkanoid
# https://github.com/Gehstock/Mist_FPGA_Cores/tree/master/Arcade_MiST/Taito%20Arkanoid
# 6916 -> https://www.arcade-museum.com/game_detail.php?game_id=6916
#
#

arcade_cores="${HOME}/git/Mist_FPGA_Cores/Arcade_MiST/README.txt"
sep=';'

if ! [[ -f "${arcade_cores}" ]]; then
  echo "arcade cores file ${arcade_cores} does not exist"
  exit 1
fi

echo "arcade_id${sep}arcade_name${sep}genre_id${sep}year${sep}manufacturer_hardware${sep}arcade_mist_url${sep}arcade_museum_id${sep}core_name${sep}note"

IFS=''
new_hardware=1
id=1
while read line; do
  hardware=$(grep -E '^#' <<< "${line}")
  if [[ -n "${hardware}" ]]; then
    if [[ ${new_hardware} -eq 0 ]]; then
      echo "${id}${sep}*${current_hardware}${sep}${sep}${sep}${current_hardware}${sep}https://github.com/Gehstock/Mist_FPGA_Cores/tree/master/Arcade_MiST/${current_hardware}${sep}${sep}${sep}"
      id=$((id + 1))
    fi
    current_hardware="${hardware/\#/}"
    new_hardware=0
  fi

  arcade=$(grep -E $'^\t' <<< "${line}")
  if [[ -n "${arcade}" ]]; then
    if [[ "${current_hardware,,}" = "non arcade" ]]; then
      echo -n "#"
    fi
    echo "${id}${sep}${arcade/$'\t'/}${sep}${sep}${sep}${current_hardware}${sep}https://github.com/Gehstock/Mist_FPGA_Cores/tree/master/Arcade_MiST/${current_hardware}${sep}${sep}${sep}"
    id=$((id + 1))
    new_hardware=1
  fi
done <"${arcade_cores}"
