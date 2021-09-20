function doUpdate() {
    var days = new Array(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31);
    var f = document.forms["converter"].elements;
    var month = parseInt(f["month"].options[f["month"].selectedIndex].value);
    var day = parseInt(f["day"].value);
    var year = parseInt(f["year"].value);
    var time = parseInt(f["time"].value);
    var zone = parseInt(f["zone"].options[f["zone"].selectedIndex].value);

    // calc julian date
    if (isLeapYear(year)) days[1] += 1;
    var jDate = 0;
    for (var i = 0; i < month; i++) jDate += days[i];
    jDate += day;
    if (jDate < 100) jDate = "0" + jDate;
    if (jDate < 10) jDate = "0" + jDate;

    // calc gmt
    var gmtTime = time + zone * 100;
    if (gmtTime >= 2400) gmtTime -= 2400;
    if (gmtTime < 1000) gmtTime = "0" + gmtTime;
    if (gmtTime < 100) gmtTime = "0" + gmtTime;
    if (gmtTime < 10) gmtTime = "0" + gmtTime;

    // update form
    f["julian"].value = jDate;
    f["gmttime"].value = gmtTime;
}

function isLeapYear(y) {
    if (y % 4 == 0) {
        if (y % 100 == 0) return (y % 400 == 0) ? true : false;
        return true;
    }
    return false;
}

function init() {
    var f = document.forms["converter"].elements;

    today = new Date();
    f["month"].value = today.getMonth();
    f["day"].value = today.getDate();
    if (today.getFullYear()) {
        f["year"].value = today.getFullYear();
    }

    var h = today.getHours().toString();
    if (parseInt(h) < 10) h = "0" + h;
    var m = today.getMinutes().toString();
    if (parseInt(m) < 10) m = "0" + m;
    f["time"].value = h + m;

    doUpdate();
}

