function reverseIt(s) {
  let rev = "";
  for (i in s) {
    rev = s[i] + rev;
  }
  console.log(rev);
  return rev;
}
reverseIt("fazilet");
