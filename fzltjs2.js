// Unlike for...of, you get the letter index instead of the letter. It performs pretty badly.
function reverseIt(s) {
  let rev = "";
  for (i in s) {
    rev = s[i] + rev;
  }
  console.log(rev);
  return rev;
}
reverseIt("fazilet"); //telizaf

/*for...of is the new ES6 for iterator. Supported by most modern browsers. It is visually more appealing and is less prone to typing mistakes. If you are going for this one in a production application, you should be probably using a transpiler like Babel.*/
function reverseIt2(s) {
  let rev = "";
  for (i of s) {
    rev = i + rev;
  }
  console.log(rev);
  return rev;
}
reverseIt2("fazilet"); //telizaf
