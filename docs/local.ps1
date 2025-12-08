# PowerShell Script to make local builds easier to validate

# Define parameter
param(
    [switch]$htm,
    [switch]$sin,
    [switch]$clr,
    [switch]$ver,
	[switch]$img,
	[switch]$help
)

# Define global variables
$SourceDir = "./source"
$BuildDir  = "./_build"
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

# Clean build directory
if ($clr) {
    if (Test-Path $BuildDir) {
        Write-Host "Cleaning build directory: $BuildDir"
        Remove-Item -Recurse -Force $BuildDir
    } else {
        Write-Host "No build directory found to clean."
    }
    exit
}

# Show required package versions
if ($ver) {
    Write-Host "==========================================="	
	pip show sphinx-book-theme
	Write-Host "==========================================="
	pip show myst-parser
	Write-Host "==========================================="
	sphinx-build --version
	Write-Host "==========================================="
	exit
}

if ($img) {
	& $ImageScript
	exit
}

# Show usage
if ($help) {
clear
Write-Host "==========================================="
Write-Host "  Usage: .\local.ps1 -<param>"
Write-Host "==========================================="	
Write-Host "   -htm    # Build and open HTML Documentation"
Write-Host "   -sin    # Build and open single HTML output"
Write-Host "   -img    # Build Mermaid images"
Write-Host "   -clr    # Clean build directory"
Write-Host "   -ver    # Show Sphinx version"
Write-Host "   -help   # Show this help"
Write-Host "==========================================="
exit
}

# If no option was provided, show usage
.\local.ps1 -help

