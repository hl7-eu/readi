@ECHO OFF
:: Regenerates in output\ only the narrative pages from input\pagecontent,
:: reusing the temp\pages folder of the last full IG Publisher run.
::   runJekyll.bat                      all pages in input\pagecontent
::   runJekyll.bat usdm2fhir-mapping    only that page (name without extension)
setlocal

SET "lang=en"
SET "jekyll_out=temp\jekyll-out"

IF NOT EXIST temp\pages\_config.yml (
    echo temp\pages not found: run a full IG Publisher build first.
    EXIT /B 1
)

IF "%~1"=="" (SET "pages=*") ELSE (SET "pages=%~n1")

:: the default language template reads the page from _includes\<lang>
copy input\pagecontent\%pages%.md temp\pages\_includes\ /Y >NUL
copy input\pagecontent\%pages%.md temp\pages\_includes\%lang%\ /Y >NUL

echo Running Jekyll build...
call jekyll build -s temp\pages -d %jekyll_out%
IF ERRORLEVEL 1 EXIT /B 1

:: copy the rebuilt pages, keeping the release header written by the IG Publisher
powershell -NoProfile -Command ^
  "$re = '(?s)<!--ReleaseHeader-->.*?<!--EndReleaseHeader-->';" ^
  "Get-ChildItem 'input\pagecontent\%pages%.md' | ForEach-Object {" ^
  "  $src = Join-Path '%jekyll_out%\%lang%' ($_.BaseName + '.html');" ^
  "  $dst = Join-Path 'output\%lang%' ($_.BaseName + '.html');" ^
  "  if (-not (Test-Path $src)) { Write-Host ('Skipped (not built): ' + $_.BaseName); return }" ^
  "  $html = [IO.File]::ReadAllText((Resolve-Path $src));" ^
  "  if (Test-Path $dst) {" ^
  "    $m = [regex]::Match([IO.File]::ReadAllText((Resolve-Path $dst)), $re);" ^
  "    if ($m.Success) { $html = [regex]::Replace($html, $re, { param($x) $m.Value }) }" ^
  "  }" ^
  "  [IO.File]::WriteAllText((Join-Path (Get-Location) $dst), $html);" ^
  "  Write-Host ('Updated ' + $dst)" ^
  "}"

endlocal
