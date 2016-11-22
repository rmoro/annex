#include <stdio.h>
#include <stdint.h>
#include <sys/time.h>
#include <ApplicationServices/ApplicationServices.h> /* ApplicationServices.framework needed */

char *logFileName = "./keystroke.log";
FILE *logFile = NULL;
int counter = 0;

static uint64_t prev_time;

CGEventRef myCGEventCallback (CGEventTapProxy, CGEventType, CGEventRef, void *);

int main (int argc, const char * argv[]) {
  prev_time = clock();
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
  
  CFRunLoopRun();
  return 0;
}

uint64_t current_timestamp() {
  struct timeval te;
  gettimeofday(&te, NULL);
  uint64_t milliseconds = te.tv_sec*1000LL + te.tv_usec/1000;
  return milliseconds;
}

CGEventRef myCGEventCallback (CGEventTapProxy proxy, CGEventType type, CGEventRef event, void *refcon) {
  if ((type != kCGEventKeyDown) && (type != kCGEventFlagsChanged)) {
    return event;
  }
  
  counter++;
  CGKeyCode keyCode = (CGKeyCode) CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode);
  
  uint64_t curr_time = current_timestamp();
  uint64_t delta_ms = curr_time - prev_time;
  prev_time = curr_time;

  if (logFile) {
    fprintf(logFile, "%llu, %hu\n", delta_ms, keyCode);
    if (counter % 1 == 0) fflush(logFile);
  } else {
    printf("logfile not open, missed event: %llu, %hu\n", delta_ms, keyCode);
  }
  return event;
}
