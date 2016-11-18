#include <stdio.h>
#include <time.h>
#include <ApplicationServices/ApplicationServices.h> /* ApplicationServices.framework needed */

char *logFileName = "./keystroke.log";
FILE *logFile = NULL;
int counter = 0;

struct timespec prev_time;

char* keyCodeToReadableString (CGKeyCode);
CGEventRef myCGEventCallback (CGEventTapProxy, CGEventType, CGEventRef, void *);

int main (int argc, const char * argv[]) {
  CGEventFlags oldFlags = CGEventSourceFlagsState(kCGEventSourceStateCombinedSessionState);

  CGEventMask eventMask = (CGEventMaskBit(kCGEventKeyDown) | CGEventMaskBit(kCGEventFlagsChanged));
  CFMachPortRef eventTap = CGEventTapCreate(kCGSessionEventTap, kCGHeadInsertEventTap, 0, eventMask, myCGEventCallback, &oldFlags);
  
  if (!eventTap) {
    fprintf(stderr, "failed to create event tap\nyou need to enable \"Enable access for assitive devices\" in Universal Access preference panel.");
    exit(1);
  }
  
  CFRunLoopSourceRef runLoopSource = CFMachPortCreateRunLoopSource(kCFAllocatorDefault, eventTap, 0);
  CFRunLoopAddSource(CFRunLoopGetCurrent(), runLoopSource, kCFRunLoopCommonModes);
  CGEventTapEnable(eventTap, true);

  logFile = fopen(logFileName, "a");
  
  clock_gettime(CLOCK_MONOTONIC_RAW, &prev_time);
  CFRunLoopRun();
  return 0;
}


CGEventRef myCGEventCallback (CGEventTapProxy proxy, CGEventType type, CGEventRef event, void *refcon) {
  if ((type != kCGEventKeyDown) && (type != kCGEventFlagsChanged)) {
    return event;
  }
  
  counter++;
  CGKeyCode keyCode = (CGKeyCode) CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode);
  if (logFile) {
    struct timespec curr_time;
    clock_gettime(CLOCK_MONOTONIC_RAW, &curr_time);

    uint64_t delta_us = (curr_time.tv_sec - prev_time.tv_sec) * 1000000 + (curr_time.tv_nsec - prev_time.tv_nsec) / 1000;
    uint64_t delta_ms = delta_us / 1000;
    prev_time = curr_time;
    fprintf(logFile, "%llu, %hu\n", delta_ms, keyCode);
    
    if (counter % 1 == 0) fflush(logFile);
  }
  return event;
}
