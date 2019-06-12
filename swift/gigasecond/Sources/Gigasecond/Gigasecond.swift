//Solution goes in Sources
import Foundation

class Gigasecond {
    let from: Date
    let description: String
    
    init?(from f: String){
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ss"
        dateFormatter.timeZone = TimeZone(secondsFromGMT: 0)
        
        self.from = dateFormatter.date(from: f) ?? Date()
        
        self.description =
            dateFormatter.string(
                from: Date.init(
                    timeInterval: 1000000000,
                    since: self.from
                )
            )
    }
}

