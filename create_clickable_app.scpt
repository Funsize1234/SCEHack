-- AppleScript to create a clickable app for SCE Question
-- This script creates an AppleScript application that can be double-clicked

tell application "Script Editor"
    set appScript to "-- SCE Question App Launcher
on run
    set scriptPath to (path to me as string)
    set scriptFolder to do shell script \"dirname \" & quoted form of POSIX path of scriptPath
    
    tell application \"Terminal\"
        activate
        do script \"cd \" & quoted form of scriptFolder & \" && python run.py\"
    end tell
end run"
    
    set newDoc to make new document with properties {text:appScript}
    save newDoc in file ((path to desktop as string) & \"SCE Question.app\") as «class scpt»
    close newDoc
end tell
