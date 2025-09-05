-- SCE Question App Launcher
on run
    set scriptPath to (path to me as string)
    set scriptFolder to do shell script "dirname " & quoted form of POSIX path of scriptPath
    
    try
        -- Run the Python script directly without showing Terminal
        do shell script "cd " & quoted form of scriptFolder & " && /usr/bin/python3 run.py > /dev/null 2>&1 &"
        
    on error errMsg
        display dialog "Error launching SCE Question App: " & errMsg buttons {"OK"} default button "OK"
    end try
end run