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

document.addEventListener('DOMContentLoaded', function() {
  const addBtn = document.getElementById('addToCartBtn');
  if (!addBtn) return;

  addBtn.addEventListener('click', function() {
    const stockCountEl = document.getElementById('stock-count');
    const stockLabelEl = document.getElementById('stock-label');
    const container = document.getElementById('cartAlertContainer');

    let count = parseInt(stockCountEl.textContent) || 0;
    if (count <= 0) return;

    // Decrementar visualmente el stock (1 -> 0)
    count = Math.max(0, count - 1);
    stockCountEl.textContent = count;
    if (count === 0) {
      stockLabelEl.textContent = 'Sin stock';
      stockLabelEl.className = 'badge bg-danger ms-2';
      addBtn.disabled = true;
      addBtn.classList.remove('btn-primary');
      addBtn.classList.add('btn-secondary');
      addBtn.textContent = 'Añadido';
    } else {
      addBtn.textContent = 'Añadido';
    }

    // Fecha/hora actual para el mensaje (cliente)
    const now = new Date();
    const dd = String(now.getDate()).padStart(2, '0');
    const mm = String(now.getMonth() + 1).padStart(2, '0');
    const yyyy = now.getFullYear();
    const hh = String(now.getHours()).padStart(2, '0');
    const mins = String(now.getMinutes()).padStart(2, '0');

    const msg = `Bici agregada el ${dd}/${mm}/${yyyy} a las ${hh}:${mins}`;

    container.innerHTML = `
      <div class="alert alert-success alert-dismissible fade show" role="alert">
        ${msg}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
    `;
  });
});