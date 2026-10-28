const navButtons = document.querySelectorAll('.nav-item');
const panels = document.querySelectorAll('.panel');

navButtons.forEach((button) => {
  button.addEventListener('click', () => {
    navButtons.forEach((btn) => btn.classList.remove('active'));
    panels.forEach((panel) => panel.classList.remove('active'));

    button.classList.add('active');
    const target = document.getElementById(button.dataset.target);
    if (target) {
      target.classList.add('active');
    }
  });
});

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('service-worker.js').catch(() => {});
  });
}
