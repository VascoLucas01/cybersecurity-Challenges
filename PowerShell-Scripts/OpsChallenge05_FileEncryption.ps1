# Script : OpsChallenge05_FileEncryption.ps1
# Purpose: Encrypts a file
# Why    : As a measure of security.

[CmdletBinding()]
param (
    [Parameter(Mandatory=-$True)]
    [string]$filePath,
    [Parameter(Mandatory=-$True)]
    [string]$directoryPath,
    [Parameter(Mandatory=-$True)]
    [string]$newName,
    [Parameter(Mandatory=-$True)]
    [string]$password
)

try{
    $newPath= ($directoryPath,$newName) -join "\"
    
    # if the file path exists
    if(Test-Path $filePath) {
        # encrypt the file
        Compress-7Zip -Path $filePath -ArchiveFileName $newPath -Format SevenZip -Password $password -EncryptFilenames -Verbose
        # delete the file that is not encrypted
        Remove-Item $filePath
    } 
    # if the file path does not exists
    else{
        Write-Host "__Incorrect file path__"
    }
    
}
catch{
    Write-Output $_.Exception.Message
}
