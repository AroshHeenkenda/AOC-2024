
function calc_mul{

    param(
        [String]$eq
    )

    $split = $eq.Replace("mul(", "").Replace(")", "").Split(",")

    return ([int]$split[0] * [int]$split[1])

}

function part1 {

    param(
        [String]$fname
    )

    $code = Get-Content -Path $fname -Raw
    $mul = $code | Select-String -Pattern "mul\(\d{1,3},\d{1,3}\)" -AllMatches -CaseSensitive

    $sum = 0
    foreach ($m in $mul.Matches){ $sum += calc_mul($m) }

    return $sum
}

function part2 {

    param(
        [String]$fname
    )

    $code = Get-Content -Path $fname -Raw
    $filtered = ""
    $i = 0
    $enable = $true

    while ($i -lt $code.Length){

        if ($i -lt $code.Length - 7){
            if ($code.Substring($i, 7) -ceq "don't()"){ 
                $enable = $false 
                $i += 7
            }
        }

        if ($i -lt $code.Length - 4){
            if ($code.Substring($i, 4) -ceq "do()"){
                $enable = $true
                $i += 4
            } 
        }

        if ($enable){
            $filtered += $code[$i]
        }
        $i += 1
    }
    
    $sum = 0
    $mul = $filtered | Select-String -Pattern "mul\(\d{1,3},\d{1,3}\)" -AllMatches -CaseSensitive
    foreach ($m in $mul.Matches){ $sum += calc_mul($m) }

    return $sum
}



$part1 = part1("$($PSScriptRoot)\input3.txt")
Write-Host $part1

$part2 = part2("$($PSScriptRoot)\input3.txt")
Write-Host $part2