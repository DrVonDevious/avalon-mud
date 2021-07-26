#include <iostream>

using namespace std; 

#include "constants.h"
#include "globals.h"

void LoadThings ();
int InitComms ();
void MainLoop ();
void CloseComms ();
   
// called approximately every 0.5 seconds - handle things like fights here
void PeriodicUpdates () {
  //      The example below just sends a message every MESSAGE_INTERVAL seconds.
  // send new command if it is time
  if (time (NULL) > (tLastMessage + MESSAGE_INTERVAL))
    {
    SendToAll ("You hear creepy noises ...\n");
    tLastMessage = time (NULL);
    }
    
} // end of PeriodicUpdates

int main () {
  cout << "Avalon MUD " << VERSION << endl;

  LoadThings();
  
  if (InitComms()) {
    return 1;
  }

  cout << "Accepting connections from port " <<  PORT << endl;
  
  MainLoop ();    // handle player input/output

  // Server is shutting down, tell all players
  SendToAll ("\n\n** Server was shut down. **\n\n");
  
  CloseComms ();

  cout << "Server shut down." << endl;  
  return 0;
} // end of main
