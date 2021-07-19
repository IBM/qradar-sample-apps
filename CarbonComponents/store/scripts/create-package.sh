#!bin/bash
printf "Packaging...\n\n"
zip app.zip -r app container manifest.json
printf "\nDone!\n"