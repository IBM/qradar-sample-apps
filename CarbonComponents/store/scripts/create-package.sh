#!bin/bash
start=`date +%s`

printf "\nBuilding React application...\n\n"
cd react-app && yarn build
cd ..

printf "\nChecking if package app.zip already exists...\n"
ZIP_PATH=app.zip
if [ -f "$ZIP_PATH" ]; then
    printf "Removing existing package...\n"
    rm -rf app.zip
    printf "Old package removed.\n"
else
    echo "No existing package found."
fi

printf "\nPackaging...\n\n"
zip app.zip -r app container manifest.json

end=`date +%s`
runtime=$((end-start))

printf "\nDone in $runtime seconds!\n"
