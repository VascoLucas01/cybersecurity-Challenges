# Script : OpsChallenge05_FileDecryption.ps1
# Purpose: Decrypts a file
# Why    : As a measure of security.

[CmdletBinding()]
param (
    [Parameter(Mandatory=-$True)]
    [string]$filePath,
    [Parameter(Mandatory=-$True)]
    [string]$directoryPath,
    [Parameter(Mandatory=-$True)]
    [string]$password
)

try{

    # if the file path exists
    if(Test-Path $filePath) {
        # Decrypt the file
        Expand-7Zip -ArchiveFileName $filePath -Password $password -TargetPath $directoryPath -Verbose
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
