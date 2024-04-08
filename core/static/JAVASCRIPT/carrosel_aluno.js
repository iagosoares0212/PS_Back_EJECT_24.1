const controls_aluno = document.querySelectorAll(".control_aluno");
let currentItem_aluno = 0;
const items_aluno = document.querySelectorAll(".item_aluno");
const maxItems_aluno = items_aluno.length;

controls_aluno.forEach((control_aluno) => {
  control_aluno.addEventListener("click", (e) => {
    isLeft_aluno = e.target.classList.contains(".left_aluno");

    if (isLeft_aluno) {
      currentItem_aluno -= 1;
    } else {
      currentItem_aluno += 1;
    }

    if (currentItem_aluno >= maxItems_aluno) {
      currentItem_aluno = 0;
    }

    if (currentItem_aluno < 0) {
      currentItem_aluno = maxItems_aluno - 1;
    }

    items_aluno.forEach((item_aluno) => item_aluno.classList.remove("current_item_aluno"));

    items_aluno[currentItem_aluno].scrollIntoView({
      behavior: "smooth",
      inline: "center"
    });

    items_aluno[currentItem_aluno].classList.add(".item_aluno");
  });
});
