getData();

async function getData() {
  const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
  const data = await response.json();
  document.getElementById('hello').innerHTML = data.hello;
}