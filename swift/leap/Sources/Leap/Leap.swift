//Solution goes in Sources
struct Year {
    let calendarYear: Int
    var isLeapYear: Bool {
        return calendarYear % 400 == 0 ||
            (!(calendarYear % 100 == 0) && calendarYear % 4 == 0)
    }
}
