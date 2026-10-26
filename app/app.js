const terminal = document.getElementById("terminal");

const commands = [
  "$ nmap -sV -Pn 10.0.2.0/24",
  "[+] scanning lab network",
  "[+] host 10.0.2.15 is online",
  "[+] port 80/tcp Open HTTP",
  "[+] port 22/tcp Open SSH",
  "[+] analysis ready"
];

let index = 0;

function typeCommand() {
  if (index < commands.length) {
    const line = document.createElement("div");
    line.textContent = commands[index];
    terminal.appendChild(line);
    index++;
    setTimeout(typeCommand, 200);
  }
}

typeCommand();
