-- Client-side command; separate runtime from MoonLoader Lua.
addCommandHandler('kitclient', function()
    outputChatBox('Hello from the MTA client!', 100, 180, 255)
end)
