script_name('MoonLoader Starter')
script_author('Development Reference kit')
script_version('1.0')

-- Place in moonloader/. Requires MoonLoader and working SA-MP bindings.
function main()
    repeat wait(100) until isSampAvailable()
    sampRegisterChatCommand('kithello', function()
        sampAddChatMessage('[Reference kit] Hello from MoonLoader!', -1)
    end)
    wait(-1)
end
