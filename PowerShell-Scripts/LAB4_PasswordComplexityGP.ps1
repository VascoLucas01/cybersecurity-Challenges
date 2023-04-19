# Script : LAB4_PasswordComplexityGP.ps1
# Purpose: Automate the process of enable/disable password complexity
# Why    : As a measure of security.

# EXAMPLE: ./LAB4_PssswordComplexityGP.ps1


# enter 'y' to enable
# enter 'n' to disable
$input = Read-Host "Do you want to enable Password Complexity? (y,n)"

# export security policy settings from a local or remote machine to a security configuration file (.cfg)
secedit /export /cfg C:\secpol\securityconfig.cfg

if ($input -eq 'y'){
    # reads the contents of the "C:\secpol\securityconfig.cfg" file, 
    # replaces the string "PasswordComplexity = 0" with "PasswordComplexity = 1"
    # writes the updated contents back to the same file.
    (gc "C:\secpol\securityconfig.cfg").Replace("PasswordComplexity = 0", "PasswordComplexity = 1") | Out-File "C:\secpol\securityconfig.cfg"


    # configure the local security policy database with the updated security settings stored in the specified configuration file
    secedit /configure /db "C:\windows\security\local.sdb" /cfg "C:\secpol\securityconfig.cfg" /areas SECURITYPOLICY 
}

if ($input -eq 'n'){
    # reads the contents of the "C:\secpol\securityconfig.cfg" file, 
    # replaces the string "PasswordComplexity = 1" with "PasswordComplexity = 0"
    # writes the updated contents back to the same file.
    (gc "C:\secpol\securityconfig.cfg").Replace("PasswordComplexity = 1", "PasswordComplexity = 0") | Out-File "C:\secpol\securityconfig.cfg"


    # configure the local security policy database with the updated security settings stored in the specified configuration file
    secedit /configure /db "C:\windows\security\local.sdb" /cfg "C:\secpol\securityconfig.cfg" /areas SECURITYPOLICY 
}

# remove the exported configuration file
rm -force "C:\secpol\securityconfig.cfg" -Force -Confirm:$false

# References
# https://social.technet.microsoft.com/Forums/office/en-US/50c827f8-0b8f-4b07-a90f-582948187ccb/disabling-password-complexity-via-powershell?forum=winserverpowershell


