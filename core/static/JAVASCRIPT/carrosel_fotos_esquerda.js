const controls_esquerda = document.querySelectorAll(".control_esquerda");
let currentItem_esquerda = 0;
const items_esquerda = document.querySelectorAll(".item_esquerda");
const maxItems_esquerda = items_esquerda.length;

controls_esquerda.forEach((control_esquerda) => {
  control_esquerda.addEventListener("click", (e) => {
    isLeft_esquerda = e.target.classList.contains("arrow_left_esquerda");

    if (isLeft_esquerda) {
      currentItem_esquerda -= 1;
    } else {
      currentItem_esquerda += 1;
    }

    if (currentItem_esquerda >= maxItems_esquerda) {
      currentItem_esquerda = 0;
    }

    if (currentItem_esquerda < 0) {
      currentItem_esquerda = maxItems_esquerda - 1;
    }

    items_esquerda.forEach((item_esquerda) => item_esquerda.classList.remove("current_item_esquerda"));

    items_esquerda[currentItem_esquerda].scrollIntoView({
      behavior: "smooth",
      inline: "center"
    });

    items_esquerda[currentItem_esquerda].classList.add("current_item_esquerda");
  });
});
