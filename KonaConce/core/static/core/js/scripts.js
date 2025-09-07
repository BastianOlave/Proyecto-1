document.addEventListener("DOMContentLoaded", () => {
  const bikeCards = document.querySelectorAll(".bike-card");
  const modalTitle = document.getElementById("bikeModalLabel");
  const modalInner = document.querySelector("#modalCarousel .carousel-inner");

  document.querySelectorAll(".carousel-control-prev, .carousel-control-next")
    .forEach(btn => {
      btn.addEventListener("click", e => e.stopPropagation());
    });

  bikeCards.forEach(card => {
    card.addEventListener("click", () => {
      const title = card.getAttribute("data-title");
      const images = JSON.parse(card.getAttribute("data-images"));
      modalTitle.textContent = title;
      modalInner.innerHTML = "";
      images.forEach((img, index) => {
        const div = document.createElement("div");
        div.classList.add("carousel-item");
        if (index === 0) div.classList.add("active");
        div.innerHTML = `<img src="${img}" class="d-block w-100" alt="${title}">`;
        modalInner.appendChild(div);
      });
      const modal = new bootstrap.Modal(document.getElementById("bikeModal"));
      modal.show();
    });
  });
});