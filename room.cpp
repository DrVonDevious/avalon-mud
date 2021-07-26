#include <stdexcept>

using namespace std; 

#include "utils.h"
#include "room.h"
#include "globals.h"

tRoom * FindRoom (const int & vnum)
{
  tRoomMapIterator roomiter = roommap.find (vnum);
  
  if (roomiter == roommap.end ())
    throw runtime_error (MAKE_STRING ("Room number " << vnum << " does not exist."));

  return roomiter->second;
}
