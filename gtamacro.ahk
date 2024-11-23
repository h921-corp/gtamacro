#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Create a transparent GUI window for the text
Gui, +AlwaysOnTop +ToolWindow -Caption +E0x20  ; No title bar, no taskbar icon, click-through enabled
Gui, Margin, 10, 10  ; Set margin for padding
Gui, Color, 0x000000  ; Set background color (required before making it transparent)
; Add text to the GUI
Gui, Font, s20  ; Set font size (s20 = size 20)
Gui, Add, Text, cWhite, Hello World`nBST: b`nCall PV: `;`nCall Opressor: ]`nNew Session: [  ; White text

; make transparent
Gui, +LastFound
WinSet, ExStyle, +0x20  ; Make the GUI click-through by enabling WS_EX_LAYERED
WinSet, Transparent, 255  ; Set the transparency to fully invisible (only text remains visible)

; Position the GUI at the top-right of the screen
Gui, Show, x0 y60 NoActivate  ; Position the GUI at the top-left (x0, y0)

Return  ; End of script execution


; Hotkey to listen for "b"
b::
{
	Send {SC032}
    Sleep, 5
    Send {Enter}
    Sleep, 5
    Send {Down}
    Sleep, 5
    Send, {Down}
    Sleep, 5
    Send, {Down}
    Sleep, 5
    Send, {Down}
    Sleep, 5
    Send, {Enter}
    Sleep, 5
    Send, {Down}
    Sleep, 5
    Send, {Enter}
    Return ; End of hotkey function
}

`;::
{
	Send {SC032}
    Sleep, 5
    Send {Down}
    Sleep, 5
    Send {Down}
    Sleep, 5
    Send {Enter}
    Sleep, 5
    Send {Enter}
    Sleep, 5
    Send {Esc}
    Sleep, 5
    Send {Esc}
    Return ; End of hotkey
}
]::
{
    Send {SC032}
    Sleep, 5
    Send {Down}
    Sleep, 5
    Send {Down}
    Sleep, 5
    Send {Down}
    Sleep, 5
    Send {Enter}
    Sleep, 5
    Send {Down}
    Sleep, 5
    Send {Down}
    Sleep, 5
    Send {Down}
    Sleep, 5
    Send {Enter}
    Sleep, 5
    Send {Down}
    Sleep, 5
    Send {Down}
    Sleep, 5
    Send {Enter}
    Sleep, 5
    Send {Esc}
    Sleep, 5
    Send {Esc}
    Return ;end of hotkey again
}
[::
{
    Send {Esc}
    Sleep, 1000
    Send {Right}
    Sleep, 500
    Send {Enter}
    Sleep, 500
    Send {Up}
    Sleep, 5
    Send {Up}
    Sleep, 5
    Send {Up}
    Sleep, 5
    Send {Up}
    Sleep, 5
    Return ;dont forget to add enter here
}
