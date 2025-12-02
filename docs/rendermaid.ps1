# Script to render all Mermaid diagrams as image formats for topic
# ---------------------------------------------------
# Install command line tool. One time only.
# ---------------------------------------------------
# npm install -g @mermaid-js/mermaid-cli
# ---------------------------------------------------
# Generate .SVG and .PNG output example syntax
# ---------------------------------------------------
# mmdc -i <input file>.mmd -o <output file>.svg
# mmdc -i <input file>.mmd -o <output file>.png

# ---------------------------------------------------
# Define source and destination directories. Assume root directory.
# ---------------------------------------------------
$sourceDir = "source/_static"
$destDir   = "source/images"

# ---------------------------------------------------
# Destination directory exists
# ---------------------------------------------------
if (!(Test-Path -Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir | Out-Null
}

# ---------------------------------------------------
# Iterate .mmd files in the source directory
# ---------------------------------------------------
$mmdFiles = Get-ChildItem -Path $sourceDir -Filter *.mmd
foreach ($file in $mmdFiles) {
    # Build output path with file extension
    $outputFile = Join-Path $destDir ($file.BaseName + ".svg")
    # Run mmdc for SVG output
    mmdc -i $file.FullName -o $outputFile
    Write-Host "Output: $outputFile"
}