// Minimal open.mp server gamemode. Requires matching omp-stdlib.
#include <open.mp>

main() {}

public OnGameModeInit()
{
    SetGameModeText("Development Starter");
    AddPlayerClass(0, 1958.3783, 1343.1572, 15.3746, 270.0, 0, 0, 0, 0, 0, 0);
    return 1;
}

public OnPlayerRequestClass(playerid, classid)
{
    SetPlayerPos(playerid, 1958.3783, 1343.1572, 15.3746);
    SetPlayerCameraPos(playerid, 1958.3783, 1338.1572, 17.3746);
    SetPlayerCameraLookAt(playerid, 1958.3783, 1343.1572, 15.3746);
    return 1;
}

public OnPlayerConnect(playerid)
{
    SendClientMessage(playerid, 0xFFFFFFFF, "Development gamemode loaded. Use /hello.");
    return 1;
}

public OnPlayerCommandText(playerid, cmdtext[])
{
    if (!strcmp(cmdtext, "/hello", true))
    {
        SendClientMessage(playerid, 0xFFFFFFFF, "Hello from Pawn!");
        return 1;
    }
    return 0;
}
