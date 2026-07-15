getData();

async function getData() {
  const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const data = await response.json();
  document.getElementById('character').innerHTML = data.name;
}