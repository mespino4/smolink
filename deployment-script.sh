#!/bin/bash

# Create deployment directory
mkdir deployment

# Copy Flask application files
cp -r flask-server/* deployment/

# Copy React build files
cp -r react-client/build/* deployment/

# Optionally copy other files (e.g., configuration files, requirements.txt)

# Optionally perform any additional steps or modifications

echo "Deployment directory created successfully."
