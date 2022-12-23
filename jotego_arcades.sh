#!/bin/bash

jtbin_mist_rbfs='/tmp/jtbin_mist_rbfs.txt'
jtbin_mra="${HOME}/git/jtbin/mra"

pushd ~/git/jtbin/mist >/dev/null
ls -1 *.rbf >"${jtbin_mist_rbfs}"
popd >/dev/null

IFS=$'\n'
while read rbf; do
  echo "${rbf}"
  echo
  grep -F "<rbf>${rbf%.rbf}</rbf>" "${jtbin_mra}"/*.mra
  echo
done <"${jtbin_mist_rbfs}"
