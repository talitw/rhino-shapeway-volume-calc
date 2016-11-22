#!/bin/bash

install_path="$HOME/Library/Application Support/McNeel/Rhinoceros/MacPlugins/PythonPlugins/ShapewaysVolumeCalc{16bc1df4-5d0d-4d08-8272-343d1d9ac81}/dev"
mkdir -p "$install_path"
cp ShapewaysVolumeCalc_cmd.py "$install_path"
