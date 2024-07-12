#!/bin/bash

# Array of package names
packages=(
  numpy
  pandas
  scipy
  scikit-learn
  matplotlib
  seaborn
  jupyter
  ipykernel
  ipywidgets
  tqdm
  torch
  torchvision
  torchaudio
  transformers
  datasets
  langchain
  chromadb
  sentence-transformers
  faiss-cpu
  prefect
  python-dotenv
)

# Function to check package compatibility with Python 3.9
check_compatibility() {
  package=$1
  url="https://pypi.org/pypi/$package/json"
  
  metadata=$(curl -s $url)
  requires_python=$(echo "$metadata" | jq -r '.info.requires_python')
  version=$(echo "$metadata" | jq -r '.info.version')
  requires_dist=$(echo "$metadata" | jq -r '.info.requires_dist | join(", ")')
  
  compatible_versions=()
  
  for ((i=9; i>=1; i--)); do
    python_version="3.$i"
    if [[ $requires_python == *"$python_version"* || $requires_python == *">=$python_version"* ]]; then
      compatible_versions+=("$python_version")
    fi
  done
  
  if [ ${#compatible_versions[@]} -eq 0 ]; then
    echo "$package = Not Compatible \# ($requires_python)"
  else
    echo "$package = \"^$version\" \# ($compatible_versions)"
  fi
}

# Loop through each package and check python version compatibility
for package in "${packages[@]}"
do
  echo -n "Checking compatibility for $package: "
  check_compatibility $package
done