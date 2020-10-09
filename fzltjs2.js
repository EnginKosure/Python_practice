function reverseIt(s) {
  let rev = "";
  for (i in s) {
    rev = s[i] + rev;
  }
  console.log(rev);
  return rev;
}
reverseIt("fazilet");

function reverseIt2(s) {
  let rev = "";
  for (i of s) {
    rev = i + rev;
  }
  console.log(rev);
  return rev;
}
reverseIt2("fazilet");
