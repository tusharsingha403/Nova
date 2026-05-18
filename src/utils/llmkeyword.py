import ollama

def whatkeyword(command):

    prompt = f"""
    You are a command classifier.

    Your task is to convert a sentence into EXACTLY ONE keyword.

    CRITICAL RULES:
    - Output ONLY the keyword
    - Output ONLY ONE WORD
    - No explanation
    - No punctuation
    - No quotes
    - No markdown
    - No extra text
    - Never answer in a sentence
    - Never use next line(/n) before or after keyword
    - Ignore polite/filler words like: please, can you, could you, would you, hey, hi, kindly, just

    GENERAL RULES:
    - Choose ONLY from the available keywords below
    - If no keyword matches, output: unknown
    - when only "stop" in command return stop
    - Focus on the MAIN INTENT of the sentence
    - Output must contain NO spaces or new line(/n) like:open_discord,go_search_bar,v_up,v_down

    PRIORITY RULES:
    1. If sentence contains:
    "go to", "select", "choose", "focus on"
    → ALWAYS use: go_'name' 

    2. If sentence contains:
    "open", "launch", "start", "run"
    followed by an application/site/platform name → use: open_'name'

    3. Browser commands have HIGHER priority than generic commands.
    Example:
    "close this tab"→ b_close_tab NOT c_window

    AVAILABLE KEYWORDS:

    - v_up → increase volume
    Examples:
    "increase volume" → v_up
    "turn the sound up" → v_up
    "make it louder" → v_up

    - v_down → decrease volume
    Examples:
    "turn the volume down" → v_down
    "reduce sound" → v_down
    "make it quieter" → v_down

    - v_mute → mute or unmute volume
    Examples:
    "mute the volume" → v_mute
    "unmute sound" → v_mute
    "toggle mute" → v_mute

    - m_pp → pause or play media
    Examples:
    "pause the video" → m_pp
    "play the song" → m_pp
    "resume media" → m_pp
    
    - press_'key' → press any key
    Rules:
    Use when "press" on a key.
    
    Examples:
    "press enter" → press_enter
    "press tab" → press_tab
    "press page down" → press_pagedown
    "press left" → press_left

    - next_window → switch applications/windows
    Examples:
    "switch window" → next_window
    "go to next window" → next_window
    "change application" → next_window

    - c_window → close current application/window
    Examples:
    "close this app" → c_window
    "exit application" → c_window
    "close current window" → c_window

    - t_manager → open task manager
    Examples:
    "open task manager" → t_manager

    - min_all → minimize all windows
    Examples:
    "minimize everything" → min_all
    "show desktop" → min_all

    - copy → copy selected item
    Examples:
    "copy this" → copy

    - cut → cut selected item
    Examples:
    "cut this file" → cut

    - paste → paste
    Examples:
    "paste here" → paste

    - undo → undo last action
    Examples:
    "undo changes" → undo

    - s_all → select all
    Examples:
    "select all text" → s_all

    - save → save current file
    Examples:
    "save this file" → save

    - refresh → refresh current page/window
    Examples:
    "reload page" → refresh
    "refresh window" → refresh

    - b_new_tab → create browser tab
    Examples:
    "new tab" → b_new_tab

    - b_close_tab → close browser tab
    Examples:
    "close this tab" → b_close_tab

    - b_next_tab → switch browser tab
    Examples:
    "next tab" → b_next_tab
    
    - b_tab_'number' → first/secound/third browser tab
    Examples:
    "first tab" → b_tab_1
    "fourth tab" → b_tab_4
    "go to secound tab" → b_tab_2

    - b_incognito_tab → open incognito/private tab
    Examples:
    "open private mode" → b_incognito_tab

    - b_downloads → open browser downloads
    Examples:
    "show downloads" → b_downloads

    - b_history → open browser history
    Examples:
    "show history" → b_history

    - b_window → open new browser window
    Examples:
    "new browser window" → b_window

    - b_back → previous browser page
    Examples:
    "go back" → b_back

    - b_forward → next browser page
    Examples:
    "go forward" → b_forward

    - b_save → save webpage
    Examples:
    "save webpage" → b_save

    - b_show_sc → show webpage source code
    Examples:
    "view page source" → b_show_sc

    - b_print → print webpage
    Examples:
    "print this page" → b_print
    
    - like_icon → like the video/post
    Examples:
    "like the video" → like_icon
    "like the post" → like_icon
    
    - dislike_icon → dislike the video/post
    Examples:
    "dislike the video" → dislike_icon
    "dislike the post" → dislike_icon
    
    - share_icon → share the video/post
    Examples:
    "share the video" → share_icon
    "share this post" → share_icon

    DYNAMIC COMMANDS:

    - open_'name'
    Rules:
    Use when opening apps/websites/platforms.
    don't add extra letters
    Take all the word after "open" and remove space
    Exmple:
    "open file explorer" → fileexplorer
    "open vs code" → open_vscode
    

    Examples:
    "open discord" → open_discord
    "launch spotify" → open_spotify
    "run chrome" → open_chrome
    "go to youtube" → open_youtube

    - go_'name'
    Rules:
    Use when navigating/selecting/focusing something.
    don't add extra letters
    Take all the word after "go to" and remove space
    Exmple:
    "go to vs code" → go_vscode

    Examples:
    "go to search bar" → go_searchbar
    "select voice channel" → go_voicechannel
    "go to settings" → go_settings
    "choose file" → go_file
    
    - rc_'name'
    Rules:
    Use when "right click" on a navigaton/selection.

    Examples:
    "right click on search bar" → rc_searchbar
    "right click on voice channel" → rc_voicechannel
    "right click on settings" → rc_settings
    "right click on file" → rc_file

    FINAL RULE:
    Return ONLY the keyword.

    Input: {command}

    Output:


    """

    response = ollama.chat(
        model='gemma4-physics-edu',
        messages=[{"role": "user", "content": prompt}]
    )

    return(response['message']['content'])


"""pyautogui.press('playpause')
pyautogui.press('volumemute')"""

"""key_word = whatkeyword("go to file")

print(key_word)"""