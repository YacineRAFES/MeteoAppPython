[CmdletBinding()]
param(
    [switch]$SkipTests
)

$ErrorActionPreference = "Stop"
$requiredPythonVersion = "3.14"
$projectRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $projectRoot "env\Scripts\python.exe"

if (Test-Path $venvPython) {
    $python = $venvPython
} else {
    $pythonCommand = Get-Command python -ErrorAction Stop
    $python = $pythonCommand.Source
}

Push-Location $projectRoot
try {
    $pythonVersion = & $python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
    if ($LASTEXITCODE -ne 0 -or $pythonVersion -ne $requiredPythonVersion) {
        throw "Python $requiredPythonVersion est requis pour reproduire le build GitHub Actions."
    }

    & $python -m pip install --upgrade pip
    if ($LASTEXITCODE -ne 0) {
        throw "La mise à jour de pip a échoué."
    }

    & $python -m pip install -r requirements.txt pyinstaller
    if ($LASTEXITCODE -ne 0) {
        throw "L'installation des dépendances de build a échoué."
    }

    if (-not $SkipTests) {
        & $python -m unittest discover -s tests -v
        if ($LASTEXITCODE -ne 0) {
            throw "Les tests unitaires ont échoué."
        }
    }

    & $python -m PyInstaller --noconfirm --clean --onefile --windowed --name MeteoAppPython --paths . --paths src --add-data "src/assets;assets" --add-data "src/style.qss;." src/main.py
    if ($LASTEXITCODE -ne 0) {
        throw "La création de l'exécutable a échoué."
    }
    Write-Host "Executable created: $projectRoot\dist\MeteoAppPython.exe"
} finally {
    Pop-Location
}
