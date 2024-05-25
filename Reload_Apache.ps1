$cluster_Web = 'web4test1c'
$pub_usr = 'webpub1c'
$pub_pwd = ConvertTo-SecureString -AsPlainText 'Gkt78j4eUSi' -Force
$Cred = New-Object System.Management.Automation.PSCredential $pub_usr,$pub_pwd
$ssh_session  = New-SSHSession  -ComputerName $cluster_Web -Credential $Cred 
Invoke-SSHCommand -SSHSession $ssh_session -Command "sudo /etc/init.d/apache2 reload"
$null =  $ssh_session | Remove-SSHSession