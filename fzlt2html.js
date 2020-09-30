//Change the colors
// Change The Colors!

const colors = ["red", "blue", "gray", "green", "purple"];

const randomColorButton = document.querySelector("#randomColorButton");
const addColorButton = document.querySelector("#setColorButton");

addColorButton.addEventListener("click", addColor);
randomColorButton.addEventListener("click", changeColors);
// randomColorButton.addEventListener("click", () => changeColors());
// randomColorButton.addEventListener("click", function () {
//   changeColors();
// });

// 1) Arrayden rastgele element seçmek
function changeColors() {
  const randomIndex = Math.floor(Math.random() * colors.length);

  document.querySelector("#colorName").textContent = colors[randomIndex];
  document.querySelector("body").style.backgroundColor = colors[randomIndex];
}

// 2) Kullanıcının girdiği string'i renk listesine eklemek ve arkaplanı o renk ile güncellemek
function addColor() {
  console.log("Add color..");
  const userInput=document.querySelector('.colorInput');
  document.querySelector('body').style.backgroundColor=userInput.value;
  if(colors.indexOf(userInput.value)==-1){
    colors.push(userInput.value);
  }
  else{
      alert('Already has this color!')
  }
  userInput.value='';
  userInput.focus();
}
