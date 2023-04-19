


secedit /export /cfg C:\secpol\securityconfig.cfg
#$content = Get-Content -Path "C:\secpol\securityconfig.cfg" | ForEach-Object {$_ -replace "PasswordComplexity = 0", "PasswordComplexity = 1"}
(gc "C:\secpol\securityconfig.cfg").Replace("PasswordComplexity = 0", "PasswordComplexity = 1") | Out-File "C:\secpol\securityconfig.cfg"
secedit /configure /db "C:\windows\security\local.sdb" /cfg "C:\secpol\securityconfig.cfg" /areas SECURITYPOLICY 
rm -force "C:\secpol\securityconfig.cfg" 


