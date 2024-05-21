$cluster_Web = 'tandaterm'
$UsrName = 'dev2300201'
$new_usr = "1moredev\dev2300201" 
#$new_pwd = ConvertTo-SecureString -AsPlainText 'Lva85#pjcCU4' -Force
#$new_pwd = ConvertTo-SecureString -AsPlainText 'Jgv49+sgcNYp' -Force

$Cred = New-Object System.Management.Automation.PSCredential $new_usr, (ConvertTo-SecureString -AsPlainText 'Jgv49+sgcNYp' -Force)
$NS = New-PSSession -ComputerName $cluster_Web -Credential $Cred # новая сессию подключения	
Write-Host
if( $NS ){
    $QR = Invoke-Command -Session $NS -ScriptBlock {$env:USERPROFILE}
    Write-Host("`t", $QR )
    Remove-PSSession -Session $NS
}
$NS = $null