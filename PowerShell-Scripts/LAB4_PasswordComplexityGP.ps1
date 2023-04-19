

# export security policy settings from a local or remote machine to a security configuration file (.cfg)
secedit /export /cfg C:\secpol\securityconfig.cfg

# reads the contents of the "C:\secpol\securityconfig.cfg" file, 
# replaces the string "PasswordComplexity = 0" with "PasswordComplexity = 1"
# writes the updated contents back to the same file.
(gc "C:\secpol\securityconfig.cfg").Replace("PasswordComplexity = 0", "PasswordComplexity = 1") | Out-File "C:\secpol\securityconfig.cfg"


# configure the local security policy database with the updated security settings stored in the specified configuration file
secedit /configure /db "C:\windows\security\local.sdb" /cfg "C:\secpol\securityconfig.cfg" /areas SECURITYPOLICY 

# remove the exported configuration file
rm -force "C:\secpol\securityconfig.cfg" 


