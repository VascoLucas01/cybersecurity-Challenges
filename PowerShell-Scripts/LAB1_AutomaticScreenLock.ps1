# Script : LAB1_AutomaticScreenLock.ps1
# Purpose: The user needs to enter a value in seconds which will be the timeout to lock the computer's screen due to inactivity 
# Why    : As a measure of security.

#####################IMPORTANT NOTES############################
# 1. Too see more detailed information enter the switch -verbose
# 2. Restart the machine so that the policy take effect
################################################################

[CmdletBinding()]
param (
    [Parameter(Mandatory=-$True)]
    [string]$screenTimeout
)

Write-Verbose "Starting LAB1_AutomaticScreenLock.ps1 script..."

$path     = "Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
$name     = 'InactivityTimeoutSecs'
$property = Get-ItemProperty -Path $path -Name $name -ErrorAction SilentlyContinue

Write-Verbose "New inactivity timeout value entered by the user: $screenTimout"
try 
{ 
     if ($property -ne $null){
        Write-Verbose "The registry entry alrealdy exists"
        Set-ItemProperty -Path $path -Name $name -Value $screenTimeout 
        Write-Verbose "New inactivity timeout value updated"
     }
     else{
        Write-Verbose "The registry entry does not exists"
        New-ItemProperty -Path $path -Name $name -Value $screenTimeout -PropertyType DWord
        Write-Verbose "Registry entry created with a timeout value of $screenTimeout"
        
     }
        
} 
catch { 
   
     Write-Output $_.Exception.Message 
}

Write-Verbose "Ending LAB1_AutomaticScreenLock.ps1 script..." 
