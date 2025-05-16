document.addEventListener("DOMContentLoaded", function () {
  const popularSection = document.getElementById("popular-birds");
  const otherSection = document.getElementById("other-birds");

  for (const id in birdData) {
    const bird = birdData[id];
    const card = createBirdCard(bird);
    
    if (bird.popular) {
      popularSection.appendChild(card);
    } else {
      otherSection.appendChild(card);
    }
  }
});

function createBirdCard(bird) {
  const col = document.createElement("div");
  col.className = "col-md-3 mb-3";

  const card = document.createElement("div");
  card.className = "card h-100";

  const img = document.createElement("img");
  img.src = bird.image;
  img.className = "card-img-top";
  img.alt = bird.title;

  const cardBody = document.createElement("div");
  cardBody.className = "card-body";

  const title = document.createElement("h5");
  title.className = "card-title";
  title.textContent = bird.title;

  const link = document.createElement("a");
  link.href = `/view/${bird.id}`;
  link.className = "btn btn-custom btn-sm mt-2";
  link.textContent = "View Bird";

  cardBody.appendChild(title);
  cardBody.appendChild(link);
  card.appendChild(img);
  card.appendChild(cardBody);
  col.appendChild(card);

  return col;
}
