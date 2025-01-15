# Winget Script to Install Common Applications
# Save this file as InstallApps.ps1 and run it using PowerShell

# List of applications to install
$apps = @(
    "vmware.workstationpro"
    # "7zip.7zip",
    # "VNGCorp.Zalo",
    # "Microsoft.VisualStudioCode",
    # "MSYS2.MSYS2",
    # "Git.Git",
    # "TeXstudio.TeXstudio",
    # "Oracle.JDK.17",
    # "Microsoft.Edge",
    # "Google.Chrome",
    # "Python.Python.3.11",
    # "AnyDeskSoftwareGmbH.AnyDesk",
    # "calibre.calibre"

)

$download_path = "C:\Downloads"

# Loop through the app list and install each one
foreach ($app in $apps) {
    Write-Host "Installing $app..."
    winget install --id $app --silent --accept-source-agreements --accept-package-agreements --location $download_path -e
    if ($?) {
        Write-Host "$app installed successfully." -ForegroundColor Green
    } else {
        Write-Host "Failed to install $app." -ForegroundColor Red
    }
}

Write-Host "All applications attempted to install." -ForegroundColor Cyan
