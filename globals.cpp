using namespace std; 

#include "globals.h"

// global variables
bool   bStopNow = false;      // when set, the MUD shuts down
time_t tLastMessage = 0;      // time we last sent a periodic message 
int    iControl = NO_SOCKET;  // socket for accepting new connections 

// list of all connected players
tPlayerList playerlist;   
// map of all rooms
tRoomMap roommap;
// map of known commands (eg. look, quit, north etc.)
map<string, tHandler> commandmap;
// map of things to do for various connection states
map<tConnectionStates, tHandler> statemap;
// messages
map<string, string, ciLess> messagemap;
// directions
set<string, ciLess> directionset;
// bad player names
set<string, ciLess> badnameset;
// blocked IP addresses
set<string> blockedIP;
