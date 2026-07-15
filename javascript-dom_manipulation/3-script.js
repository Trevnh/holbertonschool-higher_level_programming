document.getElementById('toggle_header').onclick = toggleHeader;

function toggleHeader() {
  header = document.querySelector('header');
  if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  } else if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  }
}