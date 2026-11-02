$apturetie = Get-Service |
    Where-Object { $_.Status -eq "Stopped" } |
    Sort-Object Name |
    Select-Object Name, Status
$apturetie | Export-CSV -Path "apturetie.csv" -NoTypeInformation -Encoding UTF8
