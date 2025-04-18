// Astronomy Picture Loader
async function loadSpaceFact() {
    const date = document.getElementById("datePicker").value;
    const url = `/api/space-fact${date ? `?date=${date}` : ''}`;

    const res = await fetch(url);
    const data = await res.json();

    const html = `
      <h2 class="text-2xl font-semibold">${data.title} (${data.date})</h2>
      <img src="${data.url}" alt="${data.title}" class="rounded shadow mx-auto max-h-[500px]"/>
      <p class="text-gray-300 text-left">${data.explanation}</p>
    `;

    document.getElementById("content").innerHTML = html;
};

// Asteroid Modal
function openAsteroidModal() {
    document.getElementById("asteroidModal").classList.remove("hidden");
};
  
function closeAsteroidModal() {
    document.getElementById("asteroidModal").classList.add("hidden");
};

async function loadAsteroids() {
    const date = document.getElementById("asteroidDate").value;
    const container = document.getElementById("asteroidResults");
    container.innerHTML = "<p class='text-gray-300'>Loading space pebbles...</p>";
  
    try {
      const res = await fetch(`/api/asteroids?date=${date}`);
      const asteroids = await res.json();
  
      if (!asteroids.length) {
        container.innerHTML = "<p class='text-yellow-400'>No asteroids tracked on this day — space is calm. ☁️</p>";
        return;
      }
  
      container.innerHTML = asteroids.map(a => `
        <div class="bg-gray-700 p-3 rounded">
          <h3 class="font-bold text-lg">${a.name}</h3>
          <ul class="text-gray-200">
            <li><strong>Date:</strong> ${a.close_approach_date}</li>
            <li><strong>Size:</strong> ${a.estimated_diameter_km.toFixed(2)} km</li>
            <li><strong>Speed:</strong> ${a.relative_velocity_kmh.toFixed(0)} km/h</li>
            <li><strong>Miss Distance:</strong> ${a.miss_distance_km.toLocaleString()} km</li>
            <li><strong>Hazardous?</strong> ${a.is_potentially_hazardous ? "🚨 Yes" : "Nope 😌"}</li>
          </ul>
        </div>
      `).join("");
    } catch (err) {
        container.innerHTML = "<p class='text-red-400'>Something went wrong! Check your connection or NASA’s servers.</p>"
        console.error(err);
    }
};

// Set Default Dates on Load
document.addEventListener("DOMContentLoaded", () => {
    const today = new Date().toISOString().split("T")[0];
    document.getElementById("datePicker").value = today;
    document.getElementById("asteroidDate").value = today;

    loadSpaceFact();
});