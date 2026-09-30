// Windows x86 DLL starter; rename compiled DLL to .asi.
// ASI loader required. This intentionally contains no version-specific hooks.
#include <windows.h>

extern "C" __declspec(dllexport) int ReferenceKitVersion()
{
    return 1;
}

BOOL WINAPI DllMain(HINSTANCE module, DWORD reason, LPVOID)
{
    if (reason == DLL_PROCESS_ATTACH)
        DisableThreadLibraryCalls(module);
    return TRUE;
}
