/* particlesJS.load(@dom-id, @path-json, @callback (optional)); */
particlesJS.load('particles', '../static/js/particles.json', function() {
  console.log('callback - particles.js config loaded');
});

setTimeout(fade_out, 3000);

function fade_out() {
  const target = document.getElementById("flashes");
  target.style.display = "none";
}