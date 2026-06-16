// Scroll progress bar
const bar = document.getElementById("progressBar");
function updateProgress() {
  const h = document.documentElement;
  const scrolled = h.scrollTop / (h.scrollHeight - h.clientHeight || 1);
  bar.style.width = Math.min(100, Math.max(0, scrolled * 100)) + "%";
}
document.addEventListener("scroll", updateProgress, { passive: true });
updateProgress();

// Reveal on scroll (IntersectionObserver, reduced-motion safe)
const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const reveals = document.querySelectorAll(".reveal");
if (reduce || !("IntersectionObserver" in window)) {
  reveals.forEach((el) => el.classList.add("in"));
} else {
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
  );
  reveals.forEach((el) => io.observe(el));
}

// Mark questions as answered
const form = document.getElementById("surveyForm");
function refreshAnswered() {
  form.querySelectorAll("fieldset.q").forEach((fs) => {
    const inputs = fs.querySelectorAll("input, textarea");
    let done = false;
    inputs.forEach((i) => {
      if (i.type === "radio" || i.type === "checkbox") {
        if (i.checked) done = true;
      } else if (i.value.trim() !== "") {
        done = true;
      }
    });
    fs.classList.toggle("answered", done);
  });
}
form.addEventListener("input", refreshAnswered);
form.addEventListener("change", refreshAnswered);

// Submit handling (sends to Google Sheets)
const SHEET_URL = "https://script.google.com/macros/s/AKfycbxy-zy-Jvy_TaBVKDPNXlYjyQ64M1XxLVz1owLV3O3UKGOjtV3EWWTMssJRRVbwxSAtGw/exec";

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const data = {};
  const fd = new FormData(form);
  for (const key of new Set([...fd.keys()])) {
    const all = fd.getAll(key);
    data[key] = all.length > 1 ? all : all[0];
  }

  const btn = form.querySelector('button[type="submit"]');
  btn.disabled = true;
  btn.textContent = "Wird gesendet …";

  fetch(SHEET_URL, {
    method: "POST",
    mode: "no-cors",
    body: JSON.stringify(data),
  })
    .then(() => {
      form.hidden = true;
      const thanks = document.getElementById("thanks");
      thanks.hidden = false;
      thanks.classList.add("in");
      window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" });
    })
    .catch(() => {
      alert("Fehler beim Senden. Bitte prüfe deine Internetverbindung und versuche es erneut.");
      btn.disabled = false;
      btn.textContent = "Antworten absenden";
    });
});

// Restart
document.getElementById("restart").addEventListener("click", () => {
  form.reset();
  refreshAnswered();
  form.hidden = false;
  document.getElementById("thanks").hidden = true;
  window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" });
});
