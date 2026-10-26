const terminal = document.getElementById("terminal");
const navButtons = document.querySelectorAll(".nav-btn");
const panels = document.querySelectorAll(".panel");

const commands = [
  "$ nmap -sV -Pn 10.0.2.0/24",
  "[+] scanning authorized lab network",
  "[+] host 10.0.2.15 is online",
  "[+] port 80/tcp Open HTTP",
  "[+] port 22/tcp Open SSH",
  "[+] analysis ready",
  "[+] scope confirmed: local network only"
];

let index = 0;

function typeCommand() {
  if (index < commands.length) {
    const line = document.createElement("div");
    line.textContent = commands[index];
    terminal.appendChild(line);
    index++;
    setTimeout(typeCommand, 220);
  }
}

navButtons.forEach((button) => {
  button.addEventListener("click", () => {
    navButtons.forEach((btn) => btn.classList.remove("active"));
    button.classList.add("active");

    const target = button.dataset.panel;
    panels.forEach((panel) => {
      panel.classList.toggle("visible", panel.id === target);
    });
  });
});

if (terminal) {
  typeCommand();
}

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("service-worker.js").catch(() => {});
  });
}
