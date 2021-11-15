#include <iostream>
#include <string>

#ifdef _WIN32
    #include <windows.h>
#else
    #include <unistd.h>
#endif

using namespace std;

void sleepcp(int milliseconds) // Cross-platform sleep function
{
    #ifdef _WIN32
        Sleep(milliseconds);
    #else
        usleep(milliseconds * 1000);
    #endif // _WIN32
}

void Clear()
{
    #if defined _WIN32
        system("cls");
    #elif defined (__LINUX__) || defined(__gnu_linux__) || defined(__linux__)
        system("clear");
    #elif defined (__APPLE__)
        system("clear");
    #endif
}

string repeat(string s, int n)
{
    // Copying given string to temporary string.
    string s1 = s;
 
    for (int i=1; i<n;i++)
        s += s1; // Concatenating strings
 
    return s;
}

string GenSpace(int n)
{
    string chars [4] = {"-----", "-----", "-----", " * "};
    string result = repeat(" ", (rand() % 11));
    for (int i = 0; i < n-1; i++)
    {
        result += " ----- ";
        result += repeat(" ", (rand() % 11));
        result += chars [rand() % 4];
    }
    return result;
}

int main() {

    int space = 0;
    bool reverse = false;

    while (true) {

        if (space >= 15) {
            reverse = true;
        } else if (space <= 0) {
            reverse = false;
        };

        if (reverse) {
            space--;
        } else {
            space++;
        };

        string spaces = repeat("\n", space);
        string SpacesDown = repeat("\n", (20 - space));

        string res = spaces + "\n" + "   \\ \\_____ " + GenSpace(9) + "\n" + "###[==_____>\n" + "   /_/       " + GenSpace(8) + "\n" + SpacesDown;
        
        std::cout << res;
        sleepcp(1000);
        Clear();
    }
    return 0;
}
