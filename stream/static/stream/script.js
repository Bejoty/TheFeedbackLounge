var hour_start = 11;
var hour_end = 21;
var stream_length = hour_end - hour_start;

var schedule = [
    [
        ["Sunday", 12, 15, "KH1", "Kingdom Hearts"],
        ["Sunday", 18, 21, "KH1", "Kingdom Hearts"],
    ],
    [
        ["Monday", 11, 14, "KH2", "Kingdom Hearts 2"],
        ["Monday", 17, 20, "KH2", "Kingdom Hearts 2"],
    ],
    [
        ["Tuesday", 11, 14, "SSB4", "Super Smash Bros. 4"],
        ["Tuesday", 17, 20, "MK8", "Mario Kart 8"],
    ],
    [
        ["Wednesday", hour_start, hour_end, "Day Off (?)", "Possible day off"],
    ],
    [
        ["Thursday", 11, 14, "MEME", "Meme Runner"],
        ["Thursday", 17, 20, "KH2.5", "Kingdom Hearts 2.5"],
    ],
    [
        ["Friday", 12, 15, "???", "Unknown"],
        ["Friday", 18, 21, "???", "Unknown"],
    ],
    [
        ["Saturday", hour_start, hour_end, "Day Off", "Day Off"],
    ],
];

d3.select("#schedule-grid")
    .selectAll("div")
        .data(schedule)
    .enter().append("div") // month
        .style("width", "100%")
    .selectAll("div")
        .data(function(d, i) { return d; })
    .enter().append("div") // schedule
        .text(function(d) { return d[3]; })
        .style("width", function(d) { return 100 * (d[2] - d[1]) / stream_length + "%"; })
        .style("left", function(d, i) { return 100 * (d[1] - hour_start - 3 * (i % 2)) / stream_length + "%"; })
    .on("mouseover", function(d) {
        d3.select("#schedule-time").text(d[0]);
        d3.select("#schedule-info").text(d[4]);
    })
    .on("mouseout", function(d) {
        d3.select("#schedule-time").text("");
        d3.select("#schedule-info").text("");
});
