#!/bin/bash
set -e

# Create data directory and requirements file if they don't exist
DATA_DIR="./data"
REQUIREMENTS_FILE="$DATA_DIR/requirements.txt"
PERSISTENCE_FILE="$DATA_DIR/persistence.json"

if [ ! -d "$DATA_DIR" ]; then
    mkdir "$DATA_DIR"
    echo "Created data directory: $DATA_DIR"
fi

if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "flask" > "$REQUIREMENTS_FILE"
    echo "pandas" >> "$REQUIREMENTS_FILE"
    echo "matplotlib" >> "$REQUIREMENTS_FILE"
    echo "Created requirements file: $REQUIREMENTS_FILE"
fi

if [ ! -f "$PERSISTENCE_FILE" ]; then
    echo '{"browser": "", "settings": {}}' > "$PERSISTENCE_FILE"
    echo "Created persistence file: $PERSISTENCE_FILE"
fi

# Install requirements
echo "Select the installation method:"
echo "1. Install requirements using pip"
echo "2. Install requirements manually"
read -p "Enter your choice (1 or 2): " choice

if [ "$choice" == "1" ]; then
    if ! pip install -r "$REQUIREMENTS_FILE"; then
        echo "Failed to install requirements using pip. Please install them manually."
        exit 1
    fi
elif [ "$choice" == "2" ]; then
    echo "Please install the following manually:"
    cat "$REQUIREMENTS_FILE"
else
    echo "Invalid choice. Exiting."
    exit 1
fi

# Scan for available browsers
available_browsers=($(compgen -c | grep -E '^(google-chrome|firefox|chromium|opera|safari)$'))
echo "Available browsers: ${available_browsers[@]}"

# Update system info to persistence file
echo "Updating system info to persistence file..."
echo "{
    \"browser\": \"${available_browsers[0]}\",
    \"settings\": {}
}" > "$PERSISTENCE_FILE"

# Run the main script
python main_script.py