-- Server-side command. No client-triggered privileged events.
addCommandHandler('kithello', function(player)
    if isElement(player) and getElementType(player) == 'player' then
        outputChatBox('Hello from the MTA server!', player, 100, 220, 140)
    else
        outputServerLog('Reference kit server command executed from console.')
    end
end)
