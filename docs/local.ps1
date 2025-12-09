# PowerShell Script to make local builds easier to validate
# Define options parameters
param(
    [switch]$htm,
    [switch]$sin,
	[switch]$img,
    [switch]$clr,
    [switch]$ver,
	[switch]$help
)
# Validate options. If wrong, show this message
if (-not ($htm -or $sin -or $clr -or $ver -or $img -or $help)) {
    Write-Host "==========================================="
    Write-Host " Missing or invalid option."
    Write-Host " Enter '.\local.ps1 -help' for usage."
    Write-Host "==========================================="
    exit 1
}
# Define global variables
$SourceDir = "./source"
$BuildDir  = "./build"
$HomeFile = "index.html"
$ImageScript = "./rendermaid.ps1"
# Build multiple-topic HTML output
if ($htm) {
    Write-Host "Building Sphinx documentation (HTML)..."
    sphinx-build -b html $SourceDir $BuildDir
    $IndexFile = Join-Path $BuildDir $HomeFile
    if (Test-Path $IndexFile) {
        Write-Host "Opening $IndexFile..."
        Start-Process $IndexFile
    } else {
        Write-Host "Build succeeded, but $IndexFile not found."
    }
    exit
}
# Build single HTML output
if ($sin) {
    Write-Host "Building Sphinx documentation (Single HTML)..."
    sphinx-build -b singlehtml $SourceDir $BuildDir
    $IndexFile = Join-Path $BuildDir $HomeFile
    if (Test-Path $IndexFile) {
        Write-Host "Opening IndexFile..."
        Start-Process $IndexFile
    } else {
        Write-Host "Build succeeded, but $IndexFile not found."
    }
    exit
}
# Call PowerShell script to render mermaid images
if ($img) {
	& $ImageScript
	exit
}
# Delete build directory
if ($clr) {
    if (Test-Path $BuildDir) {
        Write-Host "Deleting build directory: $BuildDir"
        Remove-Item -Recurse -Force $BuildDir
    } else {
        Write-Host "No build directory found to delete."
    }
    exit
}
# Show required package information and dependencies
if ($ver) {
	Write-Host "==========================================="
	pip show sphinx
    Write-Host "==========================================="	
	pip show sphinx-book-theme
	Write-Host "==========================================="
	pip show myst-parser
	Write-Host "==========================================="
	sphinx-build --version
	Write-Host "==========================================="
	exit
}
# Show usage
if ($help) {
clear
Write-Host "==========================================="
Write-Host "  Usage: .\local.ps1 <option>"
Write-Host "==========================================="	
Write-Host "   -htm    # Build and open HTML Documentation"
Write-Host "   -sin    # Build and open single HTML output"
Write-Host "   -img    # Build Mermaid images"
Write-Host "   -clr    # Clean build directory"
Write-Host "   -ver    # Show Sphinx components"
Write-Host "   -help   # Show this help"
Write-Host "==========================================="
exit
}