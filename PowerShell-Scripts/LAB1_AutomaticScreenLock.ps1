# Script : LAB1_AutomaticScreenLock.ps1
# Purpose: The user needs to enter a value in seconds which will be the timeout to lock the computer's screen due to inactivity 
# Why    : As a measure of security.

####################IMPORTANT NOTES###########################
# Too see more detailed information enter the switch -verbose
##############################################################

[CmdletBinding()]
param (
    [Parameter(Mandatory=-$True)]
    [string]$screenTimeout
)

Write-Verbose "Starting InactivityTimeoutSetUp.ps1 script..."

$path = "Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
$name = 'InactivityTimeoutSecs'

try 
{ 
     
     Write-Verbose "New inactivity timeout value: $screenTimout"
     Set-ItemProperty -Path $path -Name $name -Value $screenTimeout 
     Write-Verbose "New inactivity timeout value updated"
        
} 
catch { 
   
     Write-Output $_.Exception.Message 
}

Write-Verbose "Ending InactivityTimeoutSetUp.ps1 script..." 
