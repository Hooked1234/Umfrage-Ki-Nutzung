@echo off
echo Starte KI-Umfrage Server...
echo.
echo Die Umfrage oeffnet sich gleich im Browser.
echo Dieses Fenster NICHT schliessen, solange die Umfrage laeuft!
echo.
start http://localhost:8765
powershell -ExecutionPolicy Bypass -File "%~dp0serve.ps1"
