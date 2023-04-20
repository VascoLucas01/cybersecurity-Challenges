# Script : Lab4_SMBv1.ps1
# Purpose: Automate the process of disable SMBv1
# Why    : As a measure of security.

# ./LAB4_SMBv1.ps1

$path     = "Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters"
$name     = "SMB1"
$property = Get-ItemProperty -Path $path -Name $name -ErrorAction SilentlyContinue

Set-ItemProperty -Path $path -Name $name -Value 0
