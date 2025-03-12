# PowerShell Script to Set Up Flask Cybersecurity Project

# Define project structure
$folders = @(
    "cyberpunk_security/static/css",
    "cyberpunk_security/static/js",
    "cyberpunk_security/templates"
)

# Create directories
foreach ($folder in $folders) {
    if (-Not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder -Force
    }
}

# Create necessary files
$files = @(
    "cyberpunk_security/main.py",
    "cyberpunk_security/templates/index.html",
    "cyberpunk_security/static/css/cyberpunk-theme.css",
    "cyberpunk_security/static/js/app.js",
    "cyberpunk_security/requirements.txt"
)

foreach ($file in $files) {
    if (-Not (Test-Path $file)) {
        New-Item -ItemType File -Path $file -Force
    }
}

# Add Flask dependency
"flask" | Out-File -FilePath "cyberpunk_security/requirements.txt" -Encoding utf8

Write-Host "Project structure set up successfully!" -ForegroundColor Green
