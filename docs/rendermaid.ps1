# PowerShell script to render Mermaid diagrams as image formats for topics; assumes Windows.
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
$destinationDir = "source/images"
# ---------------------------------------------------
# Check that destination directory exists.
# ---------------------------------------------------
if (!(Test-Path -Path $destinationDir)) {
    New-Item -ItemType Directory -Path $destinationDir | Out-Null
}
# ---------------------------------------------------
# Iterate .mmd files in the source directory and generate output.
# ---------------------------------------------------
$mmdFiles = Get-ChildItem -Path $sourceDir -Filter *.mmd
foreach ($file in $mmdFiles) {
    # Build output path with file extension
    $outputFile = Join-Path $destinationDir ($file.BaseName + ".svg")
    # Run mmdc for SVG output
    mmdc -i $file.FullName -o $outputFile
    Write-Output "Output file location and name: $outputFile"
}
# ---------------------------------------------------
# Show final image destination.
# ---------------------------------------------------
$finalMessage = "Images created in $pwd\$destinationDir."
Write-Output $finalMessage