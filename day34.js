
function QuestionsMarks(str) {
    res = false;
    for (let i = 0; i < str.length; i++) {
        for (let j = i + 1; j < str.length; j++) {
            if (Number(str[i]) + Number(str[j]) === 10) {
                if (str.slice(i + 1, j).split('?').length - 1 === 3) {
                    res = true;
                    break;
                } else {
                    return false;
                }
            }
        }
    }
    console.log(res);

    return res;
}
QuestionsMarks('acc?7??sss?3rr1??????5"');